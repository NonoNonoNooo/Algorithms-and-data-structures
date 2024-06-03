class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularQueueLinkedList:
    def __init__(self):
        self.head = None

    def enqueue(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def dequeue(self):
        if not self.head:
            print("Queue is empty")
            return
        elif self.head.next == self.head:
            self.head = None
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next

    def display(self):
        if not self.head:
            print("Queue is empty")
            return
        current = self.head
        while True:
            print(current.value, end=" ")
            current = current.next
            if current == self.head:
                break
        print()

# Приклад використання
if __name__ == "__main__":
    cq = CircularQueueLinkedList()
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    cq.enqueue(4)
    cq.enqueue(5)
    cq.display()
    cq.dequeue()
    cq.dequeue()
    cq.display()
