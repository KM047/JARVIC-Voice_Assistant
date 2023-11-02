import pyttsx3

def Speak(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    engine.setProperty('rate', 170)
    print("")
    print(f"Jarvis : {Text}.")
    print("")
    engine.say(Text)
    engine.runAndWait()


if __name__ == "__main__":

    Speak("Hello ")