from utils import Node


def insert(root, value):
    if not root:
        return Node(value)

    if value > root.val:
        return insert(root.right, value)
    else:
        return insert(root.left, value)


root_ = Node(27)
root_.insert(14)
root_.insert(35)
print(insert(root_, 30))
