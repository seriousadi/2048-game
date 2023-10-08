from random import randint

grid = [[8, 0, 9, 0],
        [0, 1, 9, 9],
        [0, 1, 9, 9],
        [8, 8, 8, 8]]


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


grid_column = 0
for n in range(len(grid)):
    grid_column = [grid[0][n], grid[1][n], grid[2][n], grid[3][n]]
    move_left(grid_column)
    grid[0][n], grid[1][n], grid[2][n], grid[3][n] = grid_column[0], grid_column[1], grid_column[2], grid_column[3]


def move_right(row):
    def move_elements(row):
        for n in range(len(row) - 1, -1, -1):
            if row[n] == 0:
                row.pop(n)
                row.insert(0, 0)
                for n in range(len(row[:n])):
                    if row[n] == 0:
                        row.pop(n)
                        row.insert(0, 0)

    move_elements(row)
    k = len(row) - 1
    while k > 1:
        p = k - 1
        if row[k] == row[p] and row[k] != 0:
            row[k] = row[p] * 2
            row[p] = 0
            move_elements(row)
        k -= 1


# for n in grid:
#    move_right(n)
#

def spawn_num():
    grid[randint(0, 3)][randint(0, 3)] = 2


def print_grid():
    for n in grid:
        print(*n)


# print_grid()

# spawn_num()
# print_grid()

game_on = False

while game_on:
    swiped = input("Where to swipe L/R/U/D : ")
    if swiped == "L":
        pass
