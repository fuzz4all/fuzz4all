from typing import List
from coder_LM import BaseCoder

class StarCoder(BaseCoder):
    def __init__(self, coder_name: str, device: str, eos: List[str], max_length: int):
        super().__init__(coder_name, device, eos, max_length)
        self.prefix_token = "<fim_prefix>"
        self.suffix_token = "<fim_suffix><fim_middle>"

    def format_prompt(self, prompt: str) -> str:
        return f"{self.prefix_token}{prompt}{self.suffix_token}"