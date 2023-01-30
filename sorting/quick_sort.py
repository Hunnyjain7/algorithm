def quick_sort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quick_sort(arr, left, partition_pos - 1)
        quick_sort(arr, partition_pos + 1, right)


def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]
    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    return i


# def quick_sort(array, s, e):
#     if e - s + 1 <= 1:
#         return
#     pivot = array[e]
#     insert = s
#     for i in range(s, e):
#         if array[i] < pivot:
#             array[insert], array[i] = array[i], array[insert]
#             insert += 1
#     array[insert], array[e] = array[e], array[insert]
#     quick_sort(array, s, insert - 1)
#     quick_sort(array, insert + 1, e)
#     return array


a = [9683, 1154, 8494, 9560, 3268, 7814, 9956, 654, 4141, 5449, 6317, 5526, 5978, 9749, 3977, 9315, 5253, 2387, 4151]
print(quick_sort(a, 0, len(a) - 1))
