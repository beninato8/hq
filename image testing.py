import pytesseract
from PIL import Image
from unidecode import unidecode

text = pytesseract.image_to_string(Image.open('test images/hq test 5.PNG'))
print(unidecode(text))
print(text.encode('utf-8'))
<<<<<<< HEAD
=======

>>>>>>> 94a7141003b1cb665a47145682beb2523b63fe13
