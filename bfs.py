#bfs algorithm using queue fifo
# bfs is level order algorithm
#implementing level order traversal

#tree class defination
from collections import deque
class TreeNode:
    def __init__(self,data = 0,left = None,right = None):
        self.data = data
        self.left = left
        self.right = right

def LevelOrder(head):
    if head is None:
        return []
    q = deque()
    q.append(head) 
    big_list = []
    while len(q):
        size = len(q)
        small_list = []
        for _ in range(size):
            node = q.popleft()
            small_list.append(node.data)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        big_list.append(small_list)
    return big_list

if __name__ == "__main__":
    #tree sturcuture
    #[3,9,20,null,null,15,7]
    head = TreeNode(3)
    head.left = TreeNode(9,None,None)
    head.right = TreeNode(20,TreeNode(15,None,None),TreeNode(7,None,None))
    print(LevelOrder(head))