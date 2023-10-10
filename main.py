import random

grid = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]


def move_left(row):
    """This shifts the nums to leat and adds the nums which are equal and are side by side
        only works for one row.
    """

    def move_elements(row2):
        """
        this one shifts elements to the respective side
        :param row2:
        :return:
        """
        for n in range(len(row2)):
            if row2[n] == 0:
                row2.pop(n)
                row2.append(0)
                for n in range(len(row2[n:])):
                    if row2[n] == 0:
                        row2.pop(n)
                        row2.append(0)

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

    def move_elements(row2):
        for n in range(len(row2) - 1, -1, -1):
            if row2[n] == 0:
                row2.pop(n)
                row2.insert(0, 0)
                for n in range(len(row2[:n+1])):
                    if row2[n] == 0:
                        row2.pop(n)
                        row2.insert(0, 0)

    move_elements(row)
    k = len(row) - 1
    while k > 0:
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
        move_left(grid_column)
        grid[0][n], grid[1][n], grid[2][n], grid[3][n] = grid_column[0], grid_column[1], grid_column[2], grid_column[3]


def move_down():
    grid_column = 0
    for n in range(len(grid)):
        grid_column = [grid[0][n], grid[1][n], grid[2][n], grid[3][n]]
        move_right(grid_column)
        grid[0][n], grid[1][n], grid[2][n], grid[3][n] = grid_column[0], grid_column[1], grid_column[2], grid_column[3]


def spawn_num():
    possible_loc = []
    for c in range(len(grid)):
        for r in range(len(grid)):
            if grid[c][r] == 0:
                possible_loc.append((c, r))

    if possible_loc:
        loc = random.choice(possible_loc)
        grid[loc[0]][loc[1]] = 2


def print_grid():
    for n in grid:
        print(*n)


game_on = True

spawn_num()
print_grid()

while game_on:
    swiped = input("Where to swipe L/R/U/D : ").lower()
    match swiped:
        case "l":
            for n in grid:
                move_left(n)
        case "r":
            for n in grid:
                move_right(n)
        case "u":
            move_up()
        case "d":
            move_down()
        case default:
            print("anything other than L/R/U/D is not allowed")
    spawn_num()
    print_grid()
