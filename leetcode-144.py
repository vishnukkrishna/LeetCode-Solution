class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root):
    arr = []
    if root is not None:
        arr.append(root.val)
        arr += preorderTraversal(root.left)
        arr += preorderTraversal(root.right)
    return arr



root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

print(preorderTraversal(root))