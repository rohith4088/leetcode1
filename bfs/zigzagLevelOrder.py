# from collections import deque
# class TreeNode:
#     def __init__(self,val = 0,left = None,right = None):
#         self.val = val
#         self.left = left
#         self.right = right
# def zigzag(root):
#     if root is None:
#         return []
#     q = deque()
#     q.append(root)
#     big_list = []
#     flag = False
#     while len(q):
#         size = len(q)
#         small_list= []
#         for _ in range(size):
#             node = q.popleft()
#             small_list.append(node.val)
#             if node.left:
#                 q.append(node.left)
#             if node.right:
#                 q.append(node.right)
#         if flag:
#             small_list.reverse()
#         big_list.append(small_list)
#         flag = not flag
#     return big_list

# if __name__ == "__main__":
#     #root = [3,9,20,null,null,15,7]
#     root = TreeNode(3)
#     root.left = TreeNode(9,None,None)
#     root.right = TreeNode(20,TreeNode(15,None,None),TreeNode(7,None,None))
#     print(zigzag(root))
# #ONLY PASSES TWO TEST CASES


#PASSES ALL THE TEST CASES
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
