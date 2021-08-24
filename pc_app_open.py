import main_mimi as m;
import os



def open_application(input):
      
    if "chrome" in input:
        m.mimi_speak("Opening Google Chrome")
        os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')
        return
  
    elif "mysql" in input or "sql" in input:
        m.mimi_speak("Opening MySql Workbench")
        os.startfile('C:\Program Files\MySQL\MySQL Workbench 8.0\MySQLWorkbench.exe')
        return

    elif "spring" in input or "sts" in input:
        m.mimi_speak("Opening Spring Tool Suite")
        os.startfile('E:\sts-4.10.0.RELEASE\SpringToolSuite4.exe')
        return

    elif "control" in input or "control panel" in input:
        m.mimi_speak("Opening Control Panel")
        os.startfile('Control Panel\All Control Panel Items')
        return

  
    else:
  
        m.mimi_speak("Application not available")
        return