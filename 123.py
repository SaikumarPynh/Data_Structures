class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    
    def is_empty(self):
        return self.size == 0
    
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
        print("node inserted successfully")
    
    def pop(self):
        if not self.is_empty():
            data = self.top.data
            top = self.top.next
            self.size -= 1
            return data
        else:
            return None
    
    def peek(self):
        if not self.is_empty():
            return self.top.data
        else:
            return None
    
s = Stack()
while True:
    ch = input("enter your choice:")
    if ch == '1' or ch == "push":
        ele = input("enter the value to be inserted")
        s.push(ele)
    elif ch == 2 or ch == "pop":
        print(s.pop)
    elif ch == 3 or ch == "peek":
        print(s.peek())
    else:
        print("enter a valid choice")
    

      