def min_node_val(root):
    curr = root
    while curr and root.left:
        curr = root.left
    return curr


def remove(root, value):
    if not root:
        return print("Removed")

    if value > root.val:
        return remove(root.right, value)
    elif value < root.val:
        return remove(root.left, value)
    else:
        if not root.left:
            return remove(root.right, root.val)
        elif not root.right:
            return remove(root.left, root.val)
        else:
            _min = min_node_val(root.right)
            root.val = _min.val
            return remove(root.left, _min.val)
