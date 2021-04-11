from speech import assistantResponse
from voiceRecognize import recordAudio
from intents.intent import intentCall
from tools.load import loadFile
import playsound

config = loadFile('config.json')

def wakeWord(text):
    words = loadFile('models/dictionary.json')

    WAKE_WORD = words['wakeAssistance']['inputs']

    text = text.lower()

    for phrase in WAKE_WORD:
        if (phrase + " " + config['assistant']['name']) in text:
            return True
        elif config['assistant']['wakeupJustName'] and config['assistant']['name'] in text:
            return True

    return False

while True:
    text = recordAudio()
    responses = ''

    if wakeWord(text.lower()) == True:
        try:
            playsound.playsound('beep.mp3')
            responses = responses + intentCall()

            if len(responses) > 0:
                assistantResponse(responses)
            playsound.playsound('beep2.mp3')
        except Exception as e:
            responses = responses + ''
