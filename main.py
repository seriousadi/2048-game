from random import randint

grid = [[0, 2, 2, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 9],
        [6, 0, 8, 0]]


def spawn_num():
    grid[randint(0, 3)][randint(0, 3)] = 2


def print_grid():
    for n in grid:
        print(*n)


spawn_num()
print_grid()

game_on = False

while game_on:
    swiped = input("Where to swipe L/R/U/D : ")
    if swiped == "L":
        pass
