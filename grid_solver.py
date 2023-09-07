# fixed grid to solve in unpretty interface

grid = [
    [0, 7, 0, 5, 3, 0, 9, 0, 0],
    [3, 4, 0, 6, 0, 2, 8, 5, 1],
    [2, 0, 0, 0, 8, 0, 4, 7, 0],
    [0, 0, 0, 3, 9, 0, 5, 0, 0],
    [9, 1, 5, 7, 0, 0, 3, 0, 2],
    [6, 0, 0, 0, 0, 0, 0, 0, 7],
    [1, 0, 0, 9, 0, 7, 0, 8, 5],
    [5, 9, 0, 2, 1, 6, 0, 0, 0],
    [0, 6, 4, 0, 0, 0, 0, 0, 0],
]



# всего 2 ф-ии: 1 - возможно ли число в этой клетке
#               2 - решатель с исп ф-ии 1

# возможно ли число на входе в данной пустой клетке
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
    y_block_start = (x // 3)*3
    for X in range(x_block_start, x_block_start+3):
        for Y in range(y_block_start, y_block_start+3):
            if grid[X][Y] == n:
                return False
            
    return True


def solve():
    pass

for i in range(1, 10):
    print(i, is_possible(0, 0, i))