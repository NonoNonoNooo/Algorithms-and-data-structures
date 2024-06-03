class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def print_leaves(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        print(root.val)
    print_leaves(root.left)
    print_leaves(root.right)

def print_internal_nodes(root):
    if root is None:
        return
    if root.left is not None or root.right is not None:
        print(root.val)
    print_internal_nodes(root.left)
    print_internal_nodes(root.right)

def print_nodes_with_left_child(root):
    if root is None:
        return
    if root.left is not None and root.right is None:
        print(root.val)
    print_nodes_with_left_child(root.left)
    print_nodes_with_left_child(root.right)

def print_nodes_with_right_child(root):
    if root is None:
        return
    if root.left is None and root.right is not None:
        print(root.val)
    print_nodes_with_right_child(root.left)
    print_nodes_with_right_child(root.right)

def get_min_depth(node):
    if node is None:
        return 0
    left_depth = get_min_depth(node.left)
    right_depth = get_min_depth(node.right)
    return 1 + min(left_depth, right_depth)

def get_max_depth(node):
    if node is None:
        return 0
    left_depth = get_max_depth(node.left)
    right_depth = get_max_depth(node.right)
    return 1 + max(left_depth, right_depth)

def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def count_leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)

def count_internal_nodes(node):
    if node is None or (node.left is None and node.right is None):
        return 0
    return 1 + count_internal_nodes(node.left) + count_internal_nodes(node.right)

def count_nodes_with_two_children(node):
    if node is None:
        return 0
    if node.left is not None and node.right is not None:
        return 1 + count_nodes_with_two_children(node.left) + count_nodes_with_two_children(node.right)
    return count_nodes_with_two_children(node.left) + count_nodes_with_two_children(node.right)

def count_nodes_with_one_child(node):
    if node is None:
        return 0
    if (node.left is None and node.right is not None) or (node.left is not None and node.right is None):
        return 1 + count_nodes_with_one_child(node.left) + count_nodes_with_one_child(node.right)
    return count_nodes_with_one_child(node.left) + count_nodes_with_one_child(node.right)

def count_nodes_with_left_child(node):
    if node is None:
        return 0
    if node.left is not None and node.right is None:
        return 1 + count_nodes_with_left_child(node.left) + count_nodes_with_left_child(node.right)
    return count_nodes_with_left_child(node.left) + count_nodes_with_left_child(node.right)

def count_nodes_with_right_child(node):
    if node is None:
        return 0
    if node.left is None and node.right is not None:
        return 1 + count_nodes_with_right_child(node.left) + count_nodes_with_right_child(node.right)
    return count_nodes_with_right_child(node.left) + count_nodes_with_right_child(node.right)

def average_key(node):
    if node is None:
        return 0, 0
    sum_keys_left, count_keys_left = average_key(node.left)
    sum_keys_right, count_keys_right = average_key(node.right)
    return node.val + sum_keys_left + sum_keys_right, 1 + count_keys_left + count_keys_right

def tree_height(node):
    if node is None:
        return 0
    left_height = tree_height(node.left)
    right_height = tree_height(node.right)
    return 1 + max(left_height, right_height)

def inorder_successor(root, key):
    successor = None
    while root:
        if root.val > key:
            successor = root
            root = root.left
        else:
            root = root.right
    return successor

def inorder_predecessor(root, key):
    predecessor = None
    while root:
        if root.val < key:
            predecessor = root
            root = root.right
        else:
            root = root.left
    return predecessor

def delete_node(root, key):
    if root is None:
        return root
    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        root.val = min_value_node(root.right).val
        root.right = delete_node(root.right, root.val)
    return root

def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[i] < arr[l]:
            largest = l
        if r < n and arr[largest] < arr[r]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr





# Створення дерева
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(18)

# Виведення ключів листів
print("Keys of leaf nodes:")
print_leaves(root)

# Виведення ключів внутрішніх вузлів
print("\nKeys of internal nodes:")
print_internal_nodes(root)

# Виведення ключів вузлів з лівим сином
print("\nKeys of nodes with left child:")
print_nodes_with_left_child(root)

# Виведення ключів вузлів з правим сином
print("\nKeys of nodes with right child:")
print_nodes_with_right_child(root)

# Знайти глибину мінімального елемента
print("\nMinimum depth of tree:")
print(get_min_depth(root))

# Знайти глибину максимального елемента
print("\nMaximum depth of tree:")
print(get_max_depth(root))

# Кількість елементів в дереві
print("\nNumber of nodes in tree:")
print(count_nodes(root))

# Кількість листя в дереві
print("\nNumber of leaf nodes in tree:")
print(count_leaves(root))

# Кількість внутрішніх вузлів в дереві
print("\nNumber of internal nodes in tree:")
print(count_internal_nodes(root))

# Кількість вузлів, у яких два сини
print("\nNumber of nodes with two children in tree:")
print(count_nodes_with_two_children(root))

# Кількість вузлів, у яких один син
print("\nNumber of nodes with one child in tree:")
print(count_nodes_with_one_child(root))

# Кількість вузлів, у яких є лівий син
print("\nNumber of nodes with left child in tree:")
print(count_nodes_with_left_child(root))

# Кількість вузлів, у яких є правий син
print("\nNumber of nodes with right child in tree:")
print(count_nodes_with_right_child(root))

# Середнє арифметичне всіх ключів
sum_keys, count_keys = average_key(root)
print("\nAverage key value in tree:")
print(sum_keys / count_keys)

# Висота дерева
print("\nHeight of tree:")
print(tree_height(root))

# Знайти елемент, наступний за даним
key = 7
successor = inorder_successor(root, key)
print(f"\nInorder successor of {key}:")
print(successor.val if successor else "None")

# Знайти елемент, що передує даному
predecessor = inorder_predecessor(root, key)
print(f"\nInorder predecessor of {key}:")
print(predecessor.val if predecessor else "None")

# Видалити елемент із заданим ключем
key_to_delete = 5
root = delete_node(root, key_to_delete)
print(f"\nTree after deleting node with key {key_to_delete}:")
print_inorder(root)

# Відсортувати масив, використовуючи проміжне представлення у вигляді двійкової купи
arr = [4, 10, 3, 5, 1]
print("\nSorted array using heap sort:")
print(heap_sort(arr))
