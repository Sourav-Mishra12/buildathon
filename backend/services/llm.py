
# if using ollama local model

# import ollama

# MODEL_NAME = "llama3:8b"

# def call_llm(prompt: str) -> str:
#     response = ollama.chat(
#         model=MODEL_NAME,
#         messages=[
#             {"role": "user", "content": prompt}
#         ]
#     )
#     return response["message"]["content"]

# if using GROQ API

from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def call_llm(prompt: str) -> str:
    chat = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}]
    )
    return chat.choices[0].message.content
