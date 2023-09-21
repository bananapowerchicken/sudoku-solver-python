import pyautogui as pg
import time
import pytesseract
import cv2
from PIL import Image

# grid = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
# ]

# ввести адрес нужной папки и сохранить туда картинку
def download_img_to_certain_folder(adress):
    time.sleep(2)
    pg.click()
    pg.rightClick()
    pg.hotkey('down')
    pg.hotkey('enter')
    
    time.sleep(5)
    img_name = 'puzzle'
    pg.typewrite(img_name, 0.25)


    with pg.hold('ctrl'):
        pg.press('l')
    pg.typewrite(adress, 0.05)
    pg.hotkey('enter')

    time.sleep(1)
    pg.hotkey('enter')
    # pg.typewrite(img_name, 0.25)
    # pg.hotkey('enter')
    # print('Image downloaded')

# нажать ЛКМ на 1-ую ячейку судоку в браузере
def download_img():
    time.sleep(2)
    pg.click()
    pg.rightClick()
    pg.hotkey('down')
    pg.hotkey('enter')
    
    time.sleep(5)
    img_name = 'puzzle'
    pg.typewrite(img_name, 0.25)
    pg.hotkey('enter')
    print('Image downloaded')

def get_data(grid):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Anna\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

    # global grid
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

            if string != "":
                grid[y][x] = int(string)

def is_possible(grid, x, y, n) -> bool:   
    for row in range(0, 9):
        if grid[row][y] == n:
            return False
    

    for col in range(0, 9):
        if grid[x][col] == n:
            return False

    x_block_start = (x // 3)*3
    y_block_start = (y // 3)*3
    for X in range(x_block_start, x_block_start+3):
        for Y in range(y_block_start, y_block_start+3):
            if grid[X][Y] == n:
                return False
            
    return True

def print_grid(grid):
    # локальный вывод
    for i in range(0, 9):
        print(grid[i])

    # вывод на сайте
    final = []
    str_final = []
    for i in range(9):
        final.append(grid[i])

    for lists in final:
        for num in lists:
            str_final.append(str(num))
    
    counter = []

    for num in str_final:
        pg.press(num)
        pg.hotkey('right')
        counter.append(num)
        if len(counter)%9 == 0:
            pg.hotkey('down')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')

def solve(grid):
    # global grid  # чтобы все изменения сохранялись глобально, а не только внутри ф-ии
    for x in range(0, 9):
        for y in range(0, 9):
            if grid[x][y] == 0:
                for n in range(1, 10):
                    if is_possible(grid, x, y, n):
                        grid[x][y] = n                        
                        solve(grid)
                        grid[x][y] = 0
                return

    print_grid(grid)
    print('\n')

