# This program's purpose is to use a genetic algorithm to help a rat find
# its way through a map to get the block of cheese.


# importing random so i can get the random directions
import random

#directions for the random numbers
directions = [
    (-1, 0),  # UP
    (1, 0),   # DOWN
    (0, -1),  # LEFT
    (0, 1),   # RIGHT
    (-1, -1), # UP_LEFT
    (-1, 1),  # UP_RIGHT
    (1, -1),  # DOWN_LEFT
    (1, 1)    # DOWN_RIGHT
]

# function to create a 10x10 grid
def create_grid_10x10():
    rows, cols = 10, 10

    # setting up the grid
    grid = [[0 for _ in range(cols)] for _ in range(rows)]

    # initializing an empty list for the coordinates of the obstacles
    obstacles = []

    # setting the list full of obstacles
    for r in range(1, 3):
        for c in range(1, 3):
            obstacles.append((r, c))

    for r in range(5, 7):
        for c in range(4, 8):
            obstacles.append((r, c))

    for r in range(3, 5):
        for c in range(6, 8):
            obstacles.append((r, c))

    for r in range(7, 10):
        for c in range(1, 3):
            obstacles.append((r, c))

    for r, c in obstacles:
        grid[r][c] = 1

    # setting start and end points
    grid[0][0] = 'S'
    grid[9][9] = 'C'

    return grid

# function to create a 5x5 grid
def create_grid_5x5():
    rows, cols = 5, 5

    # setting the grid
    grid = [[0 for _ in range(cols)] for _ in range(rows)]

    # obstacles list
    obstacles = []


    # putting down obstacles
    for r in range(1, 3):
        for c in range(1, 3):
            obstacles.append((r, c))

    for r, c in obstacles:
        grid[r][c] = 1

    # setting start and end
    grid[0][0] = 'S'
    grid[4][4] = 'C'

    return grid

def create_grid_50x50():
    rows, cols = 50, 50

    # setting the grid
    grid = [[0 for _ in range(cols)] for _ in range(rows)]

    # obstacles list
    obstacles = []

    # setting obstacles into list
    for r in range(3, 12):
        for c in range(5, 9):
            obstacles.append((r, c))

    for r in range(2, 8):
        for c in range(17, 25):
            obstacles.append((r, c))

    for r in range(10, 18):
        for c in range(35, 42):
            obstacles.append((r, c))

    for r in range(18, 27):
        for c in range(3, 10):
            obstacles.append((r, c))

    for r in range(20, 29):
        for c in range(19, 27):
            obstacles.append((r, c))

    for r in range(25, 34):
        for c in range(38, 45):
            obstacles.append((r, c))

    for r in range(35, 43):
        for c in range(10, 17):
            obstacles.append((r, c))

    for r in range(38, 46):
        for c in range(25, 33):
            obstacles.append((r, c))

    for r in range(13, 17):
        for c in range(14, 18):
            obstacles.append((r, c))

    for r in range(32, 36):
        for c in range(5, 9):
            obstacles.append((r, c))

    for r, c in obstacles:
        grid[r][c] = 1

    # setting start and end
    grid[0][0] = 'S'
    grid[49][49] = 'C'

    return grid

# printing the original grid
def print_grid(grid):
    for row in grid:
        print(*(str(cell) for cell in row))

# printing the grid that includes the rat's path
def print_path(grid, path):

    # creating a copy of the grid since I don't wanna change it fully
    display_grid = [row[:] for row in grid]

    # setting the rat's path taken to asterisks
    for r, c in path:

        if display_grid[r][c] == 0:
            display_grid[r][c] = '*'

    # Print the new grid
    for row in display_grid:
        print(*row)

# function to get the valid moves that can be taken
def valid_moves(current_pos, grid):

    # getting the number of rows and columns in the grid
    rows = len(grid)
    cols = len(grid[0])

    # setting r and c to the row and column of the current position of the rat
    r, c = current_pos

    # initializing a list of possible moves
    possible_moves = []


    # iterate through each viable direction
    for r_change, c_change in directions:

        # new row and new column are set to the direction chosen.
        new_r = r + r_change
        new_c = c + c_change

        # if the move is within the boundaries...
        if 0 <= new_r < rows and 0 <= new_c < cols:

            # and if the move does not go into an obstacle...
            if grid[new_r][new_c] != 1:

                # then append the move to the list of moves
                possible_moves.append((new_r, new_c))

    # return the list of moves
    return possible_moves

# function to actually move the rat through the map
def traverse_grid(chromosome, grid):

    # setting start position and where the cheese is
    current_pos = (0, 0)
    cheese = (len(grid) - 1, len(grid[0]) - 1)

    # set a list and variable to keep track of the moves taken (valid and invalid respectively)
    path = [current_pos]
    invalid_moves = 0

    # iterate through each chromosome containing directions to go
    for move in chromosome:

        # if the current position is on the cheese, then leave the loop
        if current_pos == cheese:
            break

        # determine the next position of the rat
        row_change, col_change = directions[move]
        new_pos = (current_pos[0] + row_change, current_pos[1] + col_change)

        # check if the new position is allowed, and if so then set the new position and append to list of moves
        if new_pos in valid_moves(current_pos, grid):
            current_pos = new_pos
            path.append(current_pos)

        # or else add an invalid move to the invalid moves variable
        else:
            invalid_moves += 1

    # return the current position, the path taken, and how many invalid moves were taken
    return current_pos, path, invalid_moves

# find out the fitness of a chromosome depending on how well the rat does
def calculate_fitness(chromosome, grid):

    # set cheese
    cheese = (len(grid) - 1, len(grid[0]) - 1)

    # simulate the rat's movements matrix style
    final_pos, path, invalid_moves = traverse_grid(chromosome, grid)

    # finding the distance between the rat and the cheese (I use Chebyshev distance since the rat moves diagonally)
    distance = max(abs(cheese[0] - final_pos[0]), abs(cheese[1] - final_pos[1]))

    # initial fitness score
    fitness = 1000 / (distance + 1)

    # bad moves get bad rewards
    fitness -= invalid_moves * 2

    # a million billion trillion points for finding cheese minus a penalty for longer paths
    if final_pos == cheese:
        fitness += 100000000000 - (len(path) * 100)

    # returning the fitness score
    return max(fitness, 0.1)

# the bread and butter function. the actual genetic algorithm. creates the population,
# look at chromosomes, selects parent, and creates generations.
def genetic_algorithm(grid):

    # setting the parameters
    population_size = 100
    chromosome_length = len(grid) * 2
    generations = 200
    mutation_rate = 0.05

    # creating population
    population = []

    # iterate and set a random direction for each rat in the population
    for i in range(population_size):
        chromosome = []
        for j in range(chromosome_length):
            chromosome.append(random.randint(0, 7))
        population.append(chromosome)

        cheese_found = False

    # let's run this bih
    for generation in range(generations):

        # evaluation the fitness of each chromosome
        fitness_scores = []
        for chromosome in population:
            fitness = calculate_fitness(chromosome, grid)
            fitness_scores.append((fitness, chromosome))

        # Sort rats by fitness
        fitness_scores.sort(reverse=True, key=sort_fitness)

        # Keep the best rats
        best_rat = fitness_scores[0][1]
        best_fitness = fitness_scores[0][0]

        # Was the cheese found?
        final_pos, path, invalid_moves = traverse_grid(best_rat, grid)

        # if cheese was found, which generation found it? Then keep going.
        if final_pos == (len(grid) - 1, len(grid) - 1) and not cheese_found:
            print(f"{generation + 1} generation rat found the cheese! Ratkind has been saved!:")
            print("But can we find it faster???")
            cheese_found = True

        # Select the top 20% of rats
        parents = []
        for i in range(population_size // 5):
            parents.append(fitness_scores[i][1])

        # Create the next generation by copying the parents into the next population
        new_population = parents[:]

        # Now crossover time (Use crossover to combine 2 parents to make a child
        while len(new_population) < population_size:

            # choose the parents
            parent1 = random.choice(parents)
            parent2 = random.choice(parents)

            # split at a random point and merge
            split = random.randint(1, chromosome_length - 1)
            child = parent1[:split] + parent2[split:]

            # go through each variable in the chromosome and you
            # might replace a variable with a random direction, perchance
            for i in range(chromosome_length):
                if random.random() < mutation_rate:
                    child[i] = random.randint(0, 7)

            # child has been added to the new generation
            new_population.append(child)

        # the future is now, old man (replace old population with the new one)
        population = new_population

        # show the fitness of every 5 generations, starting at 0.
        if generation % 5 == 0:
            print("Generation: ", generation, "Best Fitness: ", best_fitness, "Steps: ", len(path) - 1)

    #Did we find a more optimal path?
    final_pos, path, invalid_moves = traverse_grid(best_rat, grid)
    if final_pos == (len(grid) - 1, len(grid) - 1):
        print("\nHOLY MOLY! THEY SAVED THE RAT UNIVERSE IN", len(path) - 1, "STEPS!!")

    # Reserved for the braindead generations
    # (If they never found the cheese, just give them a participation trophy)
    else:
        print("\nThe cheese blew up everything... it went undetected")

    return best_rat, path

# function to get the fitness score for each rat
def sort_fitness(rat):
    return rat[0]

# main function to print ts out
if __name__ == "__main__":

    # print the grid chosen
    grid = create_grid_50x50()
    print("Original Grid: ")
    print_grid(grid)

    # run the algorithm
    print("\nStarting Genetic Algorithm :) \n")
    best_rat, path = genetic_algorithm(grid)

    # print the path chosen
    print("\nGrid Showing Rat's Path: ")
    print_path(grid, path)

    # print how many moves were taken
    print("\nNumber of Moves: ", len(path) - 1)
