from grille.grid import generate_grid, display_grid
from grille.save import load_grid, save_grid
from logique.rules import next_state
import os
import time

def verify_nb():
    while True:
        try:
            taille = int(input("Entrez la taille de la grille : "))
            if taille > 0:
                return taille
            else:
                print("Veuillez entrer un entier positif.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un entier.")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    action = input("Appuyez sur N pour une nouvelle grille ou L pour charger une sauvegarde : ").strip().upper()
    if action == 'L':
        grille, tour = load_grid()
        if grille is None:
            print("Aucune sauvegarde disponible. Création d'une nouvelle grille.")
            taille = verify_nb()
            grille = generate_grid(taille)
            tour = 0
    else:
        taille = verify_nb()
        grille = generate_grid(taille)
        tour = 0

    history = []  # Historique des grilles

    # Boucle principale
    while True:
        clear_screen()
        print(f"\nTour n°{tour}")
        display_grid(grille)

        action = input("\nAppuyez sur Entrée pour passer au tour suivant, S pour sauvegarder, ou Q pour quitter : ").strip().upper()
        if action == 'S':
            save_grid(grille, tour)  # Sauvegarde de la grille et du numéro du tour
            print("Grille sauvegardée.")
            time.sleep(3)  # Pause d'une seconde pour laisser le message visible
            continue
        elif action == 'Q':
            print("Fin du jeu. Au revoir !")
            break

    # Calculer la grille suivante
        next_grille = next_state(grille)
        if next_grille == grille:  # Vérifie si la grille est stable
            print(f"\nLa grille est stable au tour n°{tour}. Simulation arrêtée.")
            break

        grille = next_grille
        tour += 1


if __name__ == "__main__":
    main()
