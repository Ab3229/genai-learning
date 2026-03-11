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
- Respond strictly in JSON with keys "step" and "content"
- Follow step sequence strictly: start → plan → display
- One step at a time
- Valid steps are only: "start", "plan", "display"
"""

message_history = [
    {"role": "system", "content": system_prompt},
]

user_query = input("👉 ")
message_history.append({"role": "user", "content": user_query})

while True:
    response = client.chat.completions.create(
        model="gemini-3-flash-preview",
        response_format={"type": "json_object"},
        messages=message_history
    )

    raw_result = response.choices[0].message.content
    message_history.append({"role": "assistant", "content": raw_result})
    parsed_result = json.loads(raw_result)

    step = parsed_result.get("step")
    content = parsed_result.get("content")

    if step == "start":
        print("🔥", content)
        # Nudge the model to move to the next step
        message_history.append({"role": "user", "content": "Proceed to the next step."})

    elif step == "plan":
        print("🔥🔥", content)
        message_history.append({"role": "user", "content": "Proceed to the next step."})

    elif step == "display":
        print("🤖", content)
        break

    else:
        print(f"⚠️ Unknown step '{step}', stopping.")
        break