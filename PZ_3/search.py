class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def search(head, key):
    current = head
    while current is not None:
        if current.data == key:
            return True
        current = current.next
    return False

# Приклад використання:
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
key = 2
print(f"Element {key} found:", search(head, key))  # Output: True
