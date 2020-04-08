ss2text
=======

Usage:
------
It can get the Chinese and english text in your screenshot and copy it to clipboard.   
This tool only supports windows now.  
It use tesseract by default and also support use ocr function in baidu cloud.
If you want to use baidu cloud, you need a baidu cloud account. And add your key in ocr_baidu.py

Running screenshot2chinese.py  
Then you can use hotkey 'win+shift+s' to screenshot.  
After you select the content,Type 'win+ctrl'   
The result will be stored in your clipboard.  
If you want to exit, type'ctrl+c'  

Install:
-------
Install tesseract-ocr, please ref https://tesseract-ocr.github.io/tessdoc/Home.html
pip install keyboard
pip install pillow
pip install pytesseract
pip install pyperclip

If you want to use baidu ocr:
pip install baidu-aip
