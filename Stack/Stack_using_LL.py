class Node:
    def __init__(self,x):
        self.x = x
        self.next = None #whenever new node created it will be the last node no pointer to next node
    
class Stack:
    def __init__(self):
        self.top = None

    def push(self,data):
        if self.top == None:
            new  = Node(data)
            self.top = new

        else:
            new = Node(data)
            self.top.next = new
            self.top = new
        
    def pop(self):
        if self.top == None:    # if stack is empty
            print("Stack is empty:")  
        elif self.top.next == None:  # if stack is having only one element
            self.top = None
        else:                       # if stack is having more than one element
            temp = self.top
            self.top = self.top.next
            temp = None

    def peek(self):
        if self.top == None:    # if stack is empty
            print("Stack is empty:")
        else:
            return self.top.x
    
    def is_empty(self):
        if self.top:
            return False
    
    def display(self):
        if self.top == None:    # if stack is empty
            print("Stack is empty:")  
        else:
            temp = self.top
            while temp is not None:
                print(temp.x)
                temp = temp.next
    


obj = Stack()
        
while True:
    print("1.push\n2.pop\n3.peek\n4.is_empty\n5.Display")
    choice = int(input("enter the choice:"))
    if choice == 1:
        item = int(input("enter the element to be push:"))
        obj.push(item)
    elif choice == 2:
        obj.pop()
    elif choice == 3:
        peek_ele = obj.peek()
        print("peek element is :",peek_ele)
    elif choice == 4:
        result = obj.is_empty()
        print(result)
    elif choice == 5:
        obj.display()
    
    else:
        print("invalid choice:")
        break
    