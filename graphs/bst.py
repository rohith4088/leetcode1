
# implementing bst
# functions implemented are--> insert,preorder,inorder and postorder,  traversals and find , delete function.
class Node():
    def __init__(self,key):
        self.data = key
        self.right_child = None
        self.left_child = None
class BST():
    def __init__(self):
        self.root = None
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
        l#eft right root
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
        self._delete_val(self.root,key)
    def _delete_val(self,root,key):
        if root is None:
            return root
        if key > root.data:
            root.right_child = self._delete_val(root.right_child,key)
        if key < root.data:
            root.left_child = self._delete_val(root.left_child,key)
        else:
            if not root.right_child: return root.left_child
            if not root.left_child: return root.rigth_child
            cur = root.right_child
            while cur.left_child:
                cur = cur.left_child
            root.data = cur.data
            root.right_child = self._delete_val(root.right_child,root.data)
        return root
tree = BST()
tree.insert("F")
tree.insert("C")
print("Test deleting leaf node which is left child of parent")
tree.inorder()
tree.delete_val("C")
tree.inorder()
tree.insert("G")
print("Test deleting leaf node which is right child of parent")
tree.inorder()
tree.delete_val("G")
tree.inorder()
tree.insert("A")
print("Test deleting parent/root node which has one child")
tree.inorder()
tree.delete_val("F")
tree.inorder()
print("Test deleting root node which has no children")
tree.inorder()
tree.delete_val("A")
tree.inorder()
tree.insert("F")
tree.insert("C")
tree.insert("G")
tree.insert("A")
tree.insert("B")
tree.insert("K")
tree.insert("E")
tree.insert("H")
tree.insert("D")
tree.insert("I")
tree.insert("M")
tree.insert("J")
tree.insert("L")
tree.inorder()
tree.delete_val("F")
tree.inorder()
tree.inorder()
tree.delete_val("K")
tree.inorder()
tree.inorder()
tree.delete_val("C")
tree.inorder()
tree.delete_val("Z")

        





