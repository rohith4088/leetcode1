class TreeNode():
    def __init__(self,val = 0,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right
def addOneRow(root,val,depth):
    if depth == 1:
        newroot = TreeNode(val)
        newroot.left = root
        return newroot
    def dfs(node,depth):
        if node is None:
            return
        if depth == 2:
            left = TreeNode(val)
            right = TreeNode(val)
            left.left = node.left
            right.right = node.right
            node.left = left
            node.right = right
        else:
            dfs(node.left,depth - 1)
            dfs(node.right,depth - 1)
    dfs(root,depth)
    return root
    
if __name__ == "__main__":
    #root = [4,2,6,3,1,5]
    root = TreeNode(4)
    root.left = TreeNode(2,TreeNode(3),TreeNode(1))
    root.right = TreeNode(6,TreeNode(5))
    print(addOneRow(root,1,2))
