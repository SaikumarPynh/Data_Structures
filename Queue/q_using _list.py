def enqueue(item):
    Queue.append(item)
    print("element added to queue")
def dequeue():
    if len(Queue) >= 1:
        removed_item = Queue.pop(0)
        print("rempved item is:",removed_item)
    else:
        print("queue is empty")

def peek():
    if len(Queue) >= 1:
        print("peek element is:",Queue[-1])
    else:
        print("queue is empty:")

def isempty():
    if len(Queue) >= 1:
        print("Queue is empty")
    else:
        print("queue is not empty:")

def display():
    for i in Queue:
        print(i)
    





#driver 
Queue = []
while True:
    print("1.enqueue\n2.dequeue\n3.peek\n4.isempty\n5.display")
    choice = int(input("enter youe choice"))
    if choice == 1:
        item = int(input("enter the item to be add:"))
        enqueue(item)
    elif choice == 2:
        dequeue()

    elif choice == 3:
        peek()
    
    elif choice == 4:
        isempty()
    
    elif choice == 5:
        display()
    else:
        print("enter a valid choice")
    
