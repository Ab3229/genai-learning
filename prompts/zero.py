# from dotenv import load_dotenv
# from openai import OpenAI

# load_dotenv()

# client = OpenAI(
#     api_key="AIzaSyAJERUYdJp3FNz610wHYunIJ9XEl9-TOqU",
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# )

# system_prompt="Your name is lucky. you should only and only answer coding question,do not answer anything else.if user ask  something other than coding question .then reply ,sorry  i am busy now !"
# # zero shot prompting : directily giving the instruction  to the model without prior example
# question=input("write your question!")
# response = client.chat.completions.create(
#     model="gemini-3-flash-preview",
#     messages=[
#         {   "role": "system",
#             "content": system_prompt
#         },
#         {
#             "role": "user",
#             "content": question
#         }
#     ]
# )

# print(response.choices[0].message.content)

from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client=OpenAI(
    
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
system_prompt=" you are expert in genral knowledge"
response=client.chat.completions.create(
   model="gemini-2.5-flash",
    messages=[
        {
          "role":"system",
          "content":"system_prompt",
        },
        {
            "role":"user",
            "content":"who  is prime minister of india",
        }
    ]
)
print(response.choices[0].message.content)