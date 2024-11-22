def count_neighbors(grid, i, j):
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    n = len(grid)
    living_neighbors = 0
    for di, dj in neighbors:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < n:
            living_neighbors += grid[ni][nj]
    return living_neighbors

def next_state(grid):
    n = len(grid)
    new_grid = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            living_neighbors = count_neighbors(grid, i, j)
            if grid[i][j] == 1:
                if living_neighbors == 2 or living_neighbors == 3:
                    new_grid[i][j] = 1
                else:
                    new_grid[i][j] = 0
            else:
                if living_neighbors == 3:
                    new_grid[i][j] = 1
    return new_grid
