from typing import List
from coder_LM import BaseCoder

class DeepSeekCoder(BaseCoder):
    def __init__(self, coder_name: str, device: str, eos: List[str], max_length: int):
        super().__init__(coder_name, device, eos, max_length)

    def format_prompt(self, prompt: str) -> str:
        # DeepSeek doesn’t need special tokens; return as-is
        return prompt
