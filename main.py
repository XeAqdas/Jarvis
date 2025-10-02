import os
import sys
import sounddevice as sd
import numpy as np
import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import pywhatkit

# --- Securely load API keys from environment variables ---
# NOTE: You must set these variables in your system for the script to work.
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Check if essential API keys are set
required_keys = {
    "NEWS_API_KEY": NEWS_API_KEY,
    "OPENWEATHERMAP_API_KEY": OPENWEATHERMAP_API_KEY,
    "OPENROUTER_API_KEY": OPENROUTER_API_KEY
}
missing_keys = [key for key, value in required_keys.items() if not value]
if missing_keys:
    print(f"Error: The following environment variables are not set: {', '.join(missing_keys)}")
    print("Please set them before running the script.")
    sys.exit(1) # Exit the script if keys are missing

# Initialize speech engine
engine = pyttsx3.init()

# Speak Function
def speak(text):
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# Record Audio using sounddevice
def record_audio(duration=2, fs=16000):
    print("Listening...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype=np.int16)
    sd.wait()
    return np.squeeze(audio)

# Speech Recognition
def recognize_speech(duration=2):
    recognizer = sr.Recognizer()
    audio_np = record_audio(duration)
    audio_bytes = audio_np.tobytes()
    audio_data = sr.AudioData(audio_bytes, 16000, 2)
    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return "Speech Recognition error"

# Ask AI using OpenRouter
def askAI(question):
    try:
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "You are Jarvis, a helpful AI assistant."},
                {"role": "user", "content": question}
            ]
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            reply = response.json()["choices"][0]["message"]["content"]
            return reply.strip()
        else:
            return "Sorry, I couldn't process your request."
    except Exception as e:
        return f"Error: {e}"

# Command Processor
def processCommand(command):
    command = command.lower()

    if "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")
    elif "open facebook" in command:
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook.")
    elif "open linkedin" in command:
        webbrowser.open("https://www.linkedin.com")
        speak("Opening LinkedIn.")
    elif "play" in command:
        song = command.replace("play", "").strip()
        speak(f"Playing {song} on YouTube.")
        pywhatkit.playonyt(song)
    elif "news" in command:
        r = requests.get(f"https://newsapi.org/v2/top-headlines?q=technology&apiKey={NEWS_API_KEY}")
        if r.status_code == 200:
            data = r.json()
            articles = data['articles']
            if articles:
                speak("Here are the top news headlines:")
                for article in articles[:5]:
                    title = article['title']
                    speak(title)
                    print(title)
    elif "weather" in command:
        city = command.replace("weather", "").strip()
        
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP_API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            weather_desc = data['weather'][0]['description']
            speak(f"The current temperature in {city} is {temp} degrees Celsius with {weather_desc}.")
        else:
            speak(f"Sorry, I couldn't find the weather for {city}.")

    elif "shutdown" in command or "exit" in command or "stop" in command:
        speak("Shutting down. Goodbye!")
        print("Jarvis has been shut down.")
        exit()
    else:
        answer = askAI(command)
        print(answer)
        speak(answer)

# Main Loop with Wake Word
if __name__ == "__main__":
    speak("Hello, I am Jarvis, your personal assistant.")
    while True:
        print("Say 'Jarvis' to activate...")
        wake_word = recognize_speech(duration=2)

        if wake_word and "jarvis" in wake_word.lower():
            speak("Yes?")
            print("Jarvis is active. Listening for command...")
            command = recognize_speech(duration=3)
            if command:
                print(f"You said: {command}")
                processCommand(command)
            else:
                speak("I didn't hear any command.")