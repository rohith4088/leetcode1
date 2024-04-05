#AVERAGE OF LEVELS IN BINARY TREE
#defination of the binary tree
from collections import deque
class TreeNode():
    def __init__(self,val = 0,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right
def avg_levels(root):
    q = deque()
    al = []
    q.append(root)
    while len(q):
        sum_val = 0
        size = len(q)
        for _ in range(size):
            node = q.popleft()
            sum_val += node.val
            if node.left:
                q.append(node.left)
                
    
if __name__ == "__main__":
    bt = TreeNode(3,TreeNode(9,None,None),TreeNode(20,TreeNode(15,None,None),TreeNode(7,None,None)))
    print(avg_levels(bt))