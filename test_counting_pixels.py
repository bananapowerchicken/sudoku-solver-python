# знаю цвет цифры
# открываю изображение
# закрашиваю все, что не цифра
# получаю белый + цифра
# считаю не белые - получаю кол-во пикселей в цифре

from PIL import Image

num_color = (52, 72, 97, 255)
num_pixels_amount = 0
# getting cut templates to count pixels for every num
# for i in range (10):
#     image = Image.open(f'{i}.png')
#     pixels = image.load()

#     print(pixels[110, 57])
#     for x in range(200):
#         for y in range(200):
#             if pixels[x,y] != num_color:
#                 pixels[x,y] = (255, 255, 255)
#             else:
#                 num_pixels_amount+=1

#     image.save(f'{i}_white.png', quality=95)
#     print(num_pixels_amount)

#     im_crop = image.crop((50, 40, 150, 170))
#     im_crop.save(f'{i}_cropped.png', quality=95) # для контроля

# should be constant here in this program
# key - num
# meaning - non-white pixel amount
num_pixel = {
    # 0: 0, 
    1: 1234,
    2: 3312,
    3: 5479,
    4: 7733,
    5: 10029,
    6: 12728,
    7: 14274,
    8: 17008,
    9: 19695,
}

# total_num = 0
# for i in range (10):
#     image = Image.open(f'cropped/{i}_cropped.png')
#     pixels = image.load()

#     for x in range(100):
#         for y in range(130):
#             if pixels[x,y] == num_color:
#                 num_pixels_amount+=1
#             total_num += 1

#     print(i, num_pixels_amount)

# print(total_num)

def compare_per_pixel(img1, img2, threshold):
    is_equal = False
    not_equal_pixels_num = 0
    # pixel_threshhold = 1000

    # from PIL-fromat to pixels
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
    

def recognise_num(img):
    num_pixels_amount = 0
    # pixels = img.load()

    # for x in range(100):
    #     for y in range(130):
    #         if pixels[x,y] == num_color:
    #             num_pixels_amount+=1
    
    # for i in num_pixel.keys():
    #     print(num_pixels_amount, num_pixel[i])
    #     if num_pixels_amount == 0:
    #         return 0
    #     if num_pixels_amount >= num_pixel[i]:
    #         return i + 1

    # compare with templates
    threshold = 1300 #200
    
    for i in range (0, 10):
        print(i, f'cropped/{i}_cropped.png')
        tmpl = Image.open(f'cropped/{i}_cropped.png')
        res = compare_per_pixel(img, tmpl, threshold)

        if res:
            print(i, res)
            num = i
            return num

    if res == False :
        res = compare_per_pixel(img, tmpl, threshold+100) # +300 
 
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

get_nums(grid, 'puzzle_3')
print('end')

grid_size = len(grid)

# terminal output
for i in range(0, grid_size):
    print(grid[i])
