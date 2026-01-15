import os
import requests

API_URL = os.getenv("HF_API_URL")
HF_TOKEN = os.getenv("HF_TOKEN")

def generate_ai_text(prompt):
    if not API_URL or not HF_TOKEN:
        return f"[AI MOCK OUTPUT]\n{prompt}"

    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    payload = {"inputs": prompt}

    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()[0]["generated_text"]
