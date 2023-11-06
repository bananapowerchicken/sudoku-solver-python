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

def recognise_num(pixels):
    num_pixels_amount = 0
    # pixels = img.load()

    for x in range(100):
        for y in range(130):
            if pixels[x,y] == num_color:
                num_pixels_amount+=1
    
    for i in num_pixel.keys():
        print(num_pixels_amount, num_pixel[i])
        if num_pixels_amount == 0:
            return 0
        if num_pixels_amount >= num_pixel[i]:
            return i + 1


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
            pixels = im_crop.load()
            # im_crop = Image.open('cropped.png')
            num = recognise_num(pixels)
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
print('end')