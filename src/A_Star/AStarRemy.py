import numpy as np

def create_grid():
    rows, cols = 10, 10

    grid = [[0 for _ in range(cols)] for _ in range(rows)]

    coords = [(1, 1), (2, 1), (2, 2), (1, 2), (5, 4), (5, 5), (5, 6), (5, 7),
              (6, 4), (6, 5), (6, 6), (6, 7), (3, 6), (3, 7), (4, 6), (4, 7),
              (9, 1), (9, 2), (8, 1), (8, 2), (7, 1), (7, 2)]

    for r, c in coords: grid[r][c] = 1

    grid[0][0] = 'S'
    grid[9][9] = 'G'

    return grid

def print_grid(grid):
    for row in grid:
        print(*(str(cell) for cell in row))

def find_cell(grid, label):
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == label:
                return (r,c)
    raise ValueError(f"No '{label}' found")

if __name__ == "__main__":
    grid = create_grid()


    print_grid(grid)
    print("Start:", find_cell(grid, 'S'))
    print("Goal:", find_cell(grid, 'G'))