import PyQt5
import sys
import pydirectinput
import time
import os
import pyautogui
import re
from ast import literal_eval as make_tuple
#Check path to bot folder to run UI
from PyQt5.Qt import *
sys.path.insert(1, 'C:\\Users\\18564\\Desktop')
import Harpies
from Harpies import *

def window():
    app = QApplication(sys.argv)
    widget = QWidget()

    b1 = QPushButton(widget)
    b1.setText("Forbidden Island")
    b1.move(64,32)
    b1.clicked.connect(b1_pressed)

    b2 = QPushButton(widget)
    b2.setText("Harpy Den")
    b2.move(64,64)
    b2.clicked.connect(b2_pressed)

    b3 = QPushButton(widget)
    b3.setText("D.S. 125")
    b3.move(64,96)
    b3.clicked.connect(b3_pressed)

    widget.setGeometry(50,50,320,200)
    widget.setWindowTitle("MMO Bot UI")
    widget.show()
    sys.exit(app.exec_())


def b1_pressed():
    print("Cycle")

def b2_pressed():
    pyautogui.hotkey('alt', 'tab')
    time.sleep( .5 )
    ladde = '(8, 440)'
    ladder = make_tuple(ladde)
    bushes = []
    bushel = []
    im = ''
    waltz()
    pydirectinput.keyUp('w')
    pydirectinput.keyUp('a')
    pydirectinput.keyUp('s')
    pydirectinput.keyUp('d')
    pydirectinput.keyUp('f')


def b3_pressed():
    print("Cycle")

if __name__ == '__main__':
   window()
