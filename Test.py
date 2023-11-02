import socket
from vosk import Model, KaldiRecognizer
import pyaudio
import sys
import speech_recognition as sr
import os

model = Model("Database\\vosk-model-small-en-in-0.4")
recognizer = KaldiRecognizer(model, 16000)

# mic = pyaudio.PyAudio()
# stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
# stream.start_stream()
# os.system('cls')


def test_net():
    try:
        socket.create_connection(('Google.com', 80))
        check = 1
        
    except OSError:
        check = 2
        

    if check == 1:

        def Listen():
            
            r = sr.Recognizer()

            with sr.Microphone() as source:
                print(": Listening... ")
                r.pause_threshold = 1
                audio = r.listen(source, 0, 7)

            try:
                print(": Recognizing... ")
                query = r.recognize_google(audio, language='en-in')
                print(f": Your Said : {query}\n")
                query = str(query).lower()
                return query

            except:
                return ""

            # return query.lower()
        return Listen()
        # Listen()

    else:
        
        def Listen():
            print("")
            print(": Listening...")
            print("")

            while True:
                try:
                    mic = pyaudio.PyAudio()
                    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
                    stream.start_stream()

                    data = stream.read(4096)    #4096

                    if recognizer.AcceptWaveform(data):
                        text = recognizer.Result()
                        p = text[14:-3]
                        print(f"You Said : {p}")

                        if len(p) > 0:
                            return p

                        else:
                            break
                except:
                    return ""
                    
        return Listen()
        # Listen()

# test_net()

# socket.create_connection(('Google.com', 80))
# socket.create_connection(('Google.com', 80))


# print("0")