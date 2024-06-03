class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return not self.top

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        popped = self.top
        self.top = self.top.next
        return popped.value

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.top.value

# Приклад використання
if __name__ == "__main__":
    stack = StackLinkedList()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.peek())
