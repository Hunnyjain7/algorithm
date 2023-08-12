def min_root_val(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr.val


def remove(root, value):
    if not root:
        return print("Removed")

    if value > root.val:
        root.right = remove(root.right, value)
    elif value < root.val:
        root.left = remove(root.left, value)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            min_root_value = min_root_val(root.right)
            root.val = min_root_value
            root.right = remove(root.right, min_root_value)
    return root
