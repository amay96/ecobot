import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

def get_ai_response(user_input: str) -> str:
    lowered_input = user_input.lower()

    # ✅ Custom manual override
    if "who created you" in lowered_input or "who made you" in lowered_input:
        return "I was created by Amay Upadhyay 👨‍💻."
    if "your name" in lowered_input:
        return "I'm Eco AI Bot, your friendly sustainable assistant 🌱."
    if "president" in lowered_input and "india" in lowered_input:
        return "As of 2025, the President of India is Droupadi Murmu 🇮🇳."

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://openrouter.ai",
        "X-Title": "Eco Clean Bot"
    }

    system_prompt = (
        "You are a helpful and smart AI assistant. If the user asks anything related to cleaning, give eco-friendly, natural tips otherwise Don't. "
        "For all other topics, behave like a general assistant chatbot. Answer with useful and relevant information."
        "You can also give general knowledge answers as well."
        "You can also have basic conversation"
    )

    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    }

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=data,
            timeout=20
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error: {e}"
