"""
Given a list of N items, and a backpack with a limited capacity, return the maximum total profit that
can be contained in the backpack. The i-th item's profit is profit[i] and it's weight is weight[i].
Assume you can only add each item to the bag at most one time.
"""


def dfs(i, profit, weight, capacity):
    if i == len(profit):
        return 0

    max_profit = dfs(i + 1, profit, weight, capacity)

    new_cap = capacity - weight[i]
    if new_cap >= 0:
        p = profit[i] + dfs(i + 1, profit, weight, new_cap)
        max_profit = max(max_profit, p)
    return max_profit


# Brute force Solution
# Time: O(2^n), Space: O(n)
# Where n is the number of items.
def knapsack(profit, weight, capacity):
    return dfs(0, profit, weight, capacity)


def dfs2(i, profit, weight, capacity, cache):
    if i == len(profit):
        return 0
    if cache[i][capacity] != -1:
        return cache[i][capacity]
    cache[i][capacity] = dfs2(i + 1, profit, weight, capacity, cache)

    new_cap = capacity - weight[i]
    if new_cap >= 0:
        p = profit[i] + dfs2(i + 1, profit, weight, new_cap, cache)
        cache[i][capacity] = max(cache[i][capacity], p)
    return cache[i][capacity]


# Memoization Solution
# Time: O(n * m), Space: O(n * m)
# Where n is the number of items & m is the capacity.
def memoization_knapsack(profit, weight, capacity):
    cache = [[-1] * (capacity + 1) for _ in range(len(profit))]
    return dfs2(0, profit, weight, capacity, cache)


# Dynamic Programming Solution
# Time: O(n * m), Space: O(n * m)
# Where n is the number of items & m is the capacity.
def dp(profit, weight, capacity):
    profit_len = len(profit)
    cache = [[0] * (capacity + 1) for _ in range(profit_len)]

    # Fill the first column and row to reduce edge cases
    for i in range(len(cache)):
        cache[i][0] = 0
    for i in range(capacity + 1):
        if weight[0] <= i:
            cache[0][i] = profit[0]

    for r in range(1, len(cache)):
        for c in range(1, capacity + 1):
            skip = cache[r - 1][c]
            include = 0
            new_cap = c - weight[r]
            if new_cap >= 0:
                include = profit[r] + cache[r - 1][new_cap]
            cache[r][c] = max(skip, include)

    return cache[-1][-1]


# Memory optimized Dynamic Programming Solution
# Time: O(n * m), Space: O(m)
def optimized_dp(profit, weight, capacity):
    profit_len = len(profit)
    prev_row = [0] * (capacity + 1)

    # Fill the first row to reduce edge cases
    for c in range(capacity + 1):
        if weight[0] <= c:
            prev_row[c] = profit[0]

    for r in range(1, profit_len):
        curr_row = [0] * (capacity + 1)
        for c in range(1, capacity + 1):
            skip = prev_row[c]
            include = 0
            new_cap = c - weight[r]
            if new_cap >= 0:
                include = profit[r] + prev_row[new_cap]
            curr_row[c] = max(include, skip)
        prev_row = curr_row
    return prev_row[capacity]


if __name__ == '__main__':
    print(optimized_dp([4, 4, 7, 1], [5, 2, 3, 1], 8))
