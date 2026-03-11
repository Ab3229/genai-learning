from dotenv import load_dotenv
import os
import uuid
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


# ---------------- SPEAK FUNCTION ---------------- #

def speak(text):

    filename = f"{uuid.uuid4()}.mp3"

    tts = gTTS(text=text, lang="en")
    tts.save(filename)

    playsound.playsound(filename)

    os.remove(filename)


# ---------------- LISTEN FUNCTION ---------------- #

def listen():

    with sr.Microphone() as source:

        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1

        print("🎤 Speak Something...")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print("You:", text)
            return text

        except:
            print("❌ Could not understand audio")
            return None


# ---------------- GEMINI FUNCTION ---------------- #

def ask_gemini(prompt):

    messages.append({"role": "user", "parts": [prompt]})

    response = model.generate_content(messages)

    ai_text = response.text

    messages.append({"role": "model", "parts": [ai_text]})

    return ai_text


# ---------------- MAIN PROGRAM ---------------- #

def main():

    print("🤖 Gemini Voice Assistant Started")

    while True:

        user_input = listen()

        if user_input is None:
            continue

        if user_input.lower() in ["exit", "quit", "stop", "bye"]:
            speak("Goodbye")
            break

        ai_response = ask_gemini(user_input)

        print("AI:", ai_response)

        speak(ai_response)


# ---------------- RUN ---------------- #

if __name__ == "__main__":
    main()