import pydirectinput
import time
import os
import pyautogui
import re
from ast import literal_eval as make_tuple
bushes = []
bushel = []

def tango():
    pyautogui.hotkey('f')
    time.sleep( .4 )
    pydirectinput.keyDown('d')
    time.sleep( 1.2 )
    pydirectinput.keyUp('d')
    pydirectinput.keyDown('w')
    time.sleep( .1 )
    pyautogui.hotkey('ctrl')
    time.sleep( .9 )
    pyautogui.hotkey('ctrl')
    time.sleep( 1.3 )
    pydirectinput.keyDown('a')
    time.sleep( .1 )
    pyautogui.hotkey('ctrl')
    time.sleep( 3.4 )
    pydirectinput.keyUp('w')
    time.sleep( .5 )
    pydirectinput.keyUp('a')
    pydirectinput.keyDown('w')
    time.sleep( .8 )
    pydirectinput.keyUp('w')
    pyautogui.hotkey('f')
    time.sleep( .4 )
    pydirectinput.keyDown('d')
    time.sleep( 1 )
    pydirectinput.keyDown('w')
    time.sleep( 1 )
    pydirectinput.keyUp('d')
    pydirectinput.keyDown('a')
    time.sleep( 1 )
    pydirectinput.keyUp('w')
    time.sleep( 2 )
    pydirectinput.keyDown('s')
    time.sleep( 1 )
    pydirectinput.keyUp('a')
    pydirectinput.keyDown('d')
    time.sleep( .5 )
    pydirectinput.keyUp('s')
    time.sleep( 1.5 )
    pydirectinput.keyUp('d')
    pydirectinput.keyDown('s')
    time.sleep( .5 )
    seek()

def seek():
    udif = ''
    ldif = ''
    pretty = []
    pretty.append(ladder)
    fly = []
    print('honing')
    print(pretty)
    f = str(pyautogui.locateOnScreen( 'C:\\Users\\18564\\Desktop\\DEW\\ladder1.png', confidence=0.7, grayscale=False))
    im = re.sub('Box\(left\=','(',f)
    im2 = re.sub('top\=','',im)
    im3 = re.sub('width\=','',im2)
    im4 = re.sub('height\=','',im3)
    im5 = make_tuple(im4)
    pretty.append(im5)
    print(pretty)
    print(pretty[1][0])
    print(pretty[1][1])
    print(pretty[0][1])
    print(pretty[0][0])
    ldif = (pretty[1][0] - pretty[0][0])/312
    udif = (pretty[1][1] - pretty[0][1])/312
    if udif >= -.1 and udif <= .1:
        if ldif >= -.1 and ldif <= .1:
            pyautogui.hotkey('f')
        if ldif >= .1:
            pydirectinput.keyDown('d')
            time.sleep(abs(ldif))
            pydirectinput.keyUp('d')
        if ldif <= -.1:
            pydirectinput.keyDown('a')
            time.sleep(abs(ldif))
            pydirectinput.keyUp('a')
    if udif <= -.1:
        if ldif >= -.1 and ldif <= .1:
            pydirectinput.keyDown('w')
            time.sleep(abs(udif))
            pydirectinput.keyUp('w')
        if ldif >= .1:
            pydirectinput.keyDown('w')
            time.sleep(abs(udif))
            pydirectinput.keyUp('w')
            pydirectinput.keyDown('d')
            time.sleep(abs(ldif))
            pydirectinput.keyUp('d')
        if ldif <= -.1:
            pydirectinput.keyDown('w')
            time.sleep(abs(udif))
            pydirectinput.keyUp('w')
            pydirectinput.keyDown('a')
            time.sleep(abs(ldif))
            pydirectinput.keyUp('a')
    if udif >= .1:
        if ldif >= -.1 and ldif <= .1:
            pydirectinput.keyDown('s')
            time.sleep(abs(udif))
            pydirectinput.keyUp('s')
        if ldif >= .1:
            pydirectinput.keyDown('s')
            time.sleep(abs(udif))
            pydirectinput.keyUp('s')
            pydirectinput.keyDown('d')
            time.sleep(abs(ldif))
            pydirectinput.keyUp('d')
        if ldif <= -.1:
            pydirectinput.keyDown('s')
            time.sleep(abs(udif))
            pydirectinput.keyUp('s')
            pydirectinput.keyDown('a')
            time.sleep(abs(ldif))
            pydirectinput.keyUp('a')
    if udif >= -.1 and udif <=  .1:
        if ldif >= -.1 and ldif <= .1:
            pyautogui.hotkey('f')
        if ldif <= -.1 or ldif >= .1:
            seek()
    if udif <= -.1 or udif >= .1:
        seek()

def hone():
    print('honing')
    f = pyautogui.locateOnScreen( 'C:\\Users\\18564\\Desktop\\DEW\\ladder1.png', confidence=0.9, grayscale=False)
    bushes.append(str(f))
    print(bushes)
    bushel = []
    im = ''
    for i in bushes:
        it = str(i)
        im = re.sub('Box\(left\=','(',it)
        im2 = re.sub('top\=','',im)
        im3 = re.sub('width\=','',im2)
        im4 = re.sub('height\=','',im3)
        bushel.append(make_tuple(im4))
    e = len(bushel) - 1
    ldif = (bushel[e][0] - bushel[0][0])/312
    udif = (bushel[e][1] - bushel[0][1])/312
    print(bushel)
    print('honing2')
    print(udif)
    print(ldif)
    if udif >= -.1 and udif <=  .1:
        if ldif >= -.1 and ldif <= .1:
            tango()
        if ldif >= .1:
            pydirectinput.keyDown('d')
            time.sleep(abs(ldif))
            pydirectinput.keyUp('d')
        if ldif <= -.1:
            pydirectinput.keyDown('a')
            time.sleep(abs(ldif))
            pydirectinput.keyUp('a')
    if udif <= -.1:
        if ldif >= -.1 and ldif <= .1:
            pydirectinput.keyDown('w')
            time.sleep(abs(udif))
            pydirectinput.keyUp('w')
        if ldif >= .1:
            pydirectinput.keyDown('w')
            time.sleep(abs(udif))
            pydirectinput.keyUp('w')
            pydirectinput.keyDown('d')
            time.sleep(abs(ldif))
            pydirectinput.keyUp('d')
        if ldif <= -.1:
            pydirectinput.keyDown('w')
            time.sleep(abs(udif))
            pydirectinput.keyUp('w')
            pydirectinput.keyDown('a')
            time.sleep(abs(ldif))
            pydirectinput.keyUp('a')
    if udif >= .1:
        if ldif >= -.1 and ldif <= .1:
            pydirectinput.keyDown('s')
            time.sleep(abs(udif))
            pydirectinput.keyUp('s')
        if ldif >= .1:
            pydirectinput.keyDown('s')
            time.sleep(abs(udif))
            pydirectinput.keyUp('s')
            pydirectinput.keyDown('d')
            time.sleep(abs(ldif))
            pydirectinput.keyUp('d')
        if ldif <= -.1:
            pydirectinput.keyDown('s')
            time.sleep(abs(udif))
            pydirectinput.keyUp('s')
            pydirectinput.keyDown('a')
            time.sleep(abs(ldif))
            pydirectinput.keyUp('a')
    if udif >= -.1 and udif <=  .1:
        if ldif >= -.1 and ldif <= .1:
            tango()
        if ldif <= -.1 or ldif >= .1:
            hone()
    if udif <= -.1 or udif >= .1:
        hone()

def waltz():
    x = pyautogui.locateOnScreen( 'C:\\Users\\18564\\Desktop\\DEW\\ladder1.png', confidence=0.9, grayscale=False)
    t = str(x)
    print(t)
    bushes.append(t)
    pydirectinput.keyDown('w')
    time.sleep( .6 )
    pydirectinput.keyDown('a')
    time.sleep( 1.5 )
    pydirectinput.keyUp('w')
    time.sleep( 1.4 )
    pydirectinput.keyDown('s')
    time.sleep( .7 )
    pydirectinput.keyUp('a')
    pydirectinput.keyDown('s')
    pydirectinput.keyDown('d')
    time.sleep( .7 )
    pydirectinput.keyUp('d')
    time.sleep( 1.1 )
    pydirectinput.keyUp('s')
    pydirectinput.keyDown('d')
    time.sleep( 1.6 )
    pydirectinput.keyDown('w')
    time.sleep( .8 )
    pydirectinput.keyUp('w')
    time.sleep( .4 )
    pydirectinput.keyUp('w')
    pydirectinput.keyUp('a')
    pydirectinput.keyUp('s')
    pydirectinput.keyUp('d')
    print('ee')
    x = pyautogui.locateOnScreen( 'C:\\Users\\18564\\Desktop\\DEW\\ladder1.png', confidence=0.9, grayscale=False)
    t = str(x)
    bushes.append(t)
    hone()

if __name__ == "__main__": 
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
