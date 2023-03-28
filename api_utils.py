# api_utils.py
import openai
from typing import Optional

MODEL_NAME = "text-davinci-003"

def call_api(prompt: str, max_tokens: int = 1000, temperature: float = 0.7, top_p: float = 1, n: int = 1) -> str:
    response = openai.Completion.create(model=MODEL_NAME, prompt=prompt, max_tokens=max_tokens, temperature=temperature, top_p=top_p, n=n)
    return response["choices"][0]["text"]

def generate_email_content(email_prompt: str) -> Optional[str]:
    try:
        return call_api(email_prompt)
    except openai.OpenAIError as e:
        print(f"Error generating email: {e}")
        return None
