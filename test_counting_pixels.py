# знаю цвет цифры
# открываю изображение
# закрашиваю все, что не цифра
# получаю белый + цифра
# считаю не белые - получаю кол-во пикселей в цифре

from PIL import Image
import time
import os

from utils import get_data, solve, download_img

num_color = (52, 72, 97, 255)
num_pixels_amount = 0


def compare_per_pixel(img1, img2, threshold):
    # diff_pixel = []
    is_equal = False
    not_equal_pixels_num = 0

    pixels1 = img1.load()
    pixels2 = img2.load()

    if (img1.size == img2.size):
        x1, y1 = img1.size
        # comparing every pixel
        for x in range(0,x1):
            for y in range(0,y1):
                if pixels1[x,y] != pixels2[x,y]:
                    not_equal_pixels_num += 1
        print(not_equal_pixels_num, threshold)
        if not_equal_pixels_num <= threshold:
            is_equal = True
    else:
        print("Image sizes are not equal!")
    return is_equal
    
def diff_pixels(img1, img2):
    # from PIL-fromat to pixels
    pixels1 = img1.load()
    pixels2 = img2.load()
    not_equal_pixels_num = 0

    if (img1.size == img2.size):
        x1, y1 = img1.size
        # comparing every pixel
        for x in range(0,x1):
            for y in range(0,y1):
                if pixels1[x,y] != pixels2[x,y]:
                    not_equal_pixels_num += 1
        
    else:
        print("Image sizes are not equal!")
    
    return not_equal_pixels_num

# return num of dark pixels, making a digit
def digit_pixels(img):
    res = 0
    res1 = 0
    pixels = img.load()
    x1, y1 = img.size
        # comparing every pixel
    for x in range(0,x1):
        for y in range(0,y1):
            if pixels[x,y] != (255, 255, 255, 255):
                res+=1

    for x in range(0,x1):
        for y in range(0,y1):
            if pixels[x,y] == num_color:
                res1+=1
    # print(res, res1, res-res1)
    return res

def recognise_num(img):    

    # diffs = []
    # for i in range (0, 10):
    #     # print(i, f'cropped/{i}_cropped.png')
    #     tmpl = Image.open(f'cropped/{i}_cropped.png')

    #     diff = diff_pixels(img, tmpl)
    #     diffs.append(diff)
    
    # print(diffs)
    # print(min(diffs))
    # print(diffs.index(min(diffs)))
    # return diffs.index(min(diffs))
    diffs = []
    for i in range (0, 10):
        print(i, f'cropped/{i}_cropped.png')
        tmpl = Image.open(f'cropped/{i}_cropped.png')
        res_tmp = digit_pixels(tmpl)
        res = digit_pixels(img)
        print(res_tmp, res, abs(res_tmp - res))
        diffs.append(abs(res_tmp - res))

        # if abs(res - res_tmp) <= 0:
        #     return i
    print(diffs)
    print('min', min(diffs))
    print('min_ind', diffs.index(min(diffs)))
    return diffs.index(min(diffs))


    

def get_nums(grid: list, img_name: str):

    img = Image.open(f'{img_name}.png') # size 2000 * 2000

    # TODO: fix problem with fragile setting of sizes - it's too complex
    # maybe this will be finished with the new recognising way
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
            pixels = im_crop.load()
            for xx in range(200):
                for yy in range(200):                    
                    if pixels[xx,yy] != num_color:
                        pixels[xx,yy] = (255, 255, 255)
            im_crop.save('cropped.png', quality=95) # для контроля

            im_crop = im_crop.crop((50, 40, 150, 170)) # новая суженная пропорция
            im_crop.save('cropped.png', quality=95) # для контроля
            # pixels = im_crop.load()
            # im_crop = Image.open('cropped.png')
            num = recognise_num(im_crop)
            print(num)
            print('----------')

            if num != 0:
                grid[y][x] = num
    
    print('Numbers from the image recognised')

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

get_nums(grid, 'puzzle')
# print('end')

grid_size = len(grid)

# terminal output
# for i in range(0, grid_size):
#     print(grid[i])

curr_fold_address = 'D:\code\sudoku-solver-python'
img_name = 'puzzle'


# download_img(curr_fold_address)
# time.sleep(15)
# get_nums(grid, img_name)
# time.sleep(1)
# solve(grid)

# os.remove(f'{img_name}.png')
# os.remove('cropped.png')

# img = Image.open('cropped/8_cropped.png')
# digit_pixels(img)

# img = Image.open('cropped/3_cropped.png')
# digit_pixels(img)