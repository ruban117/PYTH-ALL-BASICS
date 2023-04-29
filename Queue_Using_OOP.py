class Queue:
    def __init__(self):
        self.queue=[]
    def IsEmpty(self):
        if self.queue == []:
            return True
        else:
            return False
    
    def Enqueue(self,item):
        self.queue.append(item)

    def Dequeue(self):
        return self.queue.pop(0)
    
    def Peek(self):
        return self.queue[0]
    def Display(self):
        for i in range(len(self.queue)):
            print(self.queue[i],end="|")
obj=Queue()
while (1):
    print("\nEnter 1 to Enqueue elements into the Queue")
    print("Enter 2 to Dequeue elements from the Queue")
    print("Enter 3 to PEEK element from the Queue")
    print("Enter 4 to display element from the Queue")
    print("Enter 5 to Stop:- ")

    a = int(input("Choose 1 or 2 or 3 or 4:- "))
    if a == 1:
        x = int(input("Enter Number: "))
        obj.Enqueue(x)
    elif a == 2:
        if obj.IsEmpty():
            print("Underflow Occurs")
        print(obj.Dequeue())
    elif a == 3:
        if obj.IsEmpty():
            print("Underflow Occurs")
        print(obj.Peek())
    elif a == 4:
       if obj.IsEmpty():
            print("Underflow Occurs")
       obj.Display()
    elif a == 5:
        print("Goodbye")
        break
    else:
        print("Wrong Input")