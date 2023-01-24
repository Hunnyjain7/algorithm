def brute_force(n):
    if n <= 1:
        return n
    return brute_force(n - 1) + brute_force(n - 2)


print(brute_force(5))
