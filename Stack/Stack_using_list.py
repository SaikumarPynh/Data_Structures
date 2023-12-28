class Stack:
    def __init__(self,max_size):
        self.max_size = max_size
        self.list = []
    def push(self,element):
        if len(self.list) == self.max_size:
            return "stack overflow"
        else:
            self.list.append(element)
            print("element pushed into stack")
    def pop(self):
        if len(self.list) <= 0:
            return "Stack Underflow"
        else:
            ele = self.list.pop()
            print("element ",ele,"deleted from stack")
    def peek(self):
        if len(self.list) <= 0:
            return "Stack Underflow"
        return self.list[-1]
    
    def is_empty(self):
        return len(self.list) == 0
    def Display(self):
        for i in self.list:
            print(i)
obj = Stack(5)
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
        obj.Display()
    
    else:
        print("invalid choice:")
        break
    