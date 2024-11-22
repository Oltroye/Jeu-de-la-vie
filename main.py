from grille.grid import generate_grid, display_grid

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

    print("\nGrille générée :")
    display_grid(grille)

if __name__ == "__main__":
    main()
