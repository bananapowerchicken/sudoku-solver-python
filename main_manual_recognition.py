from PIL import Image

# get the whole puzzle

# recognise the numbers

def change_background(img, background_color:tuple):
    x1,y1 = img.size # Через атрибут size получаем кортеж с двумя элементами (размер изображения по x и y)
    im = img.load()
    # Проходимся последовательно по каждому пикселю картинок
    for x in range(0,x1):
        for y in range(0,y1):
            if im[x,y] == background_color: 
                im[x,y] = (255, 255, 255, 255)
    
    return img

def compare_per_pixel(img1, img2):
    is_equal = False

    im1 = img1.load() # Загружаем первое изображение для доступа к пикселям
    im2 = img2.load() # Загружаем первое изображение для доступа к пикселям
    i = 0 # Счетчик пикселей, которые не совпадают

    if (img1.size == img2.size): # Проверяем, что размер изображений совпадают
        x1,y1 = img1.size # Через атрибут size получаем кортеж с двумя элементами (размер изображения по x и y)
        total_pixels_num = x1 * y1
        # Проходимся последовательно по каждому пикселю картинок
        for x in range(0,x1):
            for y in range(0,y1):
                if im1[x,y] != im2[x,y]: # Если пиксель первой картинки по координатах [x,y] не совпадает
                    # с пикселем второй картинки по координатах [x,y], тогда:
                    i = i + 1 # Увеличиваем счетчик на 1
                    # print(f'Координаты: x={x}, y={y} Изображение 1={im1[x,y]} - Изображение 2={im2[x,y]}')
        # print(f"Количество разных пикселей: {i}")
        # print(f"Всего пикселей: {total_pixels_num}")
         # пороговое условие пока от балды:
        # if i <= total_pixels_num * 0.2:
        if i < 2000:
            is_equal = True 
    else:
        print("Размеры изображений не совпадают!")
    # print(is_equal)
    return is_equal

# на входе одна картинка c любым фоном
# на выходе распознанное число
def recognise_num(img):
    im = img.load()
    if im[0, 0] != (255, 255, 255, 255):
        im = change_background(img, im[0, 0])
    for i in range(1, 10):
        img_template = Image.open(f'num_templates/{i}.png')
        # print(i)
        if compare_per_pixel(im, img_template):
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
            num = recognise_num(im_crop)

            if num != 0:
                grid[y][x] = num
    
    print('Numbers from the image recognised')


# tests


# test_img2 = Image.open('num_templates/1_blue.png') # + на 2000
# test_img2 = Image.open('num_templates/2_blue.png') # + на 2000
# test_img2 = Image.open('num_templates/3_blue.png') # + на 2000
# test_img2 = Image.open('num_templates/4_blue.png') # не распозналось на 1000, + на 2000
# test_img2 = Image.open('num_templates/5_blue.png') # не распозналось на 1000, + на 2000
# test_img2 = Image.open('num_templates/6_blue.png') # не распозналось на 1000, + на 2000
# test_img2 = Image.open('num_templates/7_blue.png') # не распозналось на 1000, + на 2000
# test_img2 = Image.open('num_templates/8_blue.png') # не распозналось на 1000, + на 2000
# test_img2 = Image.open('num_templates/9_blue.png') # + на 2000

for i in range(1, 10):
    test_img = Image.open(f'num_templates/{i}_blue.png')
    res = recognise_num(test_img)
    print(res)

for i in range(1, 10):
    test_img = Image.open(f'num_templates/{i}_intense_blue.png')
    res = recognise_num(test_img)
    print(res)

# res = recognise_num(test_img2)
# changed_background.save('changed_background.png', quality=95)
# print(res)