import requests, os, dotenv

BASE_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL_NAME = "openai/gpt-oss-20b"


dotenv.load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

def ask_ai(prompt, model = MODEL_NAME):
    headers = {
        "Authorization": f"Bearer {API_KEY}", 
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(BASE_URL, headers=headers, json=payload)
    response.raise_for_status()
    data = response.json()
    return data["choices"][0]["message"]["content"]

# question = ask_ai("Generate a simple addition question in mathematics, in one line")
# answer = ask_ai(question)

# print(question, "is", answer)