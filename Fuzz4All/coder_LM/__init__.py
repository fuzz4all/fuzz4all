from typing import List
from .starcoder import StarCoder
from .deepseek import DeepSeekCoder

def build_coder_LM(coder_name: str, eos: List, device: str, max_length: int):
    """Returns a llm coder instance (optional: using the configuration file)."""

    kwargs_for_coder = {
        "coder_name": coder_name,
        "eos": eos,
        "device": device,
        "max_length": max_length,
    }
    # print the coder config
    print("=== coder Config ===")
    print(f"coder_name: {coder_name}")
    for k, v in kwargs_for_coder.items():
        print(f"{k}: {v}")
    coder_class = (
        DeepSeekCoder if "deepseek" in coder_name.lower()
        else StarCoder
    )
    coder_LM = coder_class(**kwargs_for_coder)
    coder_LM_class_name = coder_LM.__class__.__name__
    print(f"coder_obj (class name): {coder_LM_class_name}")
    print("====================")
    return coder_LM
