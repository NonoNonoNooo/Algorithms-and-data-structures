class CircularQueueArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def enqueue(self, value):
        if (self.rear + 1) % self.capacity == self.front:
            print("Queue is full")
            return
        elif self.front == -1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
            return
        elif self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity

    def display(self):
        if self.front == -1:
            print("Queue is empty")
            return
        elif self.rear >= self.front:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.front, self.capacity):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

# Приклад використання
if __name__ == "__main__":
    cq = CircularQueueArray(5)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    cq.enqueue(4)
    cq.enqueue(5)
    cq.display()
    cq.dequeue()
    cq.dequeue()
    cq.display()
