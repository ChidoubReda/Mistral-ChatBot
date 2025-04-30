import requests
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")  # Load variables from .env file
API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    print("❌ API key not found. Please check your .env file.")
    exit()

def generate_response(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
    }

    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        print("🔄 Sending request to OpenRouter...")
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        result = response.json()
        print("✅ Response received.")

        if "choices" in result:
            
            return result["choices"][0]["message"]["content"].strip()
            

        else:
            print(f"Loaded API key: {API_KEY[:8]}...")  # Print first few chars only
            return f"API Error: {result}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    while True:
        user_input = input("Enter your prompt: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            break
        response = generate_response(user_input)
        print("ChatBot:", response)
