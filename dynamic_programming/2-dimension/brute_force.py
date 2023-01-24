def brute_force(r, c, rows, cols):
    if r == rows or c == cols:
        return 0
    if r == rows - 1 and c == cols - 1:
        return 1
    return brute_force(r + 1, c, rows, cols) + brute_force(r, c + 1, rows, cols)


print(brute_force(0, 0, 4, 4))
