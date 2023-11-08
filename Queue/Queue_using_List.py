class Queue:
    def __init__(self, max_size):
        self.r = -1
        self.f = -1
        self.list = []
        self.max_size = max_size

    def enqueue(self, element):
        if self.r == self.max_size - 1:
            print("Overflow")
        else:
            if self.f == -1:
                self.f = 0
            self.r += 1
            self.list.append(element)


    def dequeue(self):
        if self.f == -1 or self.f > self.r:
            print("Underflow")
        else:
            ele = self.list.pop(0)  # Remove the first element
            self.f += 1
            if self.r < self.f:
                self.r = self.f = -1
            print("Element is dequeued")

    def peek(self):
        if self.r == -1:
            print("Queue is empty")
        else:
            print("Peek of queue is:", self.list[self.r])

    def display(self):
        if self.f == -1:
            print("Queue is empty")
        else:
            for i in range(self.f, self.r + 1):
                print(self.list[i])

    def is_empty(self):
        if self.f == -1:
            print("Queue is empty")

# Driver code
obj = Queue(5)
while True:
    print("1. Enqueue\n2. Dequeue\n3. Peek\n4. Is Empty\n5. Display")
    choice = int(input("Enter the choice:"))
    if choice == 1:
        item = int(input("Enter the element to be enqueued:"))
        obj.enqueue(item)
    elif choice == 2:
        obj.dequeue()
    elif choice == 3:
        obj.peek()
    elif choice == 4:
        obj.is_empty()
    elif choice == 5:
        obj.display()
    else:
        print("Invalid choice")
        break
