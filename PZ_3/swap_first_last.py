class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def swap_first_last(head):
    if head is None or head.next is None:
        return head

    first = head
    last = head
    while last.next is not None:
        last = last.next

    # Swap first and last nodes
    if first.next == last:  # Only two elements in the list
        first.next = last.next
        last.prev = first.prev
        last.next = first
        first.prev = last
        first.next = None
        if last.prev is not None:
            last.prev.next = last
        head = last
    else:
        if first.next:
            first.next.prev = last
        if last.prev:
            last.prev.next = first
        first.next, last.next = last.next, first.next
        first.prev, last.prev = last.prev, first.prev
        if first.prev is None:
            head = last
        if last.next is None:
            last.next = None
        else:
            first.next.prev = first

    return head

# Приклад використання:
head = DoublyNode(1)
second = DoublyNode(2)
third = DoublyNode(3)
head.next = second
second.prev = head
second.next = third
third.prev = second
head = swap_first_last(head)

# Перевірка результату:
current = head
while current:
    print(current.data, end=" ")
    current = current.next
# Output: 3 2 1
