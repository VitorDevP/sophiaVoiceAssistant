import speech_recognition as sr
import tools.connections as internet

class listen:
    def __init__(self):
        self.internetConnection = internet.available()
        self.r = sr.Recognizer()  # Creating a recognizer object
        
    def recordAudio(self):
        # Record The Audio    
            
        # Open the microphone and start recording
        with sr.Microphone() as source:
            print('Say something!')
            self.r.adjust_for_ambient_noise(source, duration=1)
            audio = self.r.listen(source, phrase_time_limit=2)

        return audio

    def recognizePhrase(self, audio):
        try:
            data = ''

            if(self.internetConnection): 
                data = self.r.recognize_google(audio)
            else:
                data = self.r.recognize_sphinx(audio)

            print('You said: ' + data)
        except sr.UnknownValueError:  # Checking for unknown errors
            print('Google Speech Recognition could not understand the audio')
        except sr.RequestError as c:
            print('Request results from Google Speech Recognition service error')

        return data
    
    def listening(self):
        audio = self.recordAudio()
        text = self.recognizePhrase(audio)
        return text