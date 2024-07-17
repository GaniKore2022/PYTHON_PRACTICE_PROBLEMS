class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def display(self):
        if self.head is None:
            print("Doubly linked list is empty.")
        else:
            current = self.head
            while current:
                print(current.data, end=" ")
                current = current.next

    def display_reverse(self):
        if self.head is None:
            print("Doubly linked list is empty.")
        else:
            current = self.head
            while current.next:
                current = current.next
            while current:
                print(current.data, end=" ")
                current = current.prev


# Create an instance of the doubly linked list
dll = DoublyLinkedList()

# Dynamic input example
n = int(input("Enter the number of elements: "))
for _ in range(n):
    data = int(input("Enter an element: "))
    dll.insert_at_end(data)

# Display the doubly linked list
print("Doubly linked list:")
dll.display()

# Display the doubly linked list in reverse order
print("\nDoubly linked list in reverse order:")
dll.display_reverse()
