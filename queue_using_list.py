# Write a menu driven program to implement Queue using liqe.

def create_Queue():
    Queue=[]
    return Queue

def IsEmpty(Queue):
    if Queue == []:
       return True
    else:
        return False
    
def Enqueue(item,Queue):
    Queue.append(item)

def Dequeue(Queue):
    if IsEmpty(Queue):
        return "Underflow Occur"
    else:
        return Queue.pop(0)
    
def Peek(Queue):
    if IsEmpty(Queue):
        return "Underflow Occur"
    else:
        return Queue[0]

def Display(Queue):
   if IsEmpty(Queue):
        print("Underflow Occur")
   for i in range(len(Queue)):
       print(Queue[i],end="|")

qe=create_Queue()
while (1):
    print("\nEnter 1 to Enqueue elements into the Queue")
    print("Enter 2 to Dequeue elements from the Queue")
    print("Enter 3 to PEEK element from the Queue")
    print("Enter 4 to display element from the Queue")
    print("Enter 5 to Stop:- ")

    a = int(input("Choose 1 or 2 or 3 or 4:- "))
    if a == 1:
        x = int(input("Enter Number: "))
        Enqueue(x,qe)
    elif a == 2:
        print(Dequeue(qe))
    elif a == 3:
        print(Peek(qe))
    elif a == 4:
       Display(qe)
    elif a == 5:
        print("Goodbye")
        break
    else:
        print("Wrong Input")