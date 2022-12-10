from datetime import datetime

a = [9683, 1154, 8494, 9560, 3268, 7814, 9956, 654, 4141, 5449, 6317, 5526, 5978, 9749, 3977, 9315, 5253, 2387, 4151]

st = datetime.now()
for i in range(len(a)):
    j = i - 1
    while j >= 0 and a[i] <= a[j]:
        a[i], a[j] = a[j], a[i]
        j -= 1
        i -= 1

print(a)
print(len(a), 'in this much of', datetime.now() - st)