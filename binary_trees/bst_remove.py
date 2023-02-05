def min_root_val(root):
    curr = root
    while curr and root.left:
        curr = root.left
    return curr.val


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
            min_root_value = min_root_val(root.right)
            root.val = min_root_value
            root.right = remove(root.right, min_root_value)
    return root
