# Jeu de la Vie
Une implémentation du célèbre automate cellulaire de John Conway, "Le Jeu de la Vie". Ce projet génère une grille interactive où chaque cellule évolue selon des règles simples, créant des motifs dynamiques fascinants.

# Le but de notre projet
Après avoir fait la piscine en python, nous avons eu comme projet imposé le jeu de la vie à faire en binôme pour appliquer ce qu'on a appris. Ronan et Stanislas (moi-même) avons répartie les tâches de cette manière : 

Ronan :

- Génération de la grille
- Affichage de la grille
- Une partie du main pour gérer la logique du jeu

Stanislas :

- Logique du jeu
- Gestion des cas d'erreurs

# Outils utilisé

- VSCode
- Documentation Python
- Internet

# Installation

Installer Python la version la plus récente si vous pouvez sur le site officiel ou via le microsoft store si vous êtes sur Windows. Télécharger notre dépôt ou le cloner et aller directement dans le dossier.

# Architecture du code

jJEU-DE-LA-VIE/ 
│ 
├── data/ 
│ └── save.json 
│ 
├── grille/ 
│ ├── grid.py 
│ └── save.py 
│ 
├── logique/ 
│     └── rules.py  
│ 
├── main.py 
└── README.md

# Lancement du projet

Une fois que vous télécharger ou cloner le dépôt vous ouvrez le dossier grâce à VSCode et ouvrez le terminal et lancer le fichier main.py.

# Fonctionnalités
- Génération d'une grille aléatoire avec des cellules vivantes et mortes.
- Interaction utilisateur pour avancer manuellement dans les cycles.
- Détection des cycles (motifs périodiques).
- Détection des grilles stables.
- Possibilité de sauvegarder et charger une grille.
- Affichage clair de la grille dans le terminal.

# Contributeurs

- Ronan Dupas Développement
- Stanislas Ibrahim Développement