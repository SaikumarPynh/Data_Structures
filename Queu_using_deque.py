from collections import deque

class Queue:
    def __init__(self):
        self.deque = deque()  # You need to initialize the deque by calling deque() constructor

    def enqueue(self, data):
        self.deque.appendleft(data)  # Use self.deque to access the deque instance

    def dequeue(self):
        self.deque.pop()  # Use self.deque to access the deque instance

    def peek(self):
        print(self.deque[-1])  # Use self.deque to access the deque instance

obj = Queue()
obj.enqueue(12)
obj.enqueue(13)
obj.enqueue(15)
obj.dequeue()
obj.peek()
