import pytesseract
from PIL import Image, ImageGrab

def transIm_pytesseract(file, lang = 'chi_sim+eng'):
    result = pytesseract.image_to_string(Image.open(file), lang)
    return result