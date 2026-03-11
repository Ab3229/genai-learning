from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key="AIzaSyAJERUYdJp3FNz610wHYunIJ9XEl9-TOqU",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def main():
    user_query = input("> ")

    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {
                "role": "user",
                "content": user_query
            }
        ]
    )

    print(": ", response.choices[0].message.content)


main()