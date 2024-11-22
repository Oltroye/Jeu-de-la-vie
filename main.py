from grille.grid import generate_grid, display_grid, next_state, save_grid
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

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    taille = verify_nb()
    grille = generate_grid(taille)

    while True:
        clear_screen()
        print("\nGrille actuelle :")
        display_grid(grille)

        action = input("\nAppuyez sur Entrée pour passer au tour suivant, S pour sauvegarder, ou Q pour quitter : ").strip().upper()
        if action == 'S':
            save_grid(grille)  # Sauvegarde la grille dans un fichier
            print("Grille sauvegardée.")
        elif action == 'Q':
            print("Fin du jeu. Au revoir !")
            break

        grille = next_state(grille)  # Calculer la grille suivante

if __name__ == "__main__":
    main()
