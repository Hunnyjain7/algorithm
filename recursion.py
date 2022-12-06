# --------------------------- ONE Branch ----------------------------
a = 5


def factorial(n):
    if n == 1:
        return 1
    b = n * factorial(n - 1)
    return b


print(factorial(a))

# better non-recursive solution as the above recursive solution will consume high memory
"""
# non-recursive solution
n = 1
while a > 1:
    n = n * a
    print(n)
    a -= 1
print(n)
"""


# --------------------------- TWO Branch ----------------------------

def fibonacci(c):
    if c <= 1:
        return c
    return fibonacci(c - 1) + fibonacci(c - 2)


print(fibonacci(8))
