


n=int(input("Enter the range of the list:- "))

list=[]

while n!=0:
    x=input("Enter Any Element:- ")
    if x not in list:
        list.append(x)
    else:
        print("The Element Is Present")
        n+=1
    n-=1
print("\nThe List Is:- ")    
print(list)