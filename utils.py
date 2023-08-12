class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    @staticmethod
    def min_root_val(root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr.val

    def insert(self, val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

    def remove(self, root, val):
        if not root:
            return

        if val > root.val:
            root.right = self.remove(root.right, val)
        elif val < root.val:
            root.left = self.remove(root.left, val)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                min_val = self.min_root_val(root.right)
                root.val = min_val
                root.right = self.remove(root.right, min_val)
        return root
