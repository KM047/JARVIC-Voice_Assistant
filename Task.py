import datetime
from Body.Speak import Speak
from PIL import ImageGrab
import pyautogui
import keyboard


def Time():
    time = datetime.datetime.now().strftime("%I : %M %p")
    Speak(time)

def Date():
    date = datetime.date.today()
    Speak(date)

# def Day():
#     day = datetime.datetime.now().strftime("%A")
#     Speak(day)

def SS():
    screenshot = ImageGrab.grab()
    current_timestamp = datetime.datetime.today().strftime('%Y-%m-%d_%H-%M-%S')
    screenshot.save(f"Screenshot/{current_timestamp}.jpg")
    Speak('Screenshot taken successfully')


def NonInput(query):
    query = str(query)

    if "time" in query:
        Time()

    elif "date" in query:
        Date()

    # elif "day" in query:
    #     Day()
    
    elif "screenshot" in query:
        SS()


def Input_task(tag, query):

    if "wikipedia" in tag:
        try:
            import wikipedia
            name = str(query).replace("wikipedia","").replace("who is","").replace("about","").replace("what","")
            result = wikipedia.summary(name)
            # return result
            print(result)

        except:
            print("Check your internet connection!")

    
    elif "google" in tag:
        try:
            from pywhatkit import misc
            name = str(query).replace("google","").replace("google search","").replace("search","").replace("find","")
            misc.search(name)

        except:
            print("Check your internet connection!")
    
    elif "open" in tag:


        from time import sleep
        name = str(query).replace("open", "").replace("jarvis", "")
        pyautogui.press('super')
        sleep(0.5)
        keyboard.write(name)
        sleep(0.5)
        keyboard.press('enter')
        sleep(0.5)

    elif "site" in tag:
        import webbrowser

        name = str(query).replace("launch", "").replace("visit", "").replace("jarvis", "")
        Link = 'https://www.'+ name + '.com'
        webbrowser.open(Link)

    elif "remember" in tag:
        remembermsg = str(query).replace("remember", "").replace("that", "").replace("jarvis", "")
        Speak(f"You told me"+remembermsg)
        with open("Remember.txt", 'a') as msg:
            msg.write(remembermsg+"\n")

        Speak("I remember that sir..")

    elif "recall" in tag:
        with open("Remember.txt", 'r') as f:
            Speak("You told me that :" + f.read())
        # remsg = retrieve.read()
        # retrive.close()
        # Speak("You told me"+ remsg )

        # Speak("You told me"+ str(retrive.read()))

