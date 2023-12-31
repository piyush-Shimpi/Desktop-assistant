# Personal Desktop Assistance

import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import wikipedia #pip install wikipedia
import requests #pip install requests
import winsound
import webbrowser
import datetime
import os
import smtplib
import json

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir . I am a Personal desktop assistant")        
    speak("Please tell me how may I help you.")
    speak("If you dont know how to use a desktop assistant") 
    speak("just speak word information to get all details.")


def takeCommand():
   #if you your microphone is not working still ou can use this using inputs
        r = input("Enter the task \n") 
        query = r
         
    #It takes microphone input from the user and returns string output
    #  r = sr.Recognizer()
    #  with sr.Microphone() as source:
    #     print("Listening...")
    #     r.pause_threshold = 1
    #     audio = r.listen(source)
    
     
    
        # try:
        #     print("Recognizing...")    
        #     query = r.recognize_google(audio, language='en-in')
        #     print(f"User said: {query}\n")

        # except Exception as e:
        #     print(e)    
        #     print("Say that again please...")  
        #     return "None"
        return query

def make_note():
    
    speak("press1 for voice command press2 for write command")
    user = int(input("Enter option:"))
    if user == 1:
        speak("what should I write?")
        note_content = takeCommand()
    else:
        speak("what should I write?")
        note_content=input("")
    with open("notes.txt","a") as file:
        file.write(note_content + "\n")
    speak("The note is successfully written")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def get_weather(city):
    api_key = "4cb8f3c8871e87460f114abf452af0f7"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(base_url)
    data = json.loads(response.text)
    if data["cod"] != "404":
        main_info = data["weather"][0]["main"]
        descripton = data["weather"][0]["main"]
        temperature = data["main"]["temp"]
        speak(f"currently, the weather in {city} is {main_info}.the temperature is {temperature} kelvin.")
    else:
        speak("Sorry i couldn't fetch the weather information")

def set_alarm(time):
    alarm_time = datetime.datetime.strptime(time,"%H:%M")
    current_time = datetime.datetime.now().strptime(time,"%H:%M")

    while current_time != alarm_time.strptime(time,"%H:%M"):
        current_time = datetime.datetime.now().strptime(time,"%H:%M")
        frequency = 2500
        duration = 1000 #milisecond
        winsound.Beep(frequency,duration)
    speak("Alarm is set!")

   

def quit():
    speak("Thanks for using Jarvis")
    speak("have a nice day")
    
def my_info():
    speak("I am a model which is build using python")
    speak("several python modules were use to build as i can perform various task.")
    speak("telling current time , weather, sending emails , setting an alarm, make notes and store them.")
    speak("I can also provide quick web search")    
    speak("just tell the operation you want to perform i will execute it for you")

#main function

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open spotify' in query:
            webbrowser.open("spotify.com")   
        
        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'tell time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "D:\Piyush Btech\Microsoft VS Code\code.exe"
            os.startfile(codePath)

        elif 'email to piyush' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "shimpipiyush2003@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry piyush email can't be send")
        
        elif 'search on google' in query:
            speak("What would you like me to search?")
            search_query = takeCommand()
            webbrowser.open(f"https://www.google.com/search?q={search_query}")

        elif 'open file'in query:
            speak("Please provide me a file path?")
            file_path = takeCommand()
            os.startfile(file_path)

        elif 'weather' in query:
            try:
                speak("Sure! please tell me the name of your city?")
                city_name = takeCommand()
                get_weather(city_name)
            except Exception as z :
                print(z)
                speak("you are not connected to a network")

        elif 'make a note' in query:
            speak("sure! tell what to note.")
            make_note()

        elif 'set alarm' in query:
            speak("Alright sir, for when?")
            tell_time = takeCommand()
            set_alarm(tell_time)
        
        elif 'information' in query:
            my_info()           
        
        elif 'quit' in query:
            quit()
            break
