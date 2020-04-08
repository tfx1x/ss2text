from ocr_pytesseract import transIm_pytesseract


class ocr:
    def __init__(self,type):
        self.oct_type = type
            
    def transIm(self, file, lang = 'chi_sim+eng'):
        if self.oct_type == 1:
            return transIm_pytesseract(file, lang)
        elif self.oct_type == 2:
            from ocr_baidu import transIm_baidu
            return transIm_baidu(file)

