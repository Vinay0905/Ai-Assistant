import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener=aa.Recognizer()

machine = pyttsx3.init()
def talk(text):
    machine.say(text)

machine.runAndWait()

def input_instruction():
    global instruction
    try:
        with aa.Microphone() as origin:
            print("listening")
            speech=listener.listen(origin)
            
            instruction= listener.recognize_google(speech)
            instruction=instruction.lower()
            if "Jarvis" in instruction:
                instruction=instruction.replace('Jarvis',' ')
                print(instruction)
    except:
        pass
    return instruction

def Play_Jarvis():
    instruction = input_instruction
    print(instruction)
    if "play" in instruction:
        song = instruction.replace("play",'')
        talk("playing"+ song)
        pywhatkit.playonyt(song)


    elif 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M%p')
        talk("current time "+ time)

    elif 'date' in instruction:
        date=datetime.datetime.now().strftime('%d /%m / % Y')
        talk("Today's date"+ date )
        
    elif 'how are u' in instruction:
        talk=('I am Fine,how about you?')

    elif 'What is your name'in instruction:
        talk("I am Jarvis, What can I do for you?")

    elif 'who is' in instruction:
        human = instruction.replace('who is'," ")
        information = wikipedia.summary(human,1)
        print(information)
        talk(information)

    else:
        talk('Please repeat')

Play_Jarvis()