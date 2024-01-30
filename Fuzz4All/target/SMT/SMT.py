import subprocess
import time
from typing import List, Union

import torch

from Fuzz4All.target.target import FResult, Target
from Fuzz4All.util.Logger import LEVEL
from Fuzz4All.util.util import comment_remover


def _check_sat(stdout):
    sat = ""
    for x in stdout.splitlines():
        if "an invalid model was generated" in x.strip():
            sat = "invalid model"
            return sat

    for x in stdout.splitlines():
        if x.strip() == "unknown" or x.strip() == "unsupported":
            sat = "unknown"
            return sat

    for x in stdout.splitlines():
        if x.strip() == "unsat" or x.strip() == "sat":
            sat = x.strip()
            break
    return sat


# why is this needed? because sometimes the error could be suppressed in
# the return code of the smt solver however such error still exists.
def _check_error(stdout):
    error = False
    for x in stdout.splitlines():
        if x.strip().startswith("(error"):
            error = True
            break
    return error


# ignore cvc5 unary minus
# TODO: add additional rewriting rule to fix this
def _check_cvc5_parse_error(stdout):
    error = False
    for x in stdout.splitlines():
        if "Parse Error:" in x.strip():
            error = True
            break
    return error


class SMTTarget(Target):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = None  # to be declared
        if kwargs["template"] == "fuzzing_with_config_file":
            config_dict = kwargs["config_dict"]
            self.prompt_used = self._create_prompt_from_config(config_dict)
            self.config_dict = config_dict
        else:
            raise NotImplementedError

        self.special_eos = "#|"

    def write_back_file(self, code):
        try:
            with open(
                "/tmp/temp{}.smt2".format(self.CURRENT_TIME), "w", encoding="utf-8"
            ) as f:
                f.write(code)
        except:
            pass
        return "/tmp/temp{}.smt2".format(self.CURRENT_TIME)

    def wrap_prompt(self, prompt: str) -> str:
        return (
            f"; {prompt}\n{self.prompt_used['separator']}\n{self.prompt_used['begin']}"
        )

    def wrap_in_comment(self, prompt: str) -> str:
        return f"; {prompt}"

    def filter(self, code) -> bool:
        if "assert" not in code:
            return False
        return True

    def clean(self, code: str) -> str:
        # remove logic set which can lead to parse errors
        # clean_code = "\n".join(
        #     [x for x in code.splitlines() if not x.startswith("(set-logic")]
        # )
        clean_code = comment_remover(code, lang="smt2")
        clean_code = "\n".join(
            [x for x in clean_code.splitlines() if not x.startswith("(set-option :")]
        )
        clean_code = "\n".join(
            [x for x in clean_code.splitlines() if not x.startswith("(get-proof)")]
        )
        return clean_code

    # remove any comments, or blank lines
    def clean_code(self, code: str) -> str:
        clean_code = comment_remover(code, lang="smt2")
        code = "\n".join(
            [
                line
                for line in clean_code.split("\n")
                if line.strip() != "" and line.strip() != self.prompt_used["begin"]
            ]
        )
        return code

    def validate_individual(self, filename) -> (FResult, str):
        try:
            cvc_exit_code = subprocess.run(
                f"{self.target_name} -m -i -q --check-models --lang smt2 {filename}",
                shell=True,
                capture_output=True,
                text=True,
                timeout=5,
            )
        except subprocess.TimeoutExpired as te:
            pname = f"'{filename}'"
            subprocess.run(
                ["ps -ef | grep " + pname + " | grep -v grep | awk '{print $2}'"],
                shell=True,
            )
            subprocess.run(
                [
                    "ps -ef | grep "
                    + pname
                    + " | grep -v grep | awk '{print $2}' | xargs -r kill -9"
                ],
                shell=True,
            )  # kill all tests thank you
            return FResult.TIMED_OUT, "CVC5 Timed out"
        except UnicodeDecodeError as ue:
            return FResult.FAILURE, "UnicodeDecodeError"

        if cvc_exit_code.returncode != 0:
            return FResult.FAILURE, "CVC5:\n{}".format(
                cvc_exit_code.stdout + cvc_exit_code.stderr,
            )

        return FResult.SAFE, "its safe"
