from grille.grid import generate_grid, display_grid
from grille.save import load_grid, save_grid
from logique.rules import next_state
import os



def verify_nb():
    """
    Demande à l'utilisateur d'entrer une taille valide pour la grille.
    """
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
    """
    Nettoie l'écran pour une meilleure lisibilité dans le terminal.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    """
    Point d'entrée principal pour le jeu de la vie.
    """
    # Initialisation des variables
    tour = 0
    history = []  # Historique des grilles

    # Choix de l'utilisateur : charger une sauvegarde ou créer une nouvelle grille
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

    # Boucle principale
    while True:
        clear_screen()
        print(f"\nTour n°{tour}")
        display_grid(grille)

        # Vérification des cycles
        if grille in history:
            print(f"\nCycle détecté au tour n°{tour} !")
            print("Vous pouvez appuyer sur Entrée pour continuer ou S pour sauvegarder et quitter.")

        # Vérification de la stabilité
        next_grille = next_state(grille)
        if next_grille == grille:
            print(f"\nLa grille est stable au tour n°{tour}.")
            print("Vous pouvez appuyer sur Entrée pour continuer ou S pour sauvegarder et quitter.")

        # Sauvegarde de la grille dans l'historique
        history.append([row[:] for row in grille])  # Sauvegarde une copie de la grille

        # Option pour sauvegarder, quitter ou continuer
        action = input("\nAppuyez sur Entrée pour passer au tour suivant, S pour sauvegarder et quitter, ou Q pour quitter : ").strip().upper()
        if action == 'S':
            save_grid(grille, tour)
            print("Grille sauvegardée. Simulation arrêtée.")
            break
        elif action == 'Q':
            print("Simulation arrêtée sans sauvegarde. Au revoir !")
            break

        # Passer au tour suivant
        grille = next_grille
        tour += 1


if __name__ == "__main__":
    main()
