def path_exists(root):
    if not root or root.val == 0:
        return False
    if not root.left and not root.right:
        return True
    if path_exists(root.left):
        return True
    if path_exists(root.right):
        return True
    else:
        return False


def find_path(root, path):
    if not root or root.val == 0:
        return False
    path.append(root.val)
    if not root.left and not root.right:
        return True
    if find_path(root.left, path):
        return True
    if find_path(root.right, path):
        return True
    else:
        path.pop()
        return False
