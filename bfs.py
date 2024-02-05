#bfs algorithm using queue fifo
# bfs is level order algorithm
#implementing level order traversal
from collections import deque
#Definition for a binary tree node.
class TreeNode:
    def __init__(self,val = 0,left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def levelorder(root):
    if root ==  None:
        return []
    q = deque()
    q.append(root)
    big_list =[]
    while len(q):
        size = len(q)
        small_list = []
        for _ in range(size):
            node = q.popleft()
            small_list.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        small_list.append(big_list)   
    return big_list
    
if __name__ == "__main__":
    #root = [3,9,20,null,null,15,7]
    head = TreeNode(3)
    head.left = TreeNode(9,None,None)
    head.right = TreeNode(20,TreeNode(15,None,None),TreeNode(7,None,None))
    print(levelorder(head))
    