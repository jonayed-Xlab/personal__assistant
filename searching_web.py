from selenium import webdriver # to control browser operations



#my files import
import main_mimi as m

def search_web(text):
    text = text.lower()
    driver = webdriver.Chrome(executable_path='C:\\Users\\mdjon\\Downloads\\chromedriver.exe')
	# driver.implicitly_wait(1)
    driver.maximize_window()

    if 'youtube' in text:
        m.mimi_speak("Opening in youtube")
        indx = text.split().index('youtube')
        query = text.split()[indx + 1:]
        driver.get("https://www.youtube.com/results?search_query=" + '+'.join(query))

        
    elif 'wikipedia' in text:
        m.mimi_speak("Opening Wikipedia")
        indx = text.split().index('wikipedia')
        query = text.split()[indx + 1:]
        driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))
    elif 'google' in text:
        m.mimi_speak("Opening Google")
        indx = text.split().index('google')
        query = text.split()[indx + 1:]
        driver.get("https://www.google.com/search?q=" + '+'.join(query))

    elif 'search' in text:
        m.mimi_speak("Opening Google")
       # indx = text.split().index('google')
        #query = text.split()[indx + 1:]
        driver.get("https://www.google.com/search?q=" + '+'.join(text.split()))

    else:
        driver.get("https://www.google.com/search?q=" + '+'.join(text.split()))

	

