import speech_recognition as sr # getting user voice by microphone



'''
1. get audio from user 
2. user audio convert it into text
'''

def get_audio():
    r = sr.Recognizer()
    audio = ''
    with sr.Microphone() as source:
        print("lisiting...")
        r.pause_threshold = 0.8
        audio = r.listen(source,phrase_time_limit = 5)
    try: 
        text = r.recognize_google(audio,language="en")  
        print("Recognizing...")
        print("You : ",text)

    except Exception as e:
        print("say again please...")
        return 0 

    return text.lower()       
       