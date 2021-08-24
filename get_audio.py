import speech_recognition as sr # getting user voice by microphone



'''
1. get audio from user 
2. user audio convert it into text
'''

def get_audio():

    r = sr.Recognizer() 
    with sr.Microphone() as source:
        r.energy_threshold = 50
        print("mimi : lisiting...") 
        audio = r.listen(source, phrase_time_limit=7)
        text = ''
    try: 
        text = r.recognize_google(audio,language="en")  
        print("You : ",text)

    except Exception as e:
        print("say again please...")
        return 0 

    return text.lower()       
       