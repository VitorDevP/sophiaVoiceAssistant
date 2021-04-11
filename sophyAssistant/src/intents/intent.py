from tools.load import loadFile
from speech import assistantResponse
from voiceRecognize import listen
from intents.timedate import timeDate_intent as timeDate
from intents.weather import wheather_intent as weather
from intents.assistant import assistant_intent as assistant
import random, os, sys
from multiprocessing import Process

loadModel = loadFile('models/dictionary.json')

Greeting_Response = loadModel['greetings']['responses']

cancle = ["ok!", "no problem", ""]
cancelWords = ['cancel', 'thanks']

intents = [weather.callActions(), timeDate.callActions(), assistant.callActions()]

STT = listen() #obj to convert speech to text

def intentCall():
    assistantResponse(random.choice(Greeting_Response))
    count = 0
    while count<3:
        text = STT.listening()

        if len(text) > 0:
            for cancelWord in cancelWords:
                if cancelWord in text:
                    return random.choice(cancle)
            
            intent = getIntent(text)
            assistantResponse(intent)
            count = 1
        elif count == 0:
            assistantResponse(random.choice(Greeting_Response))
        count += 1
    return ""

def getIntent(text):
    for intent in intents:
        if text in intent[0]:
            return intent[1]
    return "could not understand"