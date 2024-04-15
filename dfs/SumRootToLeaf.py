class TreeNode():
    def __init__(self,val = 0,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right
def sumOfRoot(root):
    if root is None:
        return 0
    stack = [(root,[root.val])]
    total_sum = 0
    while stack:
        node,path = stack.pop()
        if node.left is None and node.right is None:
            total_sum += int(''.join(map(str,path)))
        if node.left:
            stack.append((node.left,path+[node.left.val]))
        if node.right:
            stack.append((node.right,path + [node.right.val]))
    return total_sum

if __name__ == '__main__':
    #root = [4,9,0,5,1]
    root = TreeNode(4)
    root.left = TreeNode(9,TreeNode(5),TreeNode(1))
    root.right = TreeNode(0)
    print(sumOfRoot(root))