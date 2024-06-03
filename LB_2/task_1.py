class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_end(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def add_to_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def remove_by_value(self, value):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def swap_nodes(self, value1, value2):
        if value1 == value2:
            return
        prev1 = None
        current1 = self.head
        while current1 and current1.value != value1:
            prev1 = current1
            current1 = current1.next

        prev2 = None
        current2 = self.head
        while current2 and current2.value != value2:
            prev2 = current2
            current2 = current2.next

        if not current1 or not current2:
            return

        if prev1:
            prev1.next = current2
        else:
            self.head = current2

        if prev2:
            prev2.next = current1
        else:
            self.head = current1

        temp = current1.next
        current1.next = current2.next
        current2.next = temp

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=' ')
            current = current.next
        print()

# Приклад використання
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.add_to_end(1)
    linked_list.add_to_end(2)
    linked_list.add_to_end(3)
    linked_list.add_to_end(4)
    linked_list.add_to_end(5)
    linked_list.print_list()

    linked_list.add_to_beginning(0)
    linked_list.print_list()

    linked_list.remove_by_value(3)
    linked_list.print_list()

    print(linked_list.search(4))
    print(linked_list.search(6))

    linked_list.swap_nodes(1, 4)
    linked_list.print_list()
