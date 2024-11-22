from grille.grid import generate_grid, display_grid
from logique.rules import next_state

def verif_nb():
    while True:
        try:
            taille = int(input("Entrez la taille de la grille : "))
            if taille > 0:
                return taille
            else:
                print("Veuillez entrer un entier positif.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un entier.")

def main():

    taille = verif_nb()

    grille = generate_grid(taille)

    while True:
        print("\nGrille actuelle :")
        display_grid(grille)
        
        grille = next_state(grille)

        action = input("\nAppuyez sur Entrée pour passer au tour suivant, ou Q pour quitter : ").strip().upper()
        if action == 'Q':
            print("Fin du jeu. Au revoir !")
            break

if __name__ == "__main__":
    main()
