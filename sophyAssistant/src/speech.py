import pyttsx3
engine = pyttsx3.init()
from gtts import gTTS
import playsound
from pathlib import Path
from tools.load import loadFile
import re

config = loadFile('config.json')

def assistantResponse(text):
    tts = gTTS(text=text, lang=config['assistant']['lang'])
    playsound.playsound(saveAudio(tts, text))

def saveAudio(audio, name):
    name = re.sub('\W+', '', name)+'.mp3'
    if Path(name).is_file():
        return name
    else:
        audio.save(name)
        return name
