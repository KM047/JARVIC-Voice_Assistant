from pynput.keyboard import Key, Controller
from time import sleep
import os
import pyautogui
from Test import test_net


con = Controller()


def volmup():
    for i in range(5):
        con.press(Key.media_volume_up)
        con.release(Key.media_volume_up)
        sleep(0.1)


def volmdown():
    for i in range(5):
        con.press(Key.media_volume_down)
        con.release(Key.media_volume_down)
        # con.release(Key.)
        sleep(0.1)

def mute_speaker():
    con.press(Key.media_volume_mute)
    con.release(Key.media_volume_mute)
    sleep(0.1)

def system_down():
    os.system("shutdown /s /t 5")

def system_restart():
    os.system("shutdown /r /t 5")

def system_sleep():
    pyautogui.hotkey("alt", "f4")
    sleep(1)
    pyautogui.press("left")
    sleep(1)
    pyautogui.press("enter")

def type_action():
    print("Say what you want to write")
    type_msg = str(test_net())
    msg = type_msg.replace("type", "").replace("jarvis", "").replace("notepad", "")
    pyautogui.write(f"{msg}")

