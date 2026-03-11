from dotenv import load_dotenv
import os
import speech_recognition as sr
from gtts import gTTS
import playsound
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

# Speech recognizer
r = sr.Recognizer()

# conversation memory
messages = []


def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "response.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def listen():
    with sr.Microphone() as source:

        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 2

        print("🎤 Speak Something...")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print("You:", text)
            return text
        except:
            print("Could not understand audio")
            return None


def ask_gemini(prompt):

    messages.append({"role": "user", "parts": [prompt]})

    response = model.generate_content(messages)

    ai_text = response.text

    messages.append({"role": "model", "parts": [ai_text]})

    return ai_text
