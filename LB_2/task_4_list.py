class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DequeLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return not self.front

    def add_front(self, value):
        new_node = Node(value)
        if not self.front:
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node

    def add_rear(self, value):
        new_node = Node(value)
        if not self.rear:
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node

    def remove_front(self):
        if self.is_empty():
            print("Deque is empty")
            return
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None

    def remove_rear(self):
        if self.is_empty():
            print("Deque is empty")
            return
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None

    def get_front(self):
        if self.is_empty():
            print("Deque is empty")
            return None
        return self.front.value

    def get_rear(self):
        if self.is_empty():
            print("Deque is empty")
            return None
        return self.rear.value

# Приклад використання
if __name__ == "__main__":
    deque = DequeLinkedList()
    deque.add_front(1)
    deque.add_rear(2)
    deque.add_front(3)
    deque.add_rear(4)
    print(deque.get_front())
    print(deque.get_rear())
    deque.remove_front()
    deque.remove_rear()
    print(deque.get_front())
    print(deque.get_rear())
