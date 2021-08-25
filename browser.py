import pyautogui
import main_mimi as m

def browser_access(text):
    if "refresh" in text or "fresh" in text:
        m.mimi_speak("rerfesh page")
        pyautogui.hotkey('F5') 
    elif "left" in text:
        pyautogui.hotkey('alt','left')

    elif "right" in text:
        pyautogui.hotkey('alt','right')

    elif "bottom" in text:
        pyautogui.hotkey('end')

    elif "top" in text:
        pyautogui.hotkey('home')

    elif "down" in text:
        pyautogui.hotkey('space')

    elif "up" in text:
        pyautogui.hotkey('shift','space')

    elif "new" in text:
        pyautogui.hotkey('ctrl','tab')

    elif "drop" in text:
        pyautogui.hotkey('ctrl' , 'F4') 

    elif "next" in text:
        pyautogui.hotkey('ctrl','tab')  

    elif "back" in text:
        pyautogui.hotkey('ctrl', 'shift', 'tab') 

    elif "search" in text:
        pyautogui.hotkey('browsersearch')       



    

