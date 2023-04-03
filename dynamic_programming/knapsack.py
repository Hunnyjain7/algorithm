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


if __name__ == '__main__':
    print(knapsack([4, 4, 7, 1], [5, 2, 3, 1], 8))
