import os
import signal
import time

import openai

openai.api_key = os.environ.get("OPENAI_API_KEY", "dummy")
client = openai.OpenAI()


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
        "engine": engine_name,
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
    temperature: float = 2,
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


# Handles requests to OpenAI API
def request_engine(config):
    ret = None
    while ret is None:
        try:
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(120)  # wait 10
            ret = client.chat.completions.create(**config)
            signal.alarm(0)
        except openai._exceptions.BadRequestError as e:
            print(e)
            signal.alarm(0)
        except openai._exceptions.RateLimitError as e:
            print("Rate limit exceeded. Waiting...")
            print(e)
            signal.alarm(0)  # cancel alarm
            time.sleep(5)
        except openai._exceptions.APIConnectionError as e:
            print("API connection error. Waiting...")
            signal.alarm(0)  # cancel alarm
            time.sleep(5)
        except Exception as e:
            print(e)
            print("Unknown error. Waiting...")
            signal.alarm(0)  # cancel alarm
            time.sleep(1)
    return ret
