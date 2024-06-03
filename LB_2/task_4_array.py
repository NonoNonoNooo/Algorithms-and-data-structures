class DequeArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def add_front(self, value):
        if self.is_full():
            print("Deque is full")
            return
        self.front = (self.front - 1) % self.capacity
        self.queue[self.front] = value
        self.size += 1

    def add_rear(self, value):
        if self.is_full():
            print("Deque is full")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1

    def remove_front(self):
        if self.is_empty():
            print("Deque is empty")
            return
        self.front = (self.front + 1) % self.capacity
        self.size -= 1

    def remove_rear(self):
        if self.is_empty():
            print("Deque is empty")
            return
        self.rear = (self.rear - 1) % self.capacity
        self.size -= 1

    def get_front(self):
        if self.is_empty():
            print("Deque is empty")
            return None
        return self.queue[self.front]

    def get_rear(self):
        if self.is_empty():
            print("Deque is empty")
            return None
        return self.queue[self.rear]

# Приклад використання
if __name__ == "__main__":
    deque = DequeArray(5)
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
