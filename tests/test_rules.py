from logique.rules import voisinEnVie, updateGrid

def test_voisin_en_vie():
    grid = [
        [0, 1, 0],
        [1, 1, 0],
        [0, 1, 0]
    ]
    assert voisinEnVie(grid, 1, 1) == 3
    assert voisinEnVie(grid, 0, 0) == 1

def test_grille():
    grid = [
        [0, 1, 0],
        [1, 1, 0],
        [0, 1, 0]
    ]

    newGrid = updateGrid(grid)
    assert newGrid[1][1] == 1