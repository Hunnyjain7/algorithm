a = [1, 2, 5, 9, 4, 10]

for i in range(len(a)):
    j = i - 1
    while j >= 0 and a[i] <= a[j]:
        a[i], a[j] = a[j], a[i]
        j -= 1
        i -= 1

print(a)
