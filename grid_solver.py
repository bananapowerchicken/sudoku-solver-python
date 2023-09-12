import pyautogui as pg
import time
# fixed grid to solve in unpretty interface

# алгоритм: в ближайшую пустую ячейку подставляешь первое (по возрастанию)
# возможное значение. Затем рекурсивно решаешь дальше, то есть с обновленной
# сеткой переходишь к следующей пустой ячейке, там то же самое. Если в 
# очередной ячейке нет подходящих чисел в заданном диапазоне - значит ранее 
# закралась ошибка. Тогда эту ячейку с ошибкой оставляем равной 0, а сами 
# засчет рекурсии и return отступаем назад, к предыд обработанной ячейке.
# В ней все сохраняется на этапе последнего подставленного значения, а мы, 
# вернувшись, подставлем следующее (например, было 2, а следующее - 7)
# и снова шагаем дальше. Так идем, находим ошибку, возвращаемся к ней и правим
# рекурсивно, пока не останется ошибок.


# easy
# grid = [
#     [0, 7, 0, 5, 3, 0, 9, 0, 0],
#     [3, 4, 0, 6, 0, 2, 8, 5, 1],
#     [2, 0, 0, 0, 8, 0, 4, 7, 0],
#     [0, 0, 0, 3, 9, 0, 5, 0, 0],
#     [9, 1, 5, 7, 0, 0, 3, 0, 2],
#     [6, 0, 0, 0, 0, 0, 0, 0, 7],
#     [1, 0, 0, 9, 0, 7, 0, 8, 5],
#     [5, 9, 0, 2, 1, 6, 0, 0, 0],
#     [0, 6, 4, 0, 0, 0, 0, 0, 0],
# ]

# expert
grid = [
[0, 5, 3, 2, 0, 8, 0, 0, 6],
[0, 6, 0, 0, 0, 0, 0, 4, 0],
[0, 0, 0, 0, 0, 7, 0, 0, 0],
[8, 0, 0, 5, 0, 2, 0, 9, 0],
[0, 0, 5, 0, 4, 0, 0, 0, 0],
[0, 0, 0, 0, 7, 0, 0, 0, 2],
[9, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 5, 0, 0, 0, 0],
[0, 0, 8, 3, 0, 6, 0, 0, 4]
]


# возможно ли число на входе в данной пустой клетке9
# на входе координаты в матрице и само число
def is_possible(x, y, n) -> bool:

    # проверка смежной строки    
    for row in range(0, 9):
        if grid[row][y] == n:
            return False
    
    # проверка каждого ряда
    for col in range(0, 9):
        if grid[x][col] == n:
            return False
        
    # в range последнее указанное число не включительно
    # проверка каждого квадратного блока
    x_block_start = (x // 3)*3
    y_block_start = (y // 3)*3
    for X in range(x_block_start, x_block_start+3):
        for Y in range(y_block_start, y_block_start+3):
            if grid[X][Y] == n:
                return False
            
    return True

# сюда же заносим и печать на сайте
def print_grid(grid):
    # локальный вывод
    for i in range(0, 9):
        print(grid[i])

    # вывод на сайте
    final = []
    str_final = []
    for i in range(9):
        final.append(grid[i])

    for lists in final:
        for num in lists:
            str_final.append(str(num))
    
    counter = []

    for num in str_final:
        pg.press(num)
        pg.hotkey('right')
        counter.append(num)
        if len(counter)%9 == 0:
            pg.hotkey('down')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')



# это точно рекурсивная функция
# перерешивает судоку до победного
def solve():
    global grid  # чтобы все изменения сохранялись глобально, а не только внутри ф-ии
    for x in range(0, 9):
        for y in range(0, 9):
            if grid[x][y] == 0:
                for n in range(1, 10):
                    if is_possible(x, y, n):
                        grid[x][y] = n

                        # print_grid(grid)
                        # print('\n')
                        
                        solve()
                        grid[x][y] = 0
                return
    # time.sleep(2)
    print_grid(grid)
    print('\n')
# # тест на клетки
# for i in range(1, 10):
#     print(i, is_possible(0, 0, i))

# тест решателя
solve()
