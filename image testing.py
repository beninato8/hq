import pytesseract
from PIL import Image
from unidecode import unidecode

text = pytesseract.image_to_string(Image.open('test images/hq test 5.PNG'))
print(unidecode(text))
print(text.encode('utf-8'))

