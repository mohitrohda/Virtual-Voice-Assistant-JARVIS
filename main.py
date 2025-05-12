import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import openai
from gtts import gTTS
import pygame
import os

openai.api_key = "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"

# pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init() 
newsapi = "a4d9d69d06fa43dcba7b09c01940a4ba"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    os.remove("temp.mp3") 

def aiProcess(command):
    openai.api_key = "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"
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please."},
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message.content


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak("Sorry, song not found.")

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])

    else:
        # Let OpenAI handle the request
        output = aiProcess(c)
        speak(output) 





if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
               print("Listening...")
               audio = r.listen(source, timeout=5, phrase_time_limit=5)
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Ya")
                with sr.Microphone() as source:
                     print("Jarvis Active...")
                     audio = r.listen(source, timeout=5, phrase_time_limit=5)
                     command = r.recognize_google(audio)
                     processCommand(command)

        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start.")

        except sr.UnknownValueError:
            print("Could not understand the audio.")
  
        except Exception as e:
            print(f"Unknown Error: {e}")


