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


def level_order(root):
    queue = deque()
    res = []
    if root:
        res.append([root.val])
        queue.append(root)
        while queue:
            curr = []
            nex = deque()
            while queue:
                hp = queue.popleft()
                if hp.left:
                    nex.append(hp.left)
                    curr.append(hp.left.val)
                if hp.right:
                    nex.append(hp.right)
                    curr.append(hp.right.val)
            if curr:
                res.append(curr)
            queue = nex
    return res


def zigzag_level_order(root):
    queue = deque()
    res = []
    if root:
        res.append([root.val])
        queue.append(root)
        right = True
        while queue:
            curr = []
            nex = deque()
            while queue:
                hp = queue.popleft()
                if hp.left:
                    nex.append(hp.left)
                    curr.append(hp.left.val)
                if hp.right:
                    nex.append(hp.right)
                    curr.append(hp.right.val)
            if curr:
                if right:
                    curr = curr[::-1]
                    right = False
                else:
                    right = True
                res.append(curr)
            queue = nex
    return res


root_ = Node(27)
root_.insert(14)
root_.insert(35)
root_.insert(3)
root_.insert(15)
root_.insert(45)
print(search(root_))
