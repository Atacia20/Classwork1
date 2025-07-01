class TreeNode:
    def _init_(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, key):
        if key < self.value:
            if self.left is None:
                self.left = TreeNode(key)
            else:
                self.left.insert(key)
        elif key > self.value:
            if self.right is None:
                self.right = TreeNode(key)
            else:
                self.right.insert(key)

    def find(self, tey):
        if tey < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(tey)
        elif tey > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(tey)
        else:
            return True

    def preorder_traversal(self):
        print(self.value)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()

    def postorder_traversal(self):

        if self.left:
            self.left.postorder_traversal()
        print(self.value)
        if self.right:
            self.right.postorder_traversal()

        print(self.value)


if _name_ == '_main_':
    tree = TreeNode("50")
    tree.insert("12")
    tree.insert("22")
    tree.insert("2")
    tree.insert("42")
    tree.insert("72")
    tree.insert("32")
    tree.insert("752")
    tree.postorder_traversal()
