class StackArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1

    def is_full(self):
        return self.top == self.capacity - 1

    def is_empty(self):
        return self.top == -1

    def push(self, value):
        if self.is_full():
            print("Stack is full")
            return
        self.top += 1
        self.stack[self.top] = value

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        value = self.stack[self.top]
        self.top -= 1
        return value

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.stack[self.top]

# Приклад використання
if __name__ == "__main__":
    stack = StackArray(5)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.peek())
