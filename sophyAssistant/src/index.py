from speech import assistantResponse
from voiceRecognize import listen
from intents.intent import intentCall
from tools.load import loadFile
from tools.sounds import beep, beep2

config = loadFile('config.json')
STT = listen()

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

if __name__ == "__main__":
    # assistantResponse("hello i'm {0}, i'm your voice assistant, you can call me with hey {0}, ok {0} or just call my name".format(config['assistant']['name']))

    while True:
        text = STT.listening()
        
        responses = ''

        if wakeWord(text.lower()) == True:
            try:
                beep()
    
                responses = responses + intentCall()

                if len(responses) > 0:
                    assistantResponse(responses)
                
                beep2()
            except Exception as e:
                responses = responses + ''
