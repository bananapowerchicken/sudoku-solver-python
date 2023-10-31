from PIL import Image
from utils import change_background, compare_per_pixel

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


# на входе одна картинка c любым фоном
# на выходе распознанное числоgit
def recognise_num(img):
    threshhold_dict = {
        0: 1800,
        1: 1000,
        2: 1800,
        3: 1800,
        4: 1800,
        5: 1800,
        6: 1800,
        7: 1800,
        8: 1800,
        9: 1800,}
    im = img.load()    
    if im[0, 0] != (255, 255, 255, 255):
        im = change_background(img, im[0, 0])
    else:
        im = img
    for i in range(0, 10):
        img_template = Image.open(f'num_templates/{i}.png')
        pixel_threshhold = threshhold_dict[i]
        # print(pixel_threshhold)
        res = compare_per_pixel(im, img_template, pixel_threshhold)
        
        
        if res:
            # print(i, res)
            num = i
            return num


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
            im_crop.save('cropped.png', quality=95) # для контроля
            im_crop = Image.open('cropped.png')
            num = recognise_num(im_crop)

            if num != 0:
                grid[y][x] = num
    
    print('Numbers from the image recognised')


# # # tests


for i in range(0, 10):
    test_img = Image.open(f'num_templates/{i}_blue.png')
    res = recognise_num(test_img)
    print(res)

# for i in range(0, 10):
#     test_img = Image.open(f'num_templates/{i}_intense_blue.png')
#     res = recognise_num(test_img)
#     print(res)



# get_nums(grid, 'puzzle')
print('end')