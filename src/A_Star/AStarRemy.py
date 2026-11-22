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
 
 
def find_cell(grid, label):
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == label:
                return (r, c)
    raise ValueError(f"No '{label}' found")
 
 
if __name__ == "__main__":
    for make_grid in (create_grid_5x5, create_grid_10x10, create_grid_50x50):
        grid = make_grid()
        print(f"{make_grid.__name__}: {len(grid)}x{len(grid[0])}")
        print_grid(grid)
        print("Start:", find_cell(grid, 'S'), "Goal:", find_cell(grid, 'G'))
        print()
 