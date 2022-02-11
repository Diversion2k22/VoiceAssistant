import os , sys
import wikipedia
import webbrowser
import speech_recognition as spr
import pyttsx3 as sx3
import datetime
#import spotify
#import instagram




engine = sx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(aud):
    engine.say(aud)
    engine.runAndWait()

def Greet():
    #It will Greet the user and provide its services
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12 :
        speak("Good Morning... Have a nice day!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    elif hour>=18 and hour<21:
        speak("Good Evening!")

    else:
        speak("Good Night!")

    speak("Hi I am your personal assistant Zoey . Please tell how may i help you")

def Command():
    #It take voice inputs and help the user accordingly
    v = spr.Recognizer()
    with spr.Microphone() as micro:
        print("...Speak Now...")
        v.pause_threshold = 1
        aud = v.listen(micro)
        
    try:
        print("...Processing...")
        query = v.recognize_google(aud, language='en-in')
        print(f"...{query}...\n")
        
    except Exception as e:
        #print(e)
        
        print("...Unable to Understand...\n...Please Repeat...")
        return "None"
    return query


if __name__ == "__main__":
    Greet()
    while True:
        query = Command().lower()
        if 'search' in query:
            
            query = query.replace("search","")
            result = wikipedia.summary(query, sentences = 2)
            
            speak(result)
            
        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"{time} is the time")
            speak(f"{time} is the time")
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open netflix' in query:
            webbrowser.open("netflix.com")
            
        elif 'open amazon' in query:
            webbrowser.open("amazon.com")
            
        elif 'open zoom' in query:
            path =  'C:\\Users\\reliance\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe'
            os.startfile(path)
            
        elif 'open chrome' in query:
            path =  'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
            os.startfile(path)
            
        elif 'open brave'  in query:
            path =  'C:\\Program Files (x86)\\Google\\Chrome\\Application\\brave.exe'
            os.startfile(path)

        elif 'open excel' in query:
            path =  "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(path)
            
        elif 'open settings' in query:
            path =  "C:\\Windows\\System32\\Control.exe"
            os.startfile(path)
            
        elif 'exit' in query:
            speak("Powering Off!")
            sys.exit()
            
            
