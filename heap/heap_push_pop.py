class Heap:
    def __init__(self, arr):
        self.heap = [0] + arr

    def push(self, value):
        self.heap.append(value)
        last = len(self.heap) - 1
        while self.heap[last] < self.heap[last // 2]:
            self.heap[last // 2], self.heap[last] = self.heap[last], self.heap[last // 2]
            last = last // 2
        self.heap.pop(0)
        return self.heap

    def pop(self, value):
        self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
        first = 1
        while 2 * first < len(self.heap):
            left_child = 2 * first
            right_child = 2 * first + 1
            if self.heap[right_child] < self.heap[left_child] and right_child < len(self.heap) and self.heap[first] > \
                    self.heap[right_child]:
                self.heap[right_child], self.heap[first] = self.heap[first], self.heap[right_child]
                first = right_child
            elif self.heap[right_child] > self.heap[left_child]:
                self.heap[left_child], self.heap[first] = self.heap[first], self.heap[left_child]
                first = left_child
            else:
                break
        # if not is_popped:
        #     first = 1
        #     left_child = 2 * first
        #     right_child = 2 * first + 1
        #     while left_child <= len(self.heap) and right_child <= len(self.heap):
        #         if self.heap[first] == value:
        #             is_popped = True
        #             print("found")
        #             break
        #         if self.heap[left_child] > self.heap[right_child]:
        #             self.heap[left_child], self.heap[first] = self.heap[first], self.heap[left_child]
        #             first = left_child
        #             left_child = 2 * first
        #         else:
        #             self.heap[right_child], self.heap[first] = self.heap[first], self.heap[right_child]
        #             first = right_child
        #             right_child = 2 * first + 1
        self.heap.pop(0)
        self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
        self.heap.remove(value)
        return self.heap


heap = Heap([14, 19, 16, 21, 26, 19, 68, 65, 30])
# print(heap.push(17))
print(heap.pop(14))
