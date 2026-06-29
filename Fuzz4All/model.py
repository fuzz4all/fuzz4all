import os
import re
import time
import textwrap
import requests
from typing import Any, Dict, List, Optional, Tuple, Union

import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    StoppingCriteria,
    StoppingCriteriaList,
)

from ollama import Client, ResponseError

torch.cuda.empty_cache()
os.environ["TOKENIZERS_PARALLELISM"] = "false"  # disable warning
EOF_STRINGS = ["<|endoftext|>", "###"]


# ==========================================
# Routing & Helper Functions
# ==========================================

def is_ollama_model(model_name: str) -> bool:
    return model_name.startswith("ollama/")

def is_ollama_cloud_model(model_name: str) -> bool:
    return model_name.startswith("ollama-cloud/")

def is_gemini_model(model_name: str) -> bool:
    return model_name.startswith("gemini/")

def get_pure_model_name(model_name: str) -> str:
    """Strips the prefix (e.g., 'gemini/gemma...' becomes 'gemma...')"""
    if "/" in model_name:
        return model_name.split("/", 1)[1]
    return model_name

def make_model(eos: list, model_name: str, device: str, max_length: int):
    pure_name = get_pure_model_name(model_name)
    
    if is_ollama_model(model_name):
        return None  # Let target.py handle local Ollama natively
    elif is_ollama_cloud_model(model_name):
        return OllamaCloudAPI(pure_name, eos)
    elif is_gemini_model(model_name):
        return GeminiAPI(pure_name, eos)
    else:
        return StarCoder(model_name, device, eos, max_length)


# ==========================================
# Cloud API Classes
# ==========================================

class GeminiAPI:
    """Class to handle Google's Gemini API via REST"""
    def __init__(self, model_name: str, eos: Optional[List[str]] = None) -> None:
        self.model_name = model_name if model_name else "gemma-4-31b-it"
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY environment variable is not set.")
            
        self.endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model_name}:generateContent?key={self.api_key}"
        combined_eos = EOF_STRINGS + (eos if eos else [])
        self.eos = combined_eos[:5]

    def generate(self, prompt: str, batch_size: int = 1, temperature: float = 1.0, max_length: int = 4096) -> List[str]:
        outputs = []
        headers = {"Content-Type": "application/json"}
        
        for _ in range(batch_size):
            data = {
                "system_instruction": {
                    "parts": [{"text": "You are a pure code generator. Output ONLY valid Python code. "
                                       "Do not include explanations, comments about your plan, "
                                       "or any conversational text. No preamble, no postscript."}]
                },
                "contents": [{"parts": [{"text": prompt}]}],
                "generationConfig": {
                    "temperature": 0.1, 
                    "maxOutputTokens": max_length,
                    "stopSequences": self.eos,
                }
            }
            
            total_sleep_time = 0
            max_retries = 3
            
            for attempt in range(max_retries):
                try:
                    response = requests.post(self.endpoint, headers=headers, json=data)                    
                    if response.status_code >= 500:
                        wait_time = 2 ** attempt
                        print(f"[WARNING] Google Server Error ({response.status_code}). Retrying in {wait_time}s...")
                        time.sleep(wait_time)
                        total_sleep_time += wait_time
                        continue
                    
                    if response.status_code == 429:
                        print("[WARNING] Rate limit exceeded. Waiting 5s...")
                        time.sleep(5)
                        total_sleep_time += 5
                        continue

                    response.raise_for_status()
                    res_data = response.json()
                    
                    try:
                        raw_text = res_data["candidates"][0]["content"]["parts"][0]["text"]
                        matches = re.findall(r'```python[ \t]*\n(.*?)\n[ \t]*```', raw_text, re.DOTALL)

                        if matches:
                            content = textwrap.dedent(matches[-1].replace('\xa0', ' ')).strip()
                        else:
                            content = raw_text.strip()                       
                                                
                        outputs.append(content)
                        break  
                        
                    except (KeyError, IndexError):
                        print(f"[ERROR] Unexpected response structure from Gemini.")
                        outputs.append("")
                        break
                        
                except Exception as e:
                    print(f"[ERROR] Gemini API Call failed: {e}")
                    if attempt == max_retries - 1:
                        outputs.append("")
            
            if total_sleep_time > 0:
                print(f"[INFO] Gemini Total time spent sleeping: {total_sleep_time} seconds.")
                
        return outputs


class OllamaCloudAPI:
    """Class to handle Ollama Cloud using the official python client"""
    def __init__(self, model_name: str, eos: Optional[List[str]] = None) -> None:
        self.model_name = model_name if model_name else "qwen3-coder:480b-cloud"
        self.api_key = os.getenv("OLLAMA_API_KEY")
        if not self.api_key:
            raise ValueError("OLLAMA_API_KEY environment variable is not set.")
            
        self.client = Client(
            host="https://ollama.com",
            headers={'Authorization': 'Bearer ' + self.api_key}
        )
        
        combined_eos = EOF_STRINGS + (eos if eos else [])
        self.eos = combined_eos[:4]

    def generate(self, prompt: str, batch_size: int = 1, temperature: float = 1.0, max_length: int = 4096) -> List[str]:
        outputs = []
        
        for _ in range(batch_size):
            messages = [
                {"role": "system", "content": "You are a pure code generator. Output ONLY valid Python code. "
                                              "Do not include explanations, comments about your plan, "
                                              "or any conversational text. No preamble, no postscript."},
                {"role": "user", "content": prompt}
            ]
            
            options = {
                "temperature": 0.1,  
                "num_predict": max_length, 
                "stop": self.eos
            }

            total_sleep_time = 0
            max_retries = 3
            
            for attempt in range(max_retries):
                try:
                    response = self.client.chat(
                        model=self.model_name, 
                        messages=messages, 
                        stream=False,
                        options=options
                    )
                    
                    try:
                        raw_text = response.get("message", {}).get("content", "")
                        matches = re.findall(r'```python[ \t]*\n(.*?)\n[ \t]*```', raw_text, re.DOTALL)

                        if matches:
                            content = textwrap.dedent(matches[-1].replace('\xa0', ' ')).strip()
                        else:
                            content = raw_text.strip()                       
                                                
                        outputs.append(content)
                        break  
                        
                    except (KeyError, IndexError, AttributeError):
                        print(f"[ERROR] Unexpected response structure from Ollama Cloud.")
                        outputs.append("")
                        break

                except ResponseError as e:
                    if e.status_code >= 500:
                        wait_time = 2 ** attempt
                        print(f"[WARNING] Ollama Cloud Error ({e.status_code}). Retrying in {wait_time}s...")
                        time.sleep(wait_time)
                        total_sleep_time += wait_time
                        continue
                    
                    if e.status_code == 429:
                        print("[WARNING] Ollama Cloud Rate limit exceeded. Waiting 5s...")
                        time.sleep(5)
                        total_sleep_time += 5
                        continue
                    
                    print(f"[ERROR] Ollama API Error: {e.error} (Status: {e.status_code})")
                    if attempt == max_retries - 1:
                        outputs.append("")
                    break
                    
                except Exception as e:
                    print(f"[ERROR] Ollama Client Call failed: {e}")
                    if attempt == max_retries - 1: 
                        outputs.append("")
                    break

            if total_sleep_time > 0:
                print(f"[INFO] Ollama Cloud total time spent sleeping: {total_sleep_time} seconds.")
            
        return outputs


# ==========================================
# Original HuggingFace / Local Models
# ==========================================

class EndOfFunctionCriteria(StoppingCriteria):
    def __init__(self, start_length, eos, tokenizer, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_length = start_length
        self.eos = eos
        self.tokenizer = tokenizer
        self.end_length = {}

    def __call__(self, input_ids, scores, **kwargs):
        """Returns true if all generated sequences contain any of the end-of-function strings."""
        decoded_generations = self.tokenizer.batch_decode(
            input_ids[:, self.start_length :]
        )
        done = []
        for index, decoded_generation in enumerate(decoded_generations):
            finished = any(
                [stop_string in decoded_generation for stop_string in self.eos]
            )
            if (
                finished and index not in self.end_length
            ):  # ensures first time we see it
                for stop_string in self.eos:
                    if stop_string in decoded_generation:
                        self.end_length[index] = len(
                            input_ids[
                                index,  # get length of actual generation
                                self.start_length : -len(
                                    self.tokenizer.encode(
                                        stop_string,
                                        add_special_tokens=False,
                                        return_tensors="pt",
                                    )[0]
                                ),
                            ]
                        )
            done.append(finished)
        return all(done)


class StarCoder:
    def __init__(
        self, model_name: str, device: str, eos: List, max_length: int
    ) -> None:
        checkpoint = model_name
        self.device = device
        self.tokenizer = AutoTokenizer.from_pretrained(
            checkpoint,
        )
        self.model = (
            AutoModelForCausalLM.from_pretrained(
                checkpoint,
            )
            .to(torch.bfloat16)
            .to(device)
        )
        self.eos = EOF_STRINGS + eos
        self.max_length = max_length
        self.prefix_token = "<fim_prefix>"
        self.suffix_token = "<fim_suffix><fim_middle>"
        self.skip_special_tokens = False

    @torch.inference_mode()
    def generate(
        self, prompt, batch_size=10, temperature=1.0, max_length=512
    ) -> List[str]:
        input_str = self.prefix_token + prompt + self.suffix_token
        input_tokens = self.tokenizer.encode(input_str, return_tensors="pt").to(
            self.device
        )

        scores = StoppingCriteriaList(
            [
                EndOfFunctionCriteria(
                    start_length=len(input_tokens[0]),
                    eos=self.eos,
                    tokenizer=self.tokenizer,
                )
            ]
        )

        raw_outputs = self.model.generate(
            input_tokens,
            max_length=min(self.max_length, len(input_tokens[0]) + max_length),
            do_sample=True,
            top_p=1.0,
            temperature=max(temperature, 1e-2),
            num_return_sequences=batch_size,
            stopping_criteria=scores,
            output_scores=True,
            return_dict_in_generate=True,
            repetition_penalty=1.0,
            pad_token_id=self.tokenizer.eos_token_id,
        )
        gen_seqs = raw_outputs.sequences[:, len(input_tokens[0]) :]
        gen_strs = self.tokenizer.batch_decode(
            gen_seqs, skip_special_tokens=self.skip_special_tokens
        )
        outputs = []
        # removes eos tokens.
        for output in gen_strs:
            min_index = 10000
            for eos in self.eos:
                if eos in output:
                    min_index = min(min_index, output.index(eos))
            outputs.append(output[:min_index])
        return outputs