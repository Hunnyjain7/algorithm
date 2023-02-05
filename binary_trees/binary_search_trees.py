from utils import Node


def binary_search_tree(root, target):
    if not root:
        return None
    if target > root.val:
        return binary_search_tree(root.right, target)
    elif target < root.val:
        return binary_search_tree(root.left, target)
    elif target == root.val:
        return print("Target found")


root_ = Node(27)
root_.insert(14)
root_.insert(35)
binary_search_tree(root_, 14)
