import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand.")
            return ""
        except sr.RequestError:
            speak("Could not connect to the internet.")
            return ""

def run_assistant():
    command = listen()
    
    if "play" in command:
        song = command.replace("play", "").strip()
        speak(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song)
    
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {time}")
    
    elif "search" in command:
        query = command.replace("search", "").strip()
        speak(f"Searching for {query}")
        pywhatkit.search(query)
    
    elif "who is" in command or "what is" in command:
        query = command.replace("who is", "").replace("what is", "").strip()
        info = wikipedia.summary(query, sentences=1)
        speak(info)
    
    elif "exit" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("I didn't understand. Please try again.")

# Run the assistant in a loop
while True:
    run_assistant()
