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
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.search(val)
            else:
                return False

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = [self.data]

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()
        return elements

    def calc_sum(self):
        left_branch = self.left.calc_sum() if self.left else 0
        right_branch = self.right.calc_sum() if self.right else 0

        return self.data + left_branch + right_branch
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.right and self.left is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(val)

        return self



def build_tree(elements):
    root = BinarySearchTree(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
print("In order traversal gives this sorted list:",
      numbers_tree.in_order_traversal())
print(f" 17 in the random numbers: {numbers_tree.search(17)}")
print(f"max is {numbers_tree.find_max()}")

print("Sum:", numbers_tree.calc_sum())
print("In order traversal:", numbers_tree.in_order_traversal())
print("Pre order traversal:", numbers_tree.pre_order_traversal())
print("Post order traversal:", numbers_tree.post_order_traversal())
numbers_tree.delete(17)
print("In order traversal:", numbers_tree.in_order_traversal())
