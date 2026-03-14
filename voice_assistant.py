
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio)
        print("You said:", command)

    except Exception as e:
        print("Please say again...")
        return ""

    return command.lower()

def run_assistant():

    speak("Hello, I am your voice assistant")

    while True:

        command = take_command()

        if "time" in command:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print("Current Time:", current_time)
            speak("The time is " + current_time)

        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
                            
        elif "wikipedia" in command:
            speak("Searching Wikipedia")
            command = command.replace("wikipedia", "")
            result = wikipedia.summary(command, sentences=2)
            print(result)
            speak(result)

        elif "exit" in command:
            speak("Goodbye")
            break

run_assistant()
