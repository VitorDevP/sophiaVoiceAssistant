from tools.load import loadFile
from speech import assistantResponse
from voiceRecognize import recordAudio
from intents.timedate import timeDate_intent as timeDate
from intents.weather import wheather_intent as weather
import random, os, sys
from multiprocessing import Process

loadModel = loadFile('models/dictionary.json')

Greeting_Response = loadModel['greetings']['responses']

cancle = ["ok!", "no problem", ""]

intents = [weather.callActions(), timeDate.callActions()]

def intentCall():
    assistantResponse(random.choice(Greeting_Response))
    count = 0
    while count<3:
        text = recordAudio()

        if len(text) > 0:
            if 'cancel' in text:
                return random.choice(cancle)
            
            intent = getIntent(text)
            assistantResponse(intent)
            count = 1
        elif count == 0:
            assistantResponse(random.choice(Greeting_Response))
        count += 1
    return ""
# for intent in os.listdir('./sophyAssistant/src/intents'):
#     if os.path.isdir('./sophyAssistant/src/intents/'+intent) and intent in sys.modules:
#         sys.modules[intet]
#     elif os.path.isdir('./sophyAssistant/src/intents/'+intent):    
#         __import__("weather.wheather_intent", fromlist=[''])
        

def getIntent(text):
    for intent in intents:
        if text in intent[0]:
            return intent[1]
    return "could not understand"