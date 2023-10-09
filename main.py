from random import randint

grid = [[3, 3, 3, 3],
        [3, 3, 9, 9],
        [3, 1, 9, 9],
        [3, 3, 9, 8]]


def move_left(row):
    """This shifts the nums to leat and adds the nums which are equal and are side by side
        only works for one row.
    """

    def move_elements(row):
        """
        this one shifts elements to the respective side
        :param row:
        :return:
        """
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
    while k < len(row) - 1:  # adding the numbers which are equal and are right next to each other.
        p = k + 1
        if row[k] == row[p] and row[k] != 0:
            row[k] = row[p] * 2
            row[p] = 0
            move_elements(row)
        k += 1


def move_right(row):
    """This shifts the nums to right and adds the nums which are equal and are side by side.
        only works for one row.
    """

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


def move_up():
    grid_column = 0
    for n in range(len(grid)):
        grid_column = [grid[0][n], grid[1][n], grid[2][n], grid[3][n]]
        print(f"{grid_column} :grid_column")
        move_left(grid_column)
        grid[0][n], grid[1][n], grid[2][n], grid[3][n] = grid_column[0], grid_column[1], grid_column[2], grid_column[3]


def move_down():
    grid_column = 0
    for n in range(len(grid)):
        grid_column = [grid[0][n], grid[1][n], grid[2][n], grid[3][n]]
        move_right(grid_column)
        grid[0][n], grid[1][n], grid[2][n], grid[3][n] = grid_column[0], grid_column[1], grid_column[2], grid_column[3]



for n in grid:
    print(n)


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
