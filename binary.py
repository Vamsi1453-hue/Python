class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new = Node(value)
        if self.root is None:
            self.root = new
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.left is None:
                node.left = new
                return
            else:
                queue.append(node.left)
            if node.right is None:
                node.right = new
                return
            else:
                queue.append(node.right)

    def preorder(self, node, out=None):
        if out is None:
            out = []
        if node:
            out.append(node.value)
            self.preorder(node.left, out)
            self.preorder(node.right, out)
        return out

    def inorder(self, node, out=None):
        if out is None:
            out = []
        if node:
            self.inorder(node.left, out)
            out.append(node.value)
            self.inorder(node.right, out)
        return out

    def postorder(self, node, out=None):
        if out is None:
            out = []
        if node:
            self.postorder(node.left, out)
            self.postorder(node.right, out)
            out.append(node.value)
        return out

    def level_order(self):
        if not self.root:
            return []
        out, queue = [], [self.root]
        while queue:
            node = queue.pop(0)
            out.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return out

    def search(self, value):

        if not self.root:
            return False
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.value == value:
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False

    def height(self, node):
     
        if node is None:
            return 0
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height, right_height)
