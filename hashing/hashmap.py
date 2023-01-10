array = ["a", "b", "c", "b", "d", "a"]

data = {}
for i in array:
    if i in data.keys():
        data[i] += 1
    else:
        data[i] = 1
print(data)