import json
import os

def save_grid(grid, tour, filename="data/save.json"):
    """
    Sauvegarde l'état actuel de la grille et le numéro du tour dans un fichier JSON.

    Args:
        grid (list of list): La grille à sauvegarder.
        tour (int): Le numéro du tour actuel.
        filename (str): Nom du fichier de sauvegarde.
    """
    try:
        # S'assurer que le dossier `data` existe
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as file:
            json.dump({"grille": grid, "tour": tour}, file)
            print(f"Sauvegarde effectuée dans {filename}.")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde : {e}")

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
            content = file.read()
            if not content.strip():  # Vérifie si le fichier est vide
                print("Le fichier de sauvegarde est vide.")
                return None, 0
            data = json.loads(content)
            return data["grille"], data["tour"]
    except FileNotFoundError:
        print(f"Aucun fichier de sauvegarde trouvé dans {filename}.")
        return None, 0
    except json.JSONDecodeError:
        print(f"Le fichier {filename} est corrompu.")
        return None, 0