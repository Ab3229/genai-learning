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
  you are ai persona ai assiant name axtron.
   you are 22 yesrs old young tech person who lovw coding.
   
   exaMPLE:
   Q> HEY/
   A>WHAT UP GUYS!
   
"""
response = client.chat.completions.create(
model="gemini-3-flash-preview",
messages=[
    {
        "role":"user",
        "system":system_prompt
    },
    {
        "role":"user",
        "content":"Hey there!"
    }
]
)
print(response.choices[0].message.content)