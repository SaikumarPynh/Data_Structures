class Stack_implimentaion:
    def __init__(self):
        self.Arr = []
    def push(self,*item):# to pass multiple arguments 
        self.Arr.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.Arr.pop()
        else:
            return "not possinble"
    
    def peek_elelment(self):
        if not self.is_empty():
            return self.Arr[-1]
    
    def is_empty(self):
        return len(self.Arr) == 0

o = Stack_implimentaion()
while True:
    ch = int(input("enter your choice"))

    if ch  == 1:
        ele = input("enter the element to be ppushed").split()# incase of passing multiple arguments
        o.push(ele)
    elif ch == 2:
        o.pop()
    elif ch == 3:
        temp = o.peek_elelment()
        print(temp)
    else:
        print("enter a valid option")







