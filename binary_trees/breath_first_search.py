from collections import deque
from utils import Node


def search(root):
    queue = deque()
    if root:
        queue.append(root)

    level = 0
    while len(queue) > 0:
        print("level ::", level)
        for i in range(len(queue)):
            curr = queue.popleft()
            print(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        level += 1


root_ = Node(27)
root_.insert(14)
root_.insert(35)
root_.insert(3)
root_.insert(15)
root_.insert(45)
print(search(root_))
