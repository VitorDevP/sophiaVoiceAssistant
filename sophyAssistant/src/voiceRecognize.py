import speech_recognition as sr

def recordAudio():
    # Record The Audio
    r = sr.Recognizer()  # Creating a recognizer object

    try:
        # Open the microphone and start recording
        with sr.Microphone() as source:
            print('Say something!')
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source, phrase_time_limit=2)

        # Use google's speech recognition
        data = ''
    
        data = r.recognize_google(audio)
        # data = r.recognize_sphinx(audio)
        print('You said: ' + data)
    except sr.UnknownValueError:  # Checking for unknown errors
        print('Google Speech Recognition could not understand the audio')
    except sr.RequestError as c:
        print('Request results from Google Speech Recognition service error')

    return data
