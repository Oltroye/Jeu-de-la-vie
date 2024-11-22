import json

def save_grid(grid, tour, filename="data/save.json"):
    """
    Sauvegarde l'état actuel de la grille et le numéro du tour dans un fichier JSON.

    Args:
        grid (list of list): La grille à sauvegarder.
        tour (int): Le numéro du tour actuel.
        filename (str): Nom du fichier de sauvegarde.
    """
    with open(filename, "w") as file:
        json.dump({"grille": grid, "tour": tour}, file)

def load_grid(filename="data/save.json"):
    """
    Charge une grille et un numéro de tour depuis un fichier JSON.

    Args:
        filename (str): Nom du fichier de sauvegarde.

    Returns:
        tuple: (grille, tour) - La grille et le numéro de tour, ou (None, 0) si erreur.
    """
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return data["grille"], data["tour"]
    except FileNotFoundError:
        print("Aucune sauvegarde trouvée.")
        return None, 0
