import time
import os
from utils import get_data, solve, download_img


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
# print(len(grid))
# Here type your folder addressgit 
curr_fold_address = 'D:\code\sudoku-solver-python'
img_name = 'puzzle'


# # with pytesseractt
# download_img(curr_fold_address)
# time.sleep(10)
# get_data(grid, img_name)
# time.sleep(1)
# solve(grid)

# os.remove(f'{img_name}.png')
# os.remove('cropped.png')

# without the pytesseract
download_img(curr_fold_address)
time.sleep(10)
