import sys
import threading
import tkinter
import tkinter as tk
import jarvis
from tkinter import PhotoImage
from PIL import Image, ImageTk
screen_main = tkinter.Tk()
screen_main.title('JARVIS')
screen_main.configure(background='black')
screen_main.geometry("1000x700")


# screen_main.attributes(, True)

class Redirect():
    def __init__(self, text_widget, autoscroll = True):
        self.text_widget = text_widget
        self.autoscroll = autoscroll

    def write(self, strr):
        self.text_widget.insert(tk.END, strr)
        if self.autoscroll:
            self.text_widget.see("end")

def jarvis_run():
    # while True:
    jarvis.main()


def run():
    threading.Thread(target=jarvis_run).start()

    def flush(self):
        pass


def close_1():
    sys.exit()


def guide_task():
    print("")
    print('Hey! There I am Jarvis ')
    print("I can help you with variety of tasks ")


def guid_run():
    threading.Thread(target=guide_task).start()


terminal = tkinter.Text(screen_main)
terminal.configure(background='black', foreground='white')
terminal.configure(width=50, height=20)
terminal.configure(font=('arial', 10))
terminal.place(x=5, y=100)
terminal.pack(side='left', fill='both')

# guid_run()
old_stdout = sys.stdout
sys.stdout = Redirect(terminal)

image = PhotoImage(file= "jarvis_logo_intro_dribbble_2.png")
label = tkinter.Label(screen_main, image=image)
label.config(width=500,height=500, background='black')
label.pack(side="top", anchor="ne")
label.image = image 
label.configure(image=image)

# button_1 = tk.Tk()
# button_1.geometry("400x300")
frame = tk.Frame(screen_main)
button = tk.Button(screen_main,font=('space age', 25),
                             foreground='cyan', 
                             background='black', 
                             text='Close', 
                             command=close_1)


button2 = tk.Button(screen_main,font=('space age', 25),
                             foreground='cyan', 
                             background='black', 
                             text='Start',
                              command=run)

button.place(x=10, y=10)
button2.place(x=10, y=10)
button.pack(side="bottom", padx=20, pady=10)
button2.pack(side="bottom", padx=20, pady=10)
# initiate_btn = tkinter.Button(screen_main, font=('space age', 25), foreground='cyan', background='black', text='Start',command=None)
# frame.place(x=10, y=10)
# frame.pack()
# initiate_btn.place(x=1000, y=100)

screen_main.mainloop()
sys.stdout = old_stdout


