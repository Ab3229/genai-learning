from dotenv import load_dotenv
from openai import OpenAI
import os
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

system_prompt = """
You are a coding assistant.

Rules:
- Only answer coding-related questions
- Respond strictly in JSON
- Follow step sequence: start → plan → display
- One step at a time
"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": system_prompt},
        {
            "role": "user",
            "content": "Solve 2 + 3"
        },
        {
            "role": "assistant",
            "content": json.dumps({
                "step": "start",
                "content": "User wants to solve a simple math expression."
            })
        },
        {
            "role": "assistant",
            "content": json.dumps({
                "step": "plan",
                "content": "Add the two numbers and compute the result."
            })
        },
        {
            "role": "assistant",
            "content": json.dumps({
                "step": "display",
                "content": "The result of 2 + 3 is 5."
            })
        },
        {
            "role": "user",
            "content": "Write a function that adds two numbers"
        },
       {
           "role":"user",
           "content":json.dumps(
               {"step": "start", "content": "User wants a function that adds two numbers."}
           )
       },
          {
           "role":"user",
           "content":json.dumps(
               {"step": "plan", "content": "Define a function that takes two arguments, adds them together, and returns the sum. I will provide an example in Python."}
           )
       },
    ]
)

print(response.choices[0].message.content)