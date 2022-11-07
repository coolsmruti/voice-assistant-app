
import pyttsx3 as tts
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit
import pyjokes

engine = tts.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning!')

    elif hour>=12 and hour<18:
        speak('Good Afternoon!')

    else:
        speak('Good Evening!')

    speak(" How are you?? I am Layla. How can I help you Sir?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        
        r.pause_threshold = 1
        audio = r.listen(source)
    

    try:

        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()

        if 'who' in query:
            speak('Searching Wikipedia...')
            query = query.replace("who", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com") 

        elif 'open chrome' in query:
            webbrowser.open("chrome.com")

        elif 'open chrome browser' in query:
            webbrowser.open("chromebrowser.com")

        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'email' in query:
            webbrowser.open("gmail.com")

        elif 'play music' in query:
            music_dir = 'E:\\song'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")    

        elif 'the code' in query:
            path = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'date' in query:
            speak('sorry, please find someone else i am not free today.')

        elif 'are you single' in query:
            speak('please mind your business.')

        elif 'exit' in query:
            speak('okay tata.')

        else:
            speak('Please say it again.')