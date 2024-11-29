from grille.grid import generate_grid, display_grid
from grille.save import load_grid, save_grid
from logique.rules import next_state, cycle_detect
import os


def verify_nb():
    """
    Demande à l'utilisateur d'entrer une taille valide pour la grille.
    """
    while True:
        try:
            taille = int(input("Entrez la taille de la grille (entre 1 et 45): "))
            if 1 <=taille <= 45:
                return taille
            else:
                print("Veuillez choisir un chiffre entre 1 et 45.")
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

    # Demande du choix utilisateur avec validation
    while True:
        action = input("Appuyez sur N pour une nouvelle grille ou L pour charger une sauvegarde : ").strip().upper()
        if action in ['N', 'L']:
            break  # Sort de la boucle si l'entrée est valide
        else:
            print("Entrée invalide. Veuillez appuyer sur N ou L.")

    # Gestion du choix
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
        is_cycle, cycle_length = cycle_detect(grille, history)
        if is_cycle:
            print(f"\nCycle détecté au tour n°{tour} ! Longueur du cycle : {cycle_length}")
            action = input("Appuyez sur S pour sauvegarder et quitter, ou Q pour quitter : ").strip().upper()
            if action == 'S':
                save_grid(grille, tour)
                print("Grille sauvegardée. Simulation arrêtée.")
                break
            elif action == 'Q':
                print("Simulation arrêtée sans sauvegarde.")
                break

        # Vérification de la stabilité
        next_grille = next_state(grille)
        if next_grille == grille:
            print(f"\nLa grille est stable au tour n°{tour}.")
            action = input("Appuyez sur S pour sauvegarder et quitter, ou Q pour quitter : ").strip().upper()
            if action == 'S':
                save_grid(grille, tour)
                print("Grille sauvegardée. Simulation arrêtée.")
                break
            elif action == 'Q':
                print("Simulation arrêtée sans sauvegarde.")
                break

        # Ajouter la grille à l'historique (après vérifications)
        history.append(tuple(tuple(row) for row in grille))  # Ajoute une copie immuable de la grille

        # Demander à l'utilisateur de continuer ou de quitter
        action = input("\nAppuyez sur Entrée pour passer au tour suivant, ou Q pour quitter : ").strip().upper()
        if action == 'Q':
            print("Fin du jeu. Au revoir !")
            break

        # Passer au tour suivant
        grille = next_grille
        tour += 1


if __name__ == "__main__":
    main()