def heap_push(root, value):
    root.append(value)
    last = len(root) - 1
    while root[last] < root[last // 2]:
        temp = root[last]
        root[last // 2] = temp
        last = last // 2


print(heap_push([0, 14, 19, 16, 21, 26, 19, 68, 65, 30, 26], 17))
