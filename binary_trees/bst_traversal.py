# Depth first search
from utils import Node


def in_order(root_node):
    if not root_node:
        return
    a = root_node.val
    in_order(root_node.left)
    print(root_node.val)
    in_order(root_node.right)


def pre_order(root_node):
    if not root_node:
        return
    print(root_node.val)
    in_order(root_node.left)
    in_order(root_node.right)


def post_order(root_node):
    if not root_node:
        return
    in_order(root_node.left)
    in_order(root_node.right)
    print(root_node.val)


root = Node(60)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(27)
root.insert(31)
root.insert(42)
print(pre_order(root))
