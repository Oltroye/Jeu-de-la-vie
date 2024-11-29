import random

def generate_grid(size):
    return [[random.choice([0, 1]) for _ in range(size)] for _ in range(size)] 
#cette fonction permet de générer une grille bidimensionnelle en fonction de n * n avec des cases aléatoires, les deux range(size) font référence à la colonne et la ligne

def display_grid(grid):
    for row in grid:
        print(' '.join('⬛' if cell == 1 else '⬜' for cell in row))

#affiche la grille avec des couleurs noires et blanches pour les cases on a une condition pour la case noire 1 sinon case blanche 0 dans chaque ligne