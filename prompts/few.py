from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),  
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

system_prompt = """
Your name is Lucky.
You answer only coding-related questions.

Rules:
- If question is coding related → is_allow = true
- Otherwise → is_allow = false
- Output must be strictly in JSON format

Output format:
{
  "code": "string",
  "is_allow": boolean
}

Examples:

Q: What is Python?
A:
{
  "code": "Python is a high-level programming language.",
  "is_allow": true
}

Q: Who are you?
A:
{
  "code": "sorry i am busy now !",
  "is_allow": false
}
"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "what is gen ai7l"}
    ]
)

print(response.choices[0].message.content)