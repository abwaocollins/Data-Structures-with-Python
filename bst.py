class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        # append to the root node

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, val):
        if val == self.data:
            return True
        if val < self.data:
            if self.left:
                self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                self.search(val)
            else:
                return False


def build_tree(elements):
    root = BinarySearchTree(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
print("In order traversal gives this sorted list:",
      numbers_tree.in_order_traversal())
print(f" 17 in the random numbers: {numbers_tree.search(17)}")
