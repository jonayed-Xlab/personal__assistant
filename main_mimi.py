import pyttsx3  #pip install pyttsx3

#my files import
import get_audio as audio
import process_text



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("rate", 145)
engine.setProperty('voice', voices[1].id)

'''
speak function
'''

f = open("py_file/name.txt", "r")

def mimi_speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__=="__main__":
    mimi_speak("how i can help you?" + f.read())
    while True:
        text = audio.get_audio() 
        if text == 0:
            continue
        if ("sleep" in text) or ("stop" in text) or ("silent" in text):
            mimi_speak("good bye")
            break

        process_text.process(text)