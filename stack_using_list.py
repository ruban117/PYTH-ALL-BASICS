# Write a menu driven program to implement Stack using list.

def create_stack():
    stack=[]
    return stack

def IsEmpty(stack):
    if stack == []:
       return True
    else:
        return False
    
def Push(item,stack):
    stack.append(item)

def Pop(stack):
    if IsEmpty(stack):
        return "Underflow Occur"
    else:
        return stack.pop()
    
def Peek(stack):
    if IsEmpty(stack):
        return "Underflow Occur"
    else:
        return stack[-1]

def Display(stack):
   if IsEmpty(stack):
        print("Underflow Occur")
   else:
    print(stack[::-1])

st=create_stack()
while (1):
    print("Enter 1 to PUSH elements into the stack")
    print("Enter 2 to POP elements from the stack")
    print("Enter 3 to PEEK element from the stack")
    print("Enter 4 to display element from the stack")
    print("Enter 5 to stop:- ")

    a = int(input("Choose 1 or 2 or 3 or 4:- "))
    if a == 1:
        x = int(input("Enter Number: "))
        Push(x,st)
    elif a == 2:
        print(Pop(st))
    elif a == 3:
        print(Peek(st))
    elif a == 4:
       Display(st)
    elif a == 5:
        print("Goodbye")
        break
    else:
        print("Wrong Input")