class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    
    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            #add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = TreeNode(data)
        else:
            #add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = TreeNode(data)

    def in_order_traversal(self, root):
        elements = []

        
        if root:

            elements = self.in_order_traversal(root.left)
            elements.append(root.data)
            elements = elements + self.in_order_traversal(root.right)
            
        return elements

    
root = TreeNode(27)
root.add_child(15)
root.add_child(16)
root.add_child(18)
root.add_child(23)
root.add_child(1)
print(root.in_order_traversal(root))





