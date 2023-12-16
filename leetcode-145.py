# 145. Binary Tree Postorder Traversal
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorderTraversal(root):
    arr = []
    if root is not None:
        arr += postorderTraversal(root.left)
        arr += postorderTraversal(root.right)
        arr.append(root.val)
    return arr


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

print(postorderTraversal(root))