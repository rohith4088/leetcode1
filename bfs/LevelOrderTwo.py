from collections import deque
class TreeNode:
    def __init__(self,val = 0,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right
def LevelOrder(root):
    if root is None:
        return []
    q = deque()
    q.append(root)
    big_list = []
    while q:
        size = len(q)
        small_list = []
        for _ in range(size):
            node = q.popleft()
            small_list.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        big_list.append(small_list)
    return big_list[::-1]

if __name__ == "__main__":
    #root = [3,9,20,null,null,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9,None,None)
    root.right = TreeNode(20,TreeNode(15,None,None),TreeNode(7,None,None))
    print(LevelOrder(root))

