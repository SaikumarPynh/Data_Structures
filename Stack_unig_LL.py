class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None  # Initialize the top of the stack as None (empty)
        self.size = 0    # Initialize the size of the stack as 0

    def is_empty(self):
        return self.size == 0
    def push(self, data):
        new_node = Node(data)   # Create a new node with the provided data
        new_node.next = self.top  # Set the next of the new node to the current top
        self.top = new_node      # Update the top to the new node
        self.size += 1           # Increment the size of the stack

    def pop(self):
        if not self.is_empty():
            data = self.top.data   # Get the data of the top node
            self.top = self.top.next  # Update the top to the next node
            self.size -= 1           # Decrement the size of the stack
            return data              # Return the popped data
        else:
            return None              # Return None if the stack is empty
    def peek(self):
        if not self.is_empty():
            return self.top.data  # Return the data of the top node
        else:
            return None          # Return None if the stack is empty
    def get_size(self):
        return self.size  # Return the current size of the stack

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Top element:", stack.peek())  # Output: Top element: 3

popped = stack.pop()
print("Popped element:", popped)      # Output: Popped element: 3

print("Size of stack:", stack.get_size())  # Output: Size of stack: 2
