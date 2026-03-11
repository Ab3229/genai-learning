from dotenv import load_dotenv
from google import genai
load_dotenv()

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Are you become my valentine!"
)
print(response.text)