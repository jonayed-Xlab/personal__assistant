# my files import
from os import close
import main_mimi as m
import searching_web as web
import get_audio as audio
import pc_app_open as app
import taskbar_access as ta
import keyboard
import pyautogui
'''
1.processing user text in program
'''


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

        elif 'number' in user_text:
            m.mimi_speak("Opening Taskbar Application")
            ta.taskbar(user_text)

        elif 'close' in user_text:
            m.mimi_speak("Closing Opened Application")
            keyboard.send("alt+F4, space")

        elif 'minimize' in user_text or 'minimise' in user_text or 'minimice' in user_text:
            m.mimi_speak("Minimize Opened Application")
            pyautogui.hotkey('winleft', 'd') 

        elif 'maximize' in user_text or 'maximise' in user_text or 'maximice' in user_text:
            m.mimi_speak("Maximize Opened Application")
            pyautogui.hotkey('winleft', 'up') 

        elif 'mize' in user_text or 'mise' in user_text or 'mice' in user_text:
            m.mimi_speak("medium Opened Application")
            pyautogui.hotkey('winleft', 'down') 
        
        elif 'full' in user_text or 'full screen' in user_text or 'normal' in user_text or 'normal screen' in user_text:
            m.mimi_speak("full Screened Application")
            pyautogui.hotkey('F11') 


        else:
            m.mimi_speak("I can search the web for you, Do you want to continue?")
            ans = audio.get_audio()
            if 'yes' in ans or 'yeah' in ans:
                web.search_web(user_text)          
    except:
       return
                  

