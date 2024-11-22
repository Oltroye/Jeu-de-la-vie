from grille.grid import generate_grid, display_grid
from logique.rules import next_state
import os


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

def cleargrid():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    taille = verify_nb()
    grille = generate_grid(taille)
    history = []
    tour = 0

    while True:
        cleargrid()
        print(f"\nTour n°{tour}")
        display_grid(grille)

        # Vérification des cycles
        if grille in history:
            print(f"\nCycle détecté au tour n°{tour} ! Le jeu entre dans une boucle.")
            break
        history.append([row[:] for row in grille])  # Sauvegarde une copie de la grille

        grille = next_state(grille)
        tour += 1

        action = input("\nAppuyez sur Entrée pour passer au tour suivant, ou Q pour quitter : ").strip().upper()
        if action == 'Q':
            print("Fin du jeu. Au revoir !")
            break

if __name__ == "__main__":
    main()
