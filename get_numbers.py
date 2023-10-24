import time
from utils import download_img
from PIL import Image

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

def save_numbers(grid: list, img_name: str):
    
    # TODO get rid of the hardcoded img name
    img = Image.open(f'{img_name}.png') # size 2000 * 2000

    # TODO: fix problem with fragile setting of sizes - it's too complex
    # maybe this will be finished with the new recognising way
    step = 220 # TODO put away the hardcode 2000/9
    side_crop = 15
    num_index = 0
    grid_size = len(grid)
    for y in range(0, grid_size):    
        for x in range(0, grid_size):
            x0 = x * step
            y0 = y * step
            im_crop = img.crop((x0 + side_crop, y0 + side_crop, x0 + step - side_crop, y0 + step - side_crop))
            im_crop = im_crop.crop((0, 0, 200, 200))
            im_crop.save(f'{num_index}.png', quality=95)
            num_index+=1
    
    print('Numbers from the image saved')


# print(len(grid))
# Here type your folder addressgit 
curr_fold_address = 'D:\code\sudoku-solver-python'
img_name = 'puzzle'

download_img(curr_fold_address)
time.sleep(20)
save_numbers(grid, img_name)
