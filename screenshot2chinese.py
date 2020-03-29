#from graphics import *
#import pyHook
#import pythoncom
import keyboard
from PIL import Image, ImageGrab 
import platform
import os
from tempfile import TemporaryDirectory
import pytesseract
import pyperclip

r =platform.architecture()
print(r)
shot = 0

def transIm(file):
    result = pytesseract.image_to_string(Image.open(file), lang = 'chi_sim+eng')
    print(result)
    pyperclip.copy(result.strip())

def ScreenShot():
    print("input win+ctrl after screenshot")
    global shot
    shot = 1

def getScreenShot():
    global shot
    if(shot == 0):
        return
    shot = 0
    im = ImageGrab.grabclipboard()
    if isinstance(im, Image.Image):
        print("get image")
        with TemporaryDirectory() as dirname:
            print('dirname is:',dirname)
            jpg = dirname+'\\temp.jpg'
            im.save(jpg)
            transIm(jpg)
            #im.show()

keyboard.add_hotkey('win+shift+s', ScreenShot)
keyboard.add_hotkey('win+ctrl', getScreenShot)
keyboard.wait('ctrl+c')
print('exit')

