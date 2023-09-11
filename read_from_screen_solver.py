import pyautogui as pg
import time
import os

# # пробую наведение мыши
# print(pg.position())
print(pg.size())

time.sleep(2)
print(pg.position())


# pg.mouseDown(button='right')
pg.click()  # клик ЛКМ работает
pg.rightClick() # клик ПКМ работает
pg.hotkey('down')
pg.hotkey('enter')

# теперь нужно названия файла ввести - как-то он странно вводится - теряет постепенно первые буквы
time.sleep(2)
name = 'puzzle'
pg.typewrite(name, 0.5)
pg.hotkey('enter')


# тут должно быть распознавание цифр с сохраненной картинки
# waksoft.susu.ru/2021/05/18/kak-s-pomoshhyu-python-raspoznat-tekst-v-izobrazheniyah/


# для простоты удаляю судоку после решения
time.sleep(10)
os.remove(f'{name}.png')