import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser
from tkinter import *
import re



recognizer = sr.Recognizer()
engine = pyttsx3.init()



voices = engine.getProperty('voices')

voice_index = 0


engine.setProperty('voice', voices[voice_index].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    if 'play' in command:
        video = command.replace('play', '')
        speak('Playing ' + video)
        pywhatkit.playonyt(video)
    elif 'search' in command:
        query = command.replace('search', '')
        speak('Searching Wikipedia for ' + query)
        results = wikipedia.summary(query, sentences=2)
        speak('According to Wikipedia')
        speak(results)
    elif 'google' in command:
        query = command.replace('google', '')
        speak('Searching Google for ' + query)
        search_url = "https://www.google.com/search?q=" + query
        webbrowser.open(search_url)
    elif 'draw' in command:
        shape = command.replace('draw', '')
        speak('Drawing ' + shape)
        draw_shape(shape)
    elif 'who is' in command:
        human = command.replace('who is'," ")
        information = wikipedia.summary(human,1)
        print(information)
        speak(information)
    elif 'stop' in command:
        speak('Goodbye!have a nice day.')
        exit()
    elif 'thank you' in command:
        speak("ohh it is my pleasure....come back when u need more info.")
        exit()
    elif 'good morning' in command:
        speak("Good Morning mate how are You.")
    else:
        # Check if the command contains a mathematical expression
        match = re.match(r'[\d+\-*/\s]+', command)
        if match and match.group() == command:
            try:
                result = eval(command)
                speak("The result is: " + str(result))
            except Exception as e:
                speak("Sorry, I couldn't perform the calculation.")
        else:
            speak("Sorry, I didn't understand that.")
def draw_shape(shape):
    window = Tk()
    canvas = Canvas(window, width=400, height=400)
    canvas.pack()

    if shape == 'square':
        canvas.create_rectangle(100, 100, 300, 300)
    elif shape == 'triangle':
        canvas.create_polygon(200, 100, 100, 300, 300, 300)
    elif shape == 'circle':
        canvas.create_oval(100, 100, 300, 300)
    else:
        speak("Sorry, I don't know how to draw that shape.")

    window.mainloop()
while True:
    try:
        with sr.Microphone() as source:
            speak("hi,how may i help you.")
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

            command = recognizer.recognize_google(audio)
            command = command.lower()

            print("You said:", command)
            process_command(command)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
