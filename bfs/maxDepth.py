class TreeNode:
    def __init__(self,val = 0,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    if root is None:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)

    return max(left_depth,right_depth) + 1
if __name__ == "__main__":
    #root = [3,9,20,null,null,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9,None , None)
    root.right = TreeNode(20,TreeNode(15,None,None),TreeNode(7,None , None))
    print(maxDepth(root))
