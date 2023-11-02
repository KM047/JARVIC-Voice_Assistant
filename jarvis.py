import random
import json
import torch
from Brain import NeuralNet
from NeuralNetwork import bag_of_words, tokenize
import os
import pyautogui
import wikipedia


from controlD import *
from Test import test_net
from Body.Listen import Listen
from Body.Speak import Speak
from Task import NonInput
from Task import Input_task

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open("intents.json", 'r') as json_data:
    intents = json.load(json_data)

FILE = "Traindata.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

# ------------------------------------------------------------------

Name = "Jarvis"



os.system("cls")

def main():

    # Starting line

    Speak("Hello sir, I am jarvis .")
    Speak("How can I Help You ?")

    while True:

        sen = str(test_net())
        order = sen

        if sen == "bye" or sen == "exit" or sen == "close" or sen == "ok exit":
            ByeReplyList = ['Bye Sir',
                            "It'll be Nice To Meet You Again.",
                            'Bye Sir, Have a Nice Day.']
            Ans = random.choice(ByeReplyList)
            Speak(Ans)
            exit()

        sen = tokenize(sen)
        X = bag_of_words(sen, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(device)

        output = model(X)
        _, predicted = torch.max(output, dim=1)

        tag = tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]
        if prob.item() > 0.75:
            for intent in intents['intents']:
                if tag == intent["tag"]:
                    reply = random.choice(intent["responses"])
                    if "time" in reply:
                        NonInput(reply)

                    elif "date" in reply:
                        NonInput(reply)

                    # elif "day" in reply:
                    #     NonInput(reply)

                    elif "screenshot" in reply:
                        NonInput(reply)

                    # ------------------------------------------------------------------------------------

                    elif "wikipedia" in reply:
                        try:
                            import wikipedia
                            name = str(order).replace("wikipedia","").replace("who is","").replace("about","").replace("what","")
                            result = wikipedia.summary(name)
                            # return result
                            print(result)

                        except:
                            print("Check your internet connection!")
                        # Input_task(reply, order)

                    elif "open" in reply:
                        Input_task(reply, order)

                    elif "google" in reply:
                        Input_task(reply, order)

                    elif "site" in reply:
                        Input_task(reply, order)

                    elif "remember" in reply:
                        Input_task(reply, order)

                    elif "recall" in reply:
                        Input_task(reply, order)

                    # ------------------------------------------------------------------------------------

                    #  Display control

                    elif "volume up" in reply:
                        # from controlD import volmup
                        Speak("Turning volume up...")
                        volmup()

                    elif "volume down" in reply:
                        # from controlD import volmdown
                        Speak("Turning volume down...")
                        volmdown()

                    elif "shutdown" in reply:
                        Speak("Turning system shutdown...")
                        system_down()

                    elif "restart" in reply:
                        Speak("System restart...")
                        system_restart()

                    elif "sleep" in reply:
                        Speak("Turning system in sleep mode...")
                        system_restart()

                    elif "mute" in reply:
                        mute_speaker()

                    elif "type" in reply:
                        type_action()

                    else:
                        Speak(reply)



if __name__ == "__main__":
    while True:
        main()
# while True:
#     main()











