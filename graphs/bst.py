
#implementing bst
#functions implemented are--> insert,preorder,inorder and postorder,  traversals and find , delete function.
class Node():
    def __init__(self,key):
        self.data = key
        self.right_child = None
        self.left_child = None
class BST():
    def __init__(self,key):
        self.root = key
    def insert(self,key):
        if not  isinstance(key,Node): 
            key = Node(key)
        if self.root == None:
            self.root = key
        else:
            self._insert(self.root,key)

    def _insert(self,root,key):
        if key.data > root.data:
            if root.right_child == None:
                root.rigth_child = key
            else:
                self._insert(root.right_child,key)
        if key.data < root.data:
            if root.left_child == None:
                root.left_child = key
            else:
                self._insert(root.left_child,key)
    def inorder(self):
        self._inorder(self.root)

    def _inorder(self,root):
        #left root right
        if root:
            self._inorder(root.left_child)
            print(self.root)
            self._inorder(root.right_child)
    def preorder(self):
        self._preorder(self.root)
    def _preorder(self,root):
        #root left right
        if root:
            print(self.root)
            self._preorder(root.left_child)
            self._preorder(root.right_child)
    def postorder(self):
        self._postorder(self.root)
    def _postorder(self,root):
        # left right root
        if root:
            self._postorder(root.left_child)
            self._postorder(root.right_child)
            print(self.root)
    def find_val(self,key):
        self._find_val(self.root,key)
    def _find_val(self,root,key):
        if root:
            if key == root.data:
                print("the value is in the tree")
            elif key < root.data:
                self._find_val(root.left_child,key)
            else:
                self._find_val(root.right_child,key)
        return "teh value is not found in the tree"
    def min_right_subtree(self,root):
        if root.left_child == None:
            return root
        else:
            return self.min_right_subtree(root.left_child)
    def delete_val(self,key):
        self._delete_val(self.root,None,None,key)
    def _delete_val(self,root,prev,is_left,key):
        return

        





