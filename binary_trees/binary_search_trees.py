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
