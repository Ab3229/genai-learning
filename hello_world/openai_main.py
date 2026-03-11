from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key="AIzaSyAJERUYdJp3FNz610wHYunIJ9XEl9-TOqU",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {   "role": "system",
            "content": "you are expert in joke on girls who show attitude, i know"
        },
        {
            "role": "user",
            "content": "write a joke"
        }
    ]
)

print(response.choices[0].message.content)