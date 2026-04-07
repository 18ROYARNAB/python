class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
def print_inorder(root):
    if root:
        # First recur on left child
        print_inorder(root.left)
        # Then print the data of node
        print(root.val, end=" "),
        # Now recur on right child
        print_inorder(root.right)

# Let's build the tree manually to see the structure
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("In-order traversal of the binary tree is:")
    print_inorder(root)