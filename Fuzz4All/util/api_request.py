import os
import signal
import time

import openai

# openai.api_key = os.environ.get("OPENAI_API_KEY", "dummy")
# client = openai.OpenAI()

openai_client = openai.OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY", "dummy"),
    timeout=120.0  
)

# 2. Gemini Client (Using Google's OpenAI compatibility layer)
gemini_client = openai.OpenAI(
    api_key=os.environ.get("GEMINI_API_KEY", "dummy"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    timeout=120.0
)

# 3. Grok Client (xAI's OpenAI compatible endpoint)
grok_client = openai.OpenAI(
    api_key=os.environ.get("XAI_API_KEY", "dummy"),
    base_url="https://api.x.ai/v1",
    timeout=120.0
)
def create_openai_config(
    prompt,
    engine_name="code-davinci-002",
    stop=None,
    max_tokens=200,
    top_p=1,
    n=1,
    temperature=0,
):
    return {
        "model": model_name,
        "prompt": prompt,
        "max_tokens": max_tokens,
        "top_p": top_p,
        "temperature": temperature,
        "logprobs": 1,
        "n": n,
        "stop": stop,
    }


def create_config(
    prev: dict,
    messages: list,
    max_tokens: int,
    temperature: float = 1.0,
    model: str = "gpt-3.5-turbo",
):
    if prev == {}:
        return {
            "model": model,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "messages": messages,
        }
    else:
        return prev


def handler(signum, frame):
    # swallow signum and frame
    raise Exception("I have become end of time")

def request_engine(config):
    """Handles requests to OpenAI, Gemini, and Grok APIs."""
    ret = None
    
    # 1. Determine which client to use based on the model name prefix
    model_name = config.get("model", "")
    active_client = openai_client
    
    if model_name.startswith("gemini/"):
        active_client = gemini_client
        config["model"] = model_name.split("/", 1)[1]  # Strip prefix before sending
    elif model_name.startswith("grok/"):
        active_client = grok_client
        config["model"] = model_name.split("/", 1)[1]  # Strip prefix before sending

    # 2. Execute the request with modern error handling
    while ret is None:
        try:
            # Route to the correct endpoint based on the config structure
            if "messages" in config:
                ret = active_client.chat.completions.create(**config)
            else:
                ret = active_client.completions.create(**config)
                
        except openai.BadRequestError as e:
            print(f"[ERROR] Bad Request: {e}")
            break  # Break the loop since retrying a fundamentally bad request won't fix it
        except openai.RateLimitError as e:
            print(f"[WARNING] Rate limit exceeded for {model_name}. Waiting...")
            time.sleep(5)
        except openai.APIConnectionError as e:
            print(f"[WARNING] API connection error for {model_name}. Waiting...")
            time.sleep(5)
        except openai.APITimeoutError as e:
            print(f"[WARNING] Request timed out for {model_name}. Retrying...")
            time.sleep(2)
        except openai.APIError as e:
            print(f"[ERROR] API Error: {e}")
            time.sleep(2)
        except Exception as e:
            print(f"[ERROR] Unknown error: {e}. Waiting...")
            time.sleep(1)
            
    return ret