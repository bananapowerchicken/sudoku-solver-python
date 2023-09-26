import pyautogui as pg
import time
import pytesseract
import cv2
from PIL import Image


def download_img(current_folder_addr: str):
    time.sleep(2)
    pg.click()
    pg.rightClick()
    pg.hotkey('down')
    pg.hotkey('enter')
    
    time.sleep(5)
    img_name = 'puzzle'
    pg.typewrite(img_name, 0.05)


    with pg.hold('ctrl'):
        pg.press('l')
    pg.typewrite(current_folder_addr, 0.05)
    pg.hotkey('enter')

    time.sleep(1)
    pg.hotkey('enter')

    print('Image downloaded')

# TODO independent way to recognise - comparison with reference
# recognise numbers from the downloaded img
def get_data(grid):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Anna\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

    # TODO get rid of the hardcoded img name
    img = Image.open("puzzle.png") # size 2000 * 2000

    step = 220 # TODO put away the hardcode 2000/9
    side_crop = 15
    grid_size = len(grid)
    for y in range(0, grid_size):    
        for x in range(0, grid_size):
            x0 = x * step
            y0 = y * step
            im_crop = img.crop((x0 + side_crop, y0 + side_crop, x0 + step - side_crop, y0 + step - side_crop))
            im_crop = im_crop.crop((0, 0, 200, 200))
            im_crop.save('cropped.png', quality=95)
            image = cv2.imread("cropped.png")
            
            string = pytesseract.image_to_string(image, config='-c tessedit_char_whitelist=123456789 --psm 6')
            print(string)

            if string != "":
                grid[y][x] = int(string)
    
    print('Numbers from the image recognised')

# check if n-num is possible for the current cell
def is_possible(grid, x, y, n) -> bool:   
    grid_size = len(grid)
    block_size = grid_size / 3
    for row in range(0, grid_size):
        if grid[row][y] == n:
            return False
    

    for col in range(0, grid_size):
        if grid[x][col] == n:
            return False

    x_block_start = (x // block_size)*block_size
    y_block_start = (y // block_size)*block_size
    for X in range(x_block_start, x_block_start+block_size):
        for Y in range(y_block_start, y_block_start+block_size):
            if grid[X][Y] == n:
                return False
            
    return True

def print_grid(grid):

    grid_size = len(grid)

    # terminal output
    for i in range(0, grid_size):
        print(grid[i])

    # input in the site sudoku.com
    final = []
    str_final = []
    for i in range(grid_size):
        final.append(grid[i])

    for lists in final:
        for num in lists:
            str_final.append(str(num))
    
    counter = []

    for num in str_final:
        pg.press(num)
        pg.hotkey('right')
        counter.append(num)
        if len(counter)%grid_size== 0:
            pg.hotkey('down')
            for i in range(grid_size - 1):
                pg.hotkey('left')

# solving sudoku algo
def solve(grid):
    grid_size = len(grid)
    for x in range(0, grid_size):
        for y in range(0, grid_size):
            if grid[x][y] == 0:
                for n in range(1, grid_size+1):
                    if is_possible(grid, x, y, n):
                        grid[x][y] = n                        
                        solve(grid)
                        grid[x][y] = 0
                return

    print_grid(grid)
    print('\n')

    print('Sudoku solved')

