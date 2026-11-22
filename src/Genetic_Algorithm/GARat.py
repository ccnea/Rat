# This program's purpose is to use a genetic algorithm to help a rat find
# its way through a map to get the block of cheese.



import numpy as np

def create_grid_10x10():
    rows, cols = 10, 10

    grid = [[0 for _ in range(cols)] for _ in range(rows)]

    coords = []

    for r in range(1, 3):
        for c in range(1, 3):
            coords.append((r, c))

    for r in range(5, 7):
        for c in range(4, 8):
            coords.append((r, c))

    for r in range(3, 5):
        for c in range(6, 8):
            coords.append((r, c))

    for r in range(7, 10):
        for c in range(1, 3):
            coords.append((r, c))

    for r, c in coords:
        grid[r][c] = 1

    grid[0][0] = 'S'
    grid[9][9] = 'G'

    return grid

def create_grid_5x5():
    rows, cols = 5, 5

    grid = [[0 for _ in range(cols)] for _ in range(rows)]

    coords = []



    for r in range(1, 3):
        for c in range(1, 3):
            coords.append((r, c))

    for r, c in coords:
        grid[r][c] = 1

    grid[0][0] = 'S'
    grid[4][4] = 'G'

    return grid

def create_grid_50x50():
    rows, cols = 50, 50

    grid = [[0 for _ in range(cols)] for _ in range(rows)]

    coords = []

    for r in range(3, 12):
        for c in range(5, 9):
            coords.append((r, c))

    for r in range(2, 8):
        for c in range(17, 25):
            coords.append((r, c))

    for r in range(10, 18):
        for c in range(35, 42):
            coords.append((r, c))

    for r in range(18, 27):
        for c in range(3, 10):
            coords.append((r, c))

    for r in range(20, 29):
        for c in range(19, 27):
            coords.append((r, c))

    for r in range(25, 34):
        for c in range(38, 45):
            coords.append((r, c))

    for r in range(35, 43):
        for c in range(10, 17):
            coords.append((r, c))

    for r in range(38, 46):
        for c in range(25, 33):
            coords.append((r, c))

    for r in range(13, 17):
        for c in range(14, 18):
            coords.append((r, c))

    for r in range(32, 36):
        for c in range(5, 9):
            coords.append((r, c))

    for r, c in coords:
        grid[r][c] = 1

    grid[0][0] = 'S'
    grid[49][49] = 'G'

    return grid

def print_grid(grid):
    for row in grid:
        print(*(str(cell) for cell in row))

def valid_moves(current_pos, grid):
    rows = len(grid)
    cols = len(grid[0])
    r, c = current_pos

    directions = [
        (-1, 0, 'UP'),
        (1, 0, 'DOWN'),
        (0, -1, 'LEFT'),
        (0, 1, 'RIGHT'),
        (-1, -1, 'UP_LEFT'),
        (-1, 1, 'UP_RIGHT'),
        (1, -1, 'DOWN_LEFT'),
        (1, 1, 'DOWN_RIGHT')
    ]

    possible_moves = []

    for r_change, c_change, move_name in directions:
        new_r, new_c = r + r_change, c + c_change

        if 0 <= new_r < rows and 0 <= new_c < cols:
            if grid[new_r][new_c] != 1:
                possible_moves.append((new_r, new_c))

    return possible_moves


def traverse_grid():
    pass

if __name__ == "__main__":
    grid = create_grid_5x5()
    print_grid(grid)

    print('\n\n')

    grid = create_grid_10x10()
    print_grid(grid)

    print('\n\n')

    grid = create_grid_50x50()
    print_grid(grid)