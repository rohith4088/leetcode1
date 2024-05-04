# class TreeNode:
#     def __init__(self,val = 0,left = None,right = None):
#         self.val = val
#         self.left = left
#         self.right = right
# def isSameTree(p,q):
#     if p is None and q is None:
#         return True
#     if p is None or q is None:
#         return False
#     if p.val != q.val:
#         return False
#     return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)

#     #p = [1,2,3]
#     #q = [1,2,3]
# p = TreeNode(1)
# p.left = TreeNode(2)
# p.right = TreeNode(3)

# q = TreeNode(1)
# q.left = TreeNode(2)
# q.right = TreeNode(3)
# print(isSameTree(p,q))



class TreeNode:
    def __init__(self,root = 0,left = None,right = None):
        self.root = root
        self.left = left
        self.right = right

if __name__ == "__main__":
    #root = [3,9,20,null,null,15,20]
    p = TreeNode(3)
    p.left = TreeNode(9,None,None)
    p.right = TreeNode(20,TreeNode(15,None,None),TreeNode(7,None,None))
    q = TreeNode(3)
    q.left = TreeNode(9,None,None)
    q.right = TreeNode(20,TreeNode(15,None,None),TreeNode(7,None,None))
