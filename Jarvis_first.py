from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType

from Jarvis_UI import *  # Jarvis UI
import sys
import jarvis  # Jarvis Main file
import os
from time import sleep
import threading


class MainThread(QThread):

    def __int__(self):
        super(MainThread, self).__init__()

    def run(self):
        # Ui_MainWindow()
        jarvis.main()


startFunctions = MainThread()


class Gui_Start(QMainWindow):
    def __int__(self):
        super().__int__()

        # MainWindow = QtWidgets.QMainWindow()

        self.jarvis_ui = Ui_MainWindow()

        self.jarvis_ui.setupUi(self)
        # MainWindow.show()

        self.jarvis_ui.pushButton.clicked.connect(self.startFunc)
        self.jarvis_ui.pushButton_2.clicked.connect(self.close)

    def startFunc(self):
        self.jarvis_ui.movie = QtGui.QMovie("C:/Users/kunal/Downloads/G.U.I Material/VoiceReg/Siri.gif")  # C:/Users/kunal/Downloads/G.U.I Material/VoiceReg/Siri.gif

        self.jarvis_ui.Gif_1.setMovie(self.jarvis_ui.movie)

        self.jarvis_ui.movie.start()

        self.jarvis_ui.movie_1 = QtGui.QMovie("C:/Users/kunal/Downloads/G.U.I Material/B.G/Iron_Template_1.gif")  # C:/Users/kunal/Downloads/G.U.I Material/B.G/Iron_Template_1.gif

        self.jarvis_ui.Gif_2.setMovie(self.jarvis_ui.movie_1)

        self.jarvis_ui.movie_1.start()

        # MainThread.start()
        startFunctions.start()


# QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
Gui_App = QApplication(sys.argv)

Gui_Jarvis = Gui_Start()

Gui_Jarvis.show()

exit(Gui_App.exec_())
