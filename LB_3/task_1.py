class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.key)
        inorder_traversal(root.right)

def search(root, key):
    if root is None or root.key == key:
        return root
    if root.key < key:
        return search(root.right, key)
    return search(root.left, key)

# Приклад використання
root = None
keys = [5, 3, 7, 2, 4, 6, 8]
for key in keys:
    root = insert(root, key)

print("Inorder traversal:")
inorder_traversal(root)

search_key = 4
if search(root, search_key):
    print(f"Key {search_key} found in the tree.")
else:
    print(f"Key {search_key} not found in the tree.")
