from random import randint

grid = [[8, 2, 2, 0],
        [0, 1, 1, 0],
        [3, 3, 3, 9],
        [8, 0, 8, 0]]


def move_left(row):
    def move_elements(row):
        for n in range(len(row)):
            if row[n] == 0:
                row.pop(n)
                row.append(0)
                for n in range(len(row[n:])):
                    if row[n] == 0:
                        row.pop(n)
                        row.append(0)

    move_elements(row)
    k = 0
    while k < len(row) - 1:
        p = k + 1
        if row[k] == row[p] and row[k] != 0:
            row[k] = row[p] * 2
            row[p] = 0
            move_elements(row)
        k += 1


def move_right(row):
    def move_elements(row):
        for n in range(len(row)-1, -1, -1):
            if row[n] == 0:
                row.pop(n)
                row.insert(0,0)
                for n in range(len(row[:n])):
                    if row[n] == 0:
                        row.pop(n)
                        row.insert(0,0)

    move_elements(row)
    k = len(row)-1
    while k > 1:
        p = k - 1
        if row[k] == row[p] and row[k] != 0:
            row[k] = row[p] * 2
            row[p] = 0
            move_elements(row)
        k -= 1


for n in grid:
   move_right(n)
def spawn_num():
    grid[randint(0, 3)][randint(0, 3)] = 2


def print_grid():
    for n in grid:
        print(*n)


# spawn_num()
# print_grid()

game_on = False

while game_on:
    swiped = input("Where to swipe L/R/U/D : ")
    if swiped == "L":
        pass
