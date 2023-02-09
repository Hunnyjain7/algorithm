array = ["a", "b", "c", "b", "d", "a"]

data = {}
for j in array:
    if j in data.keys():
        data[j] += 1
    else:
        data[j] = 1


# print(data)


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
                return self.map
            elif self.map[index].key == key:
                self.map[index].val = val
                return self.map
            index += 1
            index = index % self.capacity

    def remove(self, key):
        if not self.get(key):
            return

        index = self.hash(key)
        while True:
            if self.map[index].key == key:
                """ Removing an element using open-addressing actually causes a bug,
                 because we may create a hole in the list, and our get() 
                 may stop searching early when it reaches this hole."""
                self.map[index] = None
                self.size -= 1
                return
            index += 1
            index = index % self.capacity

    def rehash(self):
        capacity = self.capacity
        self.capacity = 2 * capacity
        for i in range(capacity, self.capacity):
            self.map.append(None)


hash_map = HashMap()
print(hash_map.put("Alice", "Chicago"))
# hash_map.put("Brad", "Settle")
# hash_map.put("Rahul", "Delhi")
# print(hash_map.rehash())
# print(hash_map.size)
# print(hash_map.capacity)
# print(hash_map.map)
