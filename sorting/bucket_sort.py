arr = [1, 0, 2, 1, 0, 2, 1]


def bucket_sort(array):
    counts = [0, 0, 0]
    for i in array:
        counts[i] += 1

    count = 0
    for i in range(len(counts)):
        for j in range(counts[i]):
            array[count] = i
            count += 1
    return array


print(bucket_sort(arr))
