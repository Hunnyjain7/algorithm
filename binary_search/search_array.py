def search_in_array(array, target):
    """
    :param array It should be an sorted array:
    :param target:
    :return: searched value
    """
    l, r = 0, len(array) - 1

    while l <= r:
        mid = (l + r) // 2
        if target > array[mid]:
            l = mid + 1
        elif target < array[mid]:
            r = mid - 1
        else:
            return array[mid]
    return None


arr = [0, 4, 10, 30, 44, 69, 99]
print(search_in_array(arr, 100))
