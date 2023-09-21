# сохранение картинки
# считывание
# решение
import time
import os
from utils import download_img, get_data, solve, download_img_to_certain_folder


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

# download_img()
# time.sleep(10)
# get_data(grid)
# time.sleep(1)
# solve(grid)

# os.remove('puzzle.png')

# D:\code\sudoku-solver-python - путь нужной мне папки
adress = 'D:\code\sudoku-solver-python'
download_img_to_certain_folder(adress)