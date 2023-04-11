def count_bits(n):
    count = 0
    while n > 0:
        count += 1
        n = n >> 1
    return count


print(count_bits(23))


# count numbers of 1 bit's
def count_1_bits(n):
    count = 0
    while n > 0:
        if n & 1 == 1:
            count += 1
        n = n >> 1  # Bit shifting
    return count


print(count_1_bits(23))
