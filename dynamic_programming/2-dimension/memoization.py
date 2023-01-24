def memoization(r, c, rows, cols, cache):
    if r == rows or c == cols:
        return 0
    if cache[r][c] > 0:
        return cache[r][c]
    if r == rows - 1 and c == cols - 1:
        return 1
    cache[r][c] = memoization(r + 1, c, rows, cols, cache) + memoization(r, c + 1, rows, cols, cache)
    return cache[r][c]


# print(memoization(0, 0, 4, 4, [[0] * 4 for i in range(4)]))

def dp(rows, cols):
    prev_row = [0] * 4

    for r in range(rows - 1, -1, -1):
        curr_row = [0] * cols
        curr_row[-1] = 1

        for c in range(cols - 2, -1, -1):
            curr_row[c] = curr_row[c + 1] + prev_row[c]
        prev_row = curr_row
    return prev_row[0]


print(dp(4, 4))
