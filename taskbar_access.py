import keyboard
import main_mimi as m

def taskbar(text):
    try:
        if "one" in text or " 1" in text:
            keyboard.press_and_release('windows + 1')
            
        elif "two" in text or "2" in text:
            keyboard.press_and_release('windows + 2')
           
        elif "three" in text or "3" in text:
            keyboard.press_and_release('windows + 3')
           
        elif "four" in text or "4" in text:
            keyboard.press_and_release('windows + 4')
           
        elif "five" in text or "5" in text:
            keyboard.press_and_release('windows + 5')
            
        elif "six" in text or "6" in text:
            keyboard.press_and_release('windows + 6')
            
        elif "seven" in text or "7" in text:
            keyboard.press_and_release('windows + 7')
            
        elif "eight" in text or "8" in text:
            keyboard.press_and_release('windows + 8')
            
        elif "nine" in text or "9" in text:
            keyboard.press_and_release('windows + 9')
            
        else:
            return
    except:
        return
