# This memoization and caching technique is also called as Top Down Dynamic Programming
def memoization(n, cache):
    if n <= 1:
        return n
    if n in cache:
        return cache[n]
    cache[n] = memoization(n - 1, cache) + memoization(n - 2, cache)
    return cache[n]


# print(memoization(5, {}))


# Bottom Up Dynamic Programming || More often this is the real Dynamic Programming
def dp(n):
    if n <= 1:
        return n

    dp_list = [0, 1]
    count = 2
    while count <= n:
        dp_list[0], dp_list[1] = dp_list[1], dp_list[0] + dp_list[1]
        count += 1
    return dp_list[1]


print(dp(5))
