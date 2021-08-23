# my files import
import main_mimi as m
import searching_web as web
import get_audio as audio
import pc_app_open as app
from googletrans import Translator, constants
'''
1.processing user text in program
'''
translator = Translator()

def process(user_text):
    try:
        if 'search' in user_text or 'play' in user_text:
            web.search_web(user_text)

        elif "who are you" in user_text or "define yourself" in user_text:
            speak = '''Hello, I am your personal Assistant.
            I am here to make your life easier. You can command me to perform
            various tasks such as searching google or opening applications etcetra'''
            m.mimi_speak(speak)
  
        elif "who made you" in user_text or "created you" in user_text:
            speak = "I have been created by Junayed."
            m.mimi_speak(speak)  

        elif 'open' in user_text:
            app.open_application(user_text) 
           
        else:
            m.mimi_speak("I can search the web for you, Do you want to continue?")
            ans = audio.get_audio()
            if 'yes' in ans or 'yeah' in ans:
                web.search_web(user_text)
              
    except:
       return
                  

