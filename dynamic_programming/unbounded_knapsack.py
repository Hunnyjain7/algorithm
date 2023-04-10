""" Given a list of N items, and a backpack with a limited capacity, return the maximum total profit that
can be contained in the backpack. The i-th item's profit is profit[i] and it's weight is weight[i].
Assume you can have an unlimited number of each item available.
"""


def dfs(i, profit, weight, capacity):
    if i == len(profit):
        return 0

    # Skip item i
    max_profit = dfs(i + 1, profit, weight, capacity)

    # Include item i
    new_cap = capacity - weight[i]
    if new_cap >= 0:
        p = profit[i] + dfs(i, profit, weight, new_cap)
        # Compute the max
        max_profit = max(p, max_profit)
    return max_profit


# Brute force Solution
# Time: O(2^m), Space: O(m)
# Where m is the capacity.
def unbounded_knapsack(profit, weight, capacity):
    return dfs(0, profit, weight, capacity)


def dfs2(i, profit, weight, capacity, cache):
    if i == len(profit):
        return 0
    if cache[i][capacity] != 0:
        return cache[i][capacity]

    cache[i][capacity] = dfs(i + 1, profit, weight, capacity)
    new_cap = capacity - weight[i]
    if new_cap >= 0:
        p = profit[i] + dfs(i, profit, weight, new_cap)
        cache[i][capacity] = max(p, cache[i][capacity])
    return cache[i][capacity]


# Memoization Solution
# Time: O(n * m), Space: O(n * m)
# Where n is the number of items & m is the capacity.
def memoization_unbounded_knapsack(profit, weight, capacity):
    cache = [[0] * (capacity + 1) for _ in range(len(profit))]
    return dfs2(0, profit, weight, capacity, cache)


# Dynamic Programming Solution
# Time: O(n * m), Space: O(n * m)
# Where n is the number of items & m is the capacity.
def dp(profit, weight, capacity):
    cache = [[0] * (capacity + 1) for _ in range(len(profit))]

    # Fill the first column and row to reduce edge cases
    for i in range(len(profit)):
        cache[i][0] = 0
    for i in range(capacity + 1):
        if weight[0] <= i:
            cache[0][i] = profit[0]

    for r in range(len(cache)):
        for c in range(capacity + 1):
            skip = cache[r - 1][c]
            include = 0
            new_cap = c - weight[r]
            if new_cap >= 0:
                include = profit[r] + cache[r][new_cap]
            cache[r][c] = max(skip, include)
    return cache[-1][-1]


# Memory optimized Dynamic Programming Solution
# Time: O(n * m), Space: O(m)
def optimized_dp(profit, weight, capacity):
    prev_row = [0] * (capacity + 1)

    for r in range(len(profit)):
        curr_row = [0] * (capacity + 1)
        for c in range(capacity + 1):
            skip = prev_row[c]
            include = 0
            new_cap = c - weight[r]
            if new_cap >= 0:
                include = profit[r] + curr_row[new_cap]
            curr_row[c] = max(include, skip)
        prev_row = curr_row
    return prev_row[-1]


if __name__ == '__main__':
    print(optimized_dp([4, 4, 7, 1], [5, 2, 3, 1], 8))
