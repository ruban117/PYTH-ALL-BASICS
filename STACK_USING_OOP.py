class stack:
    def __init__(self):
        self.stack=[]
    def Is_Empty(self):
        if self.stack == []:
            return "Stack Underflow"
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def display(self):
        print(self.stack[::-1])

obj=stack()
while (1):
    print("Enter 1 to PUSH elements into the stack")
    print("Enter 2 to POP elements from the stack")
    print("Enter 3 to PEEK element from the stack")
    print("Enter 4 to display element from the stack")
    print("Enter 5 to stop:- ")

    a = int(input("Choose 1 or 2 or 3 or 4:- "))
    if a == 1:
        x = int(input("Enter Number: "))
        obj.push(x)
    elif a == 2:
        print(obj.pop())
    elif a == 3:
        print(obj.peek())
    elif a == 4:
       obj.display()
    elif a == 5:
        print("Goodbye")
        break
    else:
        print("Wrong Input")