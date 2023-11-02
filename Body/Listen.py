import socket

def test_net():
    try:
        socket.create_connection(('Google.com', 80))
        return True
    except OSError:
        return False



# import speech_recognition as sr
# from googletrans import Translator


# def Listen():


#     r = sr.Recognizer()

#     with sr.Microphone() as source:
#         print(": Listening... ")
#         r.pause_threshold = 2
#         audio = r.listen(source, 0, 8)

#     try:
#         print(": Recognizing... ")
#         query = r.recognize_google(audio,language='en-in')
#         print(f": Your Command : {query}\n")

#     except:
#         return ""

#     query = str(query).lower()
#     return query




# def MicExecution():
#     query = Listen()
#     data = TrnslationHinToEng(query)
#     return data


from vosk import Model, KaldiRecognizer
import pyaudio
import sys

model = Model("Database\\vosk-model-en-in-0.5")
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

def Listen():
    print("")
    print("Listening...")
    
    while True:
        try:

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
            break

if __name__ == "__main__":

    while True:
        Listen()
