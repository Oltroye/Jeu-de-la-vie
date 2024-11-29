import random

def generate_grid(size):
    return [[random.choice([0, 1]) for _ in range(size)] for _ in range(size)]

def display_grid(grid):
    for row in grid:
        print(' '.join('⬛' if cell == 1 else '⬜' for cell in row))

