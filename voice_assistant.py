import speech_recognition as sr
import pyttsx3
import pywhatkit
import webbrowser
import wikipedia


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def command_take():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}\n")
        except Exception as e:
            print("Sorry, I did not understand that. Could you please say that again?")
            speak("Sorry, I did not understand that. Could you please say that again?")
            return "None"
        return command.lower()


def command_handle(command):
    if 'play' in command:
        song = command.replace('play', '')
        speak(f"Playing {song}")
        pywhatkit.playonyt(song)
    elif 'open youtube' in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif 'open google' in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif 'search' in command:
        query = command.replace('search', '')
        speak(f"Searching {query} on Google")
        pywhatkit.search(query)
    elif 'who is' in command or 'what is' in command:
        query = command.replace('who is', '').replace('what is', '')
        speak(f"Searching {query} on Wikipedia")
        result = wikipedia.summary(query, sentences=2)
        speak(result)
    else:
        speak("Sorry, I can only perform basic tasks like playing songs, opening YouTube, and searching Google.")

def main():
    speak("Hello, how can I help you today?")
    while True:
        command = command_take()
        if command == "none":
            continue
        if 'exit' in command or 'stop' in command:
            speak("Goodbye!")
            break
        command_handle(command)

if __name__ == "__main__":
    main()
