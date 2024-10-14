import pyttsx3
import speech_recognition as sr
import time
import random
import webbrowser
import datetime
from plyer import notification
import pyautogui
import wikipedia
import OpenAI


engine = pyttsx3.init()
voice=engine.getProperty('voice')
engine.setProperty('rate',130)


def speak(command):
    engine.say(command)
    engine.runAndWait()


def command():
    contant=" "
    while(contant==" "):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        try:
            contant=r.recognize_google(audio,language='en-in')
            print("You Said.......")
            print("Command=" + contant)
        except Exception as e:
            print("Please Try again...")
        return contant
    

def main_program():
    count =int(4)
    while True:
        request = command().lower()
        if "hello" in request:
            speak("welcome Ritik How can you help me?")
        elif "play music" in request:
            music_list = ["https://www.youtube.com/watch?v=mY9fNwGE7YA&list=RDMM7zsyCt0KQmA&index=4", "https://www.youtube.com/watch?v=QxddU3sjVRY&list=RDMM7zsyCt0KQmA&index=3", "https://www.youtube.com/watch?v=VB7tiQRPds4&list=RDMM7zsyCt0KQmA&index=2"]
            random_song = random.choice(music_list)
            speak("Playing... ")
            webbrowser.open( random_song)
        elif "say time" in request:
            current_time = datetime.datetime.now().strftime("%H:%M")
            speak("The current time is: " + current_time)
        elif "say date" in request:
            current_date = datetime.datetime.now().strftime("%d-%m")
            speak("The current date is: " + current_date)
        elif "new task" in request:
            task=request.replace("new task","")
            task.strip()
            if task!="":
                speak("New task added: " + task)
                with open("tasks.txt","a") as f:
                    f.write(task + "\n")
        elif "speak task" in request:
            with open("tasks.txt","r") as f:
                tasks = f.readlines()
                speak("Here are your tasks:")
                for i, task in enumerate(tasks):
                    speak(str(i+1) + ". " + task.strip())
        elif "show task" in request:
            with open("tasks.txt","r") as f:
                tasks=f.read()
            speak("Here are your tasks:")
            notification.notify(
                title="Today task",
                message=tasks
            )
        elif "open youtube" in request:
            webbrowser.open("https://www.youtube.com")
        elif "open" in request:
            query = request.replace("open", "")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            speak("Opening " + query)
            pyautogui.press("enter")
        elif "wikipedia" in request:
            request=request.replace("wikipedia", "")
            request=request.replace("search", "")
            request=request.replace("matrix", "")
            result=wikipedia.summary(request,sentences=2)
            speak(result)
        elif "search google" in request:
            query = request.replace("search google", "")
            webbrowser.open("https://www.google.com/search?q=" + query)
        elif "matrix" in request:
            query=request.replace("matrix", "")
            res=OpenAI.Ai(query)
            # history.append(res)
            print(res)
            # speak("The answer is: " + 
            speak(res)
        else:
            if count==0:
                print("I'm sorry, I couldn't understand that. Please try again.")
                speak("I'm sorry, I couldn't understand that. Please try again.")
                count=4
            else:
                time.sleep(1)
                count-=1
                continue

main_program()