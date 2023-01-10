array = ["a", "b", "c", "b", "d", "a"]

data = {}
for i in array:
    if i in data.keys():
        data[i] += 1
    else:
        data[i] = 1
print(data)


class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val


class HashMap:
    def __init__(self):
        self.size = 0
        self.capacity = 2
        self.map = [None, None]

    def hash(self, key):
        value = 0
        for i in key:
            value += ord(i)
        return value % self.capacity

    def get(self, key):
        index = self.hash(key)
        while self.map[index] is not None:
            if self.map[index].key == key:
                return self.map[index].val
            index += 1
            index = index % self.capacity
        return None

    def put(self, key, val):
        index = self.hash(key)

        while True:
            if self.map[index] is None:
                self.map[index] = Pair(key, val)
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.rehash()
                    return
            elif self.map[index].key == key:
                self.map[index].val = val
                return
            index += 1
            index = index % self.capacity

    def rehash(self):
        self.capacity = 2 * self.capacity
        new_map = []
        for i in range(self.capacity):
            new_map.append(None)

        olp_map = self.map
        self.map = new_map
        self.size = 0

        for pair in olp_map:
            if pair:
                self.put(pair.key, pair.val)
