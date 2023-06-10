from utils import Node


def is_valid_bst(root_node):
    def inorder(node, mini, maxi):
        if node is None:
            return True
        if node.val <= mini or node.val >= maxi:
            return False
        return inorder(node.left, mini, node.val) and inorder(node.right, node.val, maxi)

    return inorder(root_node, float('-inf'), float('inf'))


root = Node(60)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(27)
root.insert(31)
root.insert(42)
print(is_valid_bst(root))
