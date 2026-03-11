from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

# Gemini client initialize
client = genai.Client()

# Image URL
image_url = "https://images.pexels.com/photos/19284512/pexels-photo-19284512.jpeg"

# Generate caption
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        "Generate a caption for this image aboput 50 words.",
        {
            "mime_type": "image/jpeg",
            "uri": image_url
        }
    ]
)

print("Response:", response.text)