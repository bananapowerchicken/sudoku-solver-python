import pytesseract
import cv2
# import matplotlib.pyplot as plt
from PIL import Image


# 1 - installed tesseract from here
# https://github.com/UB-Mannheim/tesseract/wiki

# 2 - pip install pytesseract

# 3 - add this to PATH
# C:\Users\Anna\AppData\Local\Programs\Tesseract-OCR

# 4 - wrote this
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Anna\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# читать изображение с помощью OpenCV
# image = cv2.imread("test.jpg") # текст и цифры +
# image = cv2.imread("test2.jpg") # цифры + 
image = cv2.imread("puzzle.png")  # с моим изображением на дурака не сработало)))

# получаем строку
# string = pytesseract.image_to_string(image)  # эта функция переделывает изображения в текст
# хотя она тут в тексте распознала и цифру

string = pytesseract.image_to_string(image, lang='eng',config='-c tessedit_char_whitelist=123456789 --psm 6')

# печатаем
print(string)