def count_neighbors(grid, i, j):
    """
    Compte le nombre de voisins vivants d'une cellule donnée dans une grille.
    """
    # Liste des positions relatives des voisins autour d'une cellule
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    n = len(grid)  # Taille de la grille (supposée carrée)
    living_neighbors = 0  # Compteur pour les voisins vivants

    # Parcourt chaque position relative des voisins
    for di, dj in neighbors:
        ni, nj = i + di, j + dj  # Calcule la position absolue du voisin
        # Vérifie si le voisin est dans les limites de la grille
        if 0 <= ni < n and 0 <= nj < n:
            living_neighbors += grid[ni][nj]  # Ajoute 1 si le voisin est vivant

    return living_neighbors


def next_state(grid):
    """
    Calcule l'état suivant de la grille selon les règles du jeu de la vie de Conway.
    """
    n = len(grid)  # Taille de la grille (supposée carrée)
    # Initialise une nouvelle grille remplie de zéros
    new_grid = [[0] * n for _ in range(n)]

    # Parcourt chaque cellule de la grille
    for i in range(n):
        for j in range(n):
            # Compte les voisins vivants de la cellule actuelle
            living_neighbors = count_neighbors(grid, i, j)

            # Règles pour les cellules vivantes
            if grid[i][j] == 1:
                if living_neighbors == 2 or living_neighbors == 3:
                    new_grid[i][j] = 1  # La cellule reste vivante
                else:
                    new_grid[i][j] = 0  # La cellule meurt
            else:
                # Règle pour les cellules mortes : elles revivent si elles ont exactement 3 voisins vivants
                if living_neighbors == 3:
                    new_grid[i][j] = 1

    return new_grid


def cycle_detect(grid, history):
    """
    Vérifie si la grille actuelle est déjà apparue dans l'historique
    (indiquant un cycle) et retourne la longueur du cycle si trouvé.
    """
    # Convertit la grille actuelle en un tuple de tuples (pour pouvoir la comparer dans l'historique)
    grid_tuple = tuple(tuple(row) for row in grid)

    # Vérifie si cette configuration est déjà dans l'historique
    if grid_tuple in history:
        cycle_start = history.index(grid_tuple)  # Trouve où le cycle a commencé
        cycle_length = len(history) - cycle_start  # Calcule la longueur du cycle
        return True, cycle_length  # Retourne le résultat

    # Aucun cycle détecté
    return False, 0
