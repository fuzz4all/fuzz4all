import os
from enum import IntEnum


class LEVEL(IntEnum):
    INFO = 1  # most important message (are bugs found?, overview, etc)
    TRACE = 2
    VERBOSE = 3  # most verbose messages (including validation messages, etc)


class Logger:
    # logging structure breakdown into validation, and sample generation,
    # and any potential bugs are logged always in main log.txt
    # TODO: support logging levels
    def __init__(self, basedir, file_name: str, level: LEVEL = LEVEL.INFO):
        self.logfile = os.path.join(basedir, file_name)
        self.level = level

    @staticmethod
    def format_log(msg, level: LEVEL = LEVEL.VERBOSE):
        return f"[{level.name}] {msg}"

    def logo(self, msg, level: LEVEL = LEVEL.VERBOSE):
        try:
            with open(self.logfile, "a+", encoding="utf-8") as logfile:
                logfile.write(self.format_log(msg, level))
                logfile.write("\n")
            if level <= self.level:
                print(self.format_log(msg, level))
        except Exception as e:
            pass
