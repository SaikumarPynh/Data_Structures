class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class Queue:
    def __init__(self):
        self.F = None
        self.R = None
        

    def enqueue(self,data):
        new = Node(data)
        if self.F == None:
            self.F = new
            self.R = new
        else:
            self.R.next = new
            self.R = new
    def dequeue(self):
        if self.F == None:
            print("Queue is empty")
        elif self.F.next == None:
            self.F = None
        else:
            temp = self.R
            self.F = self.F.next 
            temp = None
    def display(self): # use temp variable to access the data in each node other wise it will alter the front index
        temp = self.F
        while temp:
            print(temp.data)
            temp  = temp.next
    def peek(self):
        print(self.R.data)
    
    def isempty(self):
        if self.F == None :
            print("Queue is empty")
        else:
            print("Queue is not empty")
    
obj = Queue()
        
while True:
    print("1.push\n2.pop\n3.peek\n4.is_empty\n5.Display")
    choice = int(input("enter the choice:"))
    if choice == 1:
        item = int(input("enter the element to be push:"))
        obj.enqueue(item)
    elif choice == 2:
        obj.dequeue()
    elif choice == 3:
        obj.peek()
    elif choice == 4:
        obj.isempty()
    elif choice == 5:
        obj.display()
    
    else:
        print("invalid choice:")
        break
    


    



