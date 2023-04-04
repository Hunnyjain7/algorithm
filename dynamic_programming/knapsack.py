def dfs(i, profit, weight, capacity):
    if i == len(profit):
        return 0

    max_profit = dfs(i + 1, profit, weight, capacity)

    new_cap = capacity - weight[i]
    if new_cap >= 0:
        p = profit[i] + dfs(i + 1, profit, weight, new_cap)
        max_profit = max(max_profit, p)
    return max_profit


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


def memoization_knapsack(profit, weight, capacity):
    cache = [[-1] * (capacity + 1) for _ in range(len(profit))]
    dfs2(0, profit, weight, capacity, cache)
    return cache


if __name__ == '__main__':
    print(memoization_knapsack([4, 4, 7, 1], [5, 2, 3, 1], 8))
