class TreeNode:
    def __init__(self,val = 0,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right
def isMirror(root):
    if root is None:
        return True
    return isSymmetric(root.left,root.right)
def isSymmetric(left,right):
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    
    if (left.val != right.val):
        return False
    return isSymmetric(left.left , right.right) and isSymmetric(left.right,right.left)
if __name__ == "__main__":
    #[1,2,2,3,4,4,3]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    print(isMirror(root))

