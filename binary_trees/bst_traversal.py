from utils import Node


def in_order(root_node):
    if not root_node:
        return
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


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root)
print(post_order(root))
