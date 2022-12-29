def search_range(low, high):
    """
    :param low: lowest value
    :param high: highest value
    :return: range
    """
    while low <= high:
        mid = (low + high) // 2
        if is_correct(mid) > 0:
            high = mid - 1
        elif is_correct(mid) < 0:
            low = mid + 1
        else:
            return mid


def is_correct(n):
    if n > 10:
        return 1
    elif n < 10:
        return -1
    else:
        return 0


if __name__ == "__main__":
    res = search_range(1, 100)
    print(res)