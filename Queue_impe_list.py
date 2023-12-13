# from collections import deq
# class Queue:
#     def __init__(self):
list = [ ]
class Queue:
    def __init__(self):
        self.data = None

    def enqueue(self,data):
        list.insert(0,data)
    def is_empty(self):
        return len(list) == 0
    def dequeue(self):
        if not self.is_empty():
            list.pop()
    def peek(self):
        return list[-1]



l = Queue()
l.enqueue(12)
l.enqueue(14)
l.enqueue(15)
l.dequeue()
print("peek element is",l.peek())
