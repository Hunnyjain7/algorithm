# dfs Depth First search

# Count paths (backtracking)
def dfs(grid, r, c, visit):
    rows, cols = len(grid), len(grid[0])

    if min(r, c) < 0 or r == rows or c == cols or grid[r][c] == 1 or (r, c) in visit:
        return 0
    if r == rows - 1 and c == cols - 1:
        return 1

    visit.add((r, c))
    count = 0
    dfs(grid, r + 1, c, visit)
    dfs(grid, r - 1, c, visit)
    dfs(grid, r, c + 1, visit)
    dfs(grid, r, c - 1, visit)

    visit.remove((r, c))
    return count


# Matrix (2D Grid)
matrics = [[0, 0, 0, 0],
           [1, 1, 0, 0],
           [0, 0, 0, 1],
           [0, 1, 0, 0]]
dfs(matrics, 0, 0, set())
