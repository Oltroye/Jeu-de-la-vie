def voisinEnVie(grid, x, y):
    directions = [(-1, 1), (-1, 0), (-1, 1)
                  (0, -1),        (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    
    size = len(grid)
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < size and 0 <= ny < size and grid[nx][ny] == 1:
            count += 1
        return count
    

def updateGrid(grid):
    size = len(grid)
    newGrid = [[0] * size for _ in range(size)]

    for x in range(size):
        for y in range(size):
            voisin_Vie = voisinEnVie(grid, x, y)
            if voisin_Vie == 3 or (voisin_Vie == 2 and grid[x][y] == 1):
                newGrid[x][y] = 1
            else:
                newGrid[x][y] = 0
    return newGrid