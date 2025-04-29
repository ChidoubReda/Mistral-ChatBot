import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file
API_KEY = os.getenv("OPENROUTER_API_KEY")

def generate_response(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",  # Or your project name
    }

    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        return response.json()['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    while True:
        user_input = input("Enter your prompt: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            break
        response = generate_response(user_input)
        print("ChatBot:", response)
