from collections import deque
class TreeNode:
    def __init__(self,val = 0,left = None,right = None):
        self.val = val
        self.right = right
        self.left = left
def AverageOfLevels(root):
    if not root:
        return []
    q = deque()
    q.append(root)
    average_list = []
    while len(q):
        size = len(q)
        sum_val = 0
        for _ in range(size):
            node = q.popleft()
            sum_val += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        average_list.append(sum_val/size)
    return average_list
if __name__ == "__main__":
    #[3,9,20,null,null,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9,None,None)
    root.right = TreeNode(20,TreeNode(15,None,None),TreeNode(7,None,None))
    print(AverageOfLevels(root))
