# import numpy as np
from PIL import Image

# intense_blue = (187, 222, 251, 255)
# blue = (226, 235, 243, 255)
# adjacent_blue = (195, 215, 234, 255)
# white(main) = (255, 255, 255, 255)

img1 = Image.open('num_templates/1.png') # Открываем первое изображение
img2 = Image.open('num_templates/adjacent.png') # Открываем первое изображение
# im1 = img1.load() # Загружаем первое изображение для доступа к пикселям
# im2 = img2.load() # Загружаем первое изображение для доступа к пикселям

if (img1.size == img2.size): # Проверяем, что размер изображений совпадают
    x1, y1 = img1.size # ширина и высота по сути
total_pixels_num = x1 * y1


def comparison_per_pixel(img1, img2):
    im1 = img1.load() # Загружаем первое изображение для доступа к пикселям
    im2 = img2.load() # Загружаем первое изображение для доступа к пикселям
    i = 0 # Счетчик пикселей, которые не совпадают

    if (img1.size == img2.size): # Проверяем, что размер изображений совпадают
        x1,y1 = img1.size # Через атрибут size получаем кортеж с двумя элементами (размер изображения по x и y)

        # Проходимся последовательно по каждому пикселю картинок
        for x in range(0,x1):
            for y in range(0,y1):
                if im1[x,y] != im2[x,y]: # Если пиксель первой картинки по координатах [x,y] не совпадает
                    # с пикселем второй картинки по координатах [x,y], тогда:
                    i = i + 1 # Увеличиваем счетчик на 1
                    print(f'Координаты: x={x}, y={y} Изображение 1={im1[x,y]} - Изображение 2={im2[x,y]}')
        print(f"Количество разных пикселей: {i}")
        print(f"Всего пикселей: {total_pixels_num}")
    else:
        print("Размеры изображений не совпадают!")

def change_pixels(img, pixel_orig: tuple, pixel_final: tuple):
    im = img.load()
    x1, y1 = img.size
    for x in range(0, x1):
            for y in range(0, y1):
                if im[x,y] == pixel_orig: # Если пиксель первой картинки по координатах [x,y] не совпадает
                    im[x, y] = pixel_final
    img.save('changed.png', quality=95)

comparison_per_pixel(img1, img2)
# change_pixels(img2, (226, 235, 243, 255), (255, 255, 255, 255))
