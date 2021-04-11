import calendar
import datetime
import random
from tools.load import loadFile

def greeting(text):
    loadModel = loadFile('models/dictionary.json')
    Greeting_Inputs = loadModel['greetings']['inputs']
    Greeting_Response = loadModel['greetings']['responses']

    for word in text.split():
        if word.lower() in Greeting_Inputs:
            return random.choice(Greeting_Response)
    return "what's your desire"

