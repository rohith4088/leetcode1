class Node():
    def __init__(self,key,right,left):
        self.data = key
        self.right = None
        self.left = None
class BST():
    def __init__(self):
        self.root = None
    def DeleteNode(self,root,key):
        if root is None:
            return root
        if key > root.data:
            root.right = self.DeleteNode(root.right,key)
        if key < root.data:
            root.left = self.DeleteNode(root.left,key)
        else:
            if not root.right : return root.left
            if not root.left : return root.right
            #find the min in the right subtree
            cur = root.right
            while cur.left:
                cur = cur.left
            root.data = cur.data
            root.right = self.DeleteNode(root.right,root.data)
        return root
