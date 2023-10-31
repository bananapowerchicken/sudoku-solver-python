from PIL import Image
from utils import change_background

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

def compare_per_pixel(img1, img2):
    is_equal = False
    not_equal_pixels_num = 0
    pixel_threshhold = 2000

    # from PIL-fromat to pixels
    im1 = img1.load()
    im2 = img2.load()

    if (img1.size == img2.size):
        x1, y1 = img1.size
        # comparing every pixel
        for x in range(0,x1):
            for y in range(0,y1):
                if im1[x,y] != im2[x,y]:
                    not_equal_pixels_num += 1
        if not_equal_pixels_num < pixel_threshhold:
            is_equal = True 
    else:
        print("Image sizes are not equal!")
    return is_equal

# на входе одна картинка c любым фоном
# на выходе распознанное число
def recognise_num(img):
    im = img.load()
    if im[0, 0] != (255, 255, 255, 255):
        im = change_background(img, im[0, 0])
    else:
        im = img
    for i in range(0, 10):
        img_template = Image.open(f'num_templates/{i}.png')
        res = compare_per_pixel(im, img_template)
        
        if res:
            print(i, res)
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


# for i in range(1, 10):
#     test_img = Image.open(f'num_templates/{i}_blue.png')
#     res = recognise_num(test_img)
#     print(res)

# # for i in range(1, 10):
# #     test_img = Image.open(f'num_templates/{i}_intense_blue.png')
# #     res = recognise_num(test_img)
# #     print(res)



get_nums(grid, 'puzzle')
print('end')