import pytesseract
import cv2
# import matplotlib.pyplot as plt
from PIL import Image

# C:\Users\Anna\AppData\Local\Programs\Tesseract-OCR
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Anna\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# читать изображение с помощью OpenCV
image = cv2.imread("test.jpg")
# получаем строку
string = pytesseract.image_to_string(image)
# печатаем
print(string)