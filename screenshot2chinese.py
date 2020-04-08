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
from ocr import ocr

r =platform.architecture()
print(r)
shot = 0

my_ocr = ocr(2)

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
            result = my_ocr.transIm(jpg)
            print(result)
            pyperclip.copy(result.strip())

keyboard.add_hotkey('win+shift+s', ScreenShot)
keyboard.add_hotkey('win+ctrl', getScreenShot)
keyboard.wait('ctrl+c')
print('exit')

