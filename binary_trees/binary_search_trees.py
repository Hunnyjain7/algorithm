from utils import TreeNode


def binary_search_tree(root, target):
    if not root:
        return None
    if target > root.val:
        return binary_search_tree(root.right, target)
    elif target < root.val:
        return binary_search_tree(root.left, target)
    elif target == root.val:
        return print("Target found")


def insert(root, value):
    if root.val is None:
        root.val = value
        return print("Inserted")

    if value > root.val:
        return insert(root.right, value)
    else:
        return insert(root.left, value)


def min_root_value(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr


def remove(root, value):
    if not root:
        return None

    if root.val > value:
        root.left = remove(root.left, value)
    elif root.val < value:
        root.right = remove(root.right, value)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            min_node = min_root_value(root.right)
            root.val = min_node.val
            root.right = remove(root.right, min_node.val)
    return root


node = TreeNode(5)
print(binary_search_tree(node, 5))
