import pytesseract
import cv2
 
from PIL import Image
import numpy as np

grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

# 1 - installed tesseract from here
# https://github.com/UB-Mannheim/tesseract/wiki

# 2 - pip install pytesseract

# 3 - add this to PATH
# C:\Users\Anna\AppData\Local\Programs\Tesseract-OCR

# 4 - wrote this
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Anna\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# # разбираем больную 9
# image = cv2.imread("9.png")
# img = Image.open("9.png")
# im_crop = img.crop((0, 10, 220, 220))
# im_crop.save('cropped.png', quality=95)
# image = cv2.imread("cropped.png")
        
# string = pytesseract.image_to_string(image, config='-c tessedit_char_whitelist=123456789 --psm 6')
# print(string)


# # разбираем больную 7 - отдельно распознается
# image = cv2.imread("7.png")
# img = Image.open("7.png")
# im_crop = img.crop((0, 10, 220, 220))
# im_crop.save('cropped.png', quality=95)
# image = cv2.imread("cropped.png")
        
# string = pytesseract.image_to_string(image, config='-c tessedit_char_whitelist=123456789 --psm 6')
# print(string)


# # разбираем больную 4 - отдельно распознается
# image = cv2.imread("4.png")
# img = Image.open("4.png")
# im_crop = img.crop((0, 0, 220, 220))
# im_crop.save('cropped.png', quality=95)
# image = cv2.imread("cropped.png")
        
# string = pytesseract.image_to_string(image, config='-c tessedit_char_whitelist=123456789 --psm 6')
# print(string)

img = Image.open("puzzle.png") # size 2000 * 2000

step = 220 # ~2000//9
for y in range(0, 9):    
    for x in range(0, 9):
        x0 = x * step
        y0 = y * step
        im_crop = img.crop((x0 + 15, y0 + 15, x0 + step - 15, y0 + step - 15))
        im_crop = im_crop.crop((0, 0, 200, 200))
        im_crop.save('cropped.png', quality=95)
        image = cv2.imread("cropped.png")
        
        string = pytesseract.image_to_string(image, config='-c tessedit_char_whitelist=123456789 --psm 6')
        print(string)
        
    # if string == "17":a

        if string != "":
            # string = string[-1:]
            grid[y][x] = int(string) % 10  # топорно решаем рпоблему 17

def print_grid(grid):
    for i in range(0, 9):
        print(grid[i])

print_grid(grid)





# распознавание
# https://waksoft.susu.ru/2021/05/18/kak-s-pomoshhyu-python-raspoznat-tekst-v-izobrazheniyah/
# обрезка
# https://python-scripts.com/pillow-crop







# im_crop = img.crop((0, 0, 660, 220))
# # im_crop.show()
# im_crop.save('cropped.png', quality=95)



# # PREPROCESSING
# def preprocess(img: np.ndarray) -> np.ndarray:
#     (height, width) = img.shape[:2]
#     height, width = int(height * 3), int(width * 3)
#     img = cv2.resize(img, (width, height), interpolation=cv2.INTER_CUBIC)
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     img = cv2.medianBlur(img, 3)
#     img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#     return img

# # получаем строку
# # string = pytesseract.image_to_string(image)  # эта функция переделывает изображения в текст
# # хотя она тут в тексте распознала и цифру

# image = preprocess(image)
# image = cv2.imread("cropped.png")
# string = pytesseract.image_to_string(image, lang='eng',config='-c tessedit_char_whitelist=123456789 --psm 6')

# печатаем
# print(string)