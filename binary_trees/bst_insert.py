def insert(root, value):
    if root.val is None:
        root.val = value
        return print("Inserted")

    if value > root.val:
        return insert(root.right, value)
    else:
        return insert(root.left, value)
