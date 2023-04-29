#write a program to implement modified bubble sort by using function

def Bubble_Sort(list,n):
    for i in range(n-1):
        flag=True
        for j in range(n-i-1):
            if list[j]>list[j+1]:
                flag=False
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
        if flag == True:
            break
    printlist(list)

def printlist(list):
    print("The List Is After Sorted:- ",list)

list=[]
n=int(input("Enter the range of the list:- "))
for i in range(n):
    print("Enter List[",i+1,"]",end=":")
    x=int(input())
    list.append(x)

print("The List Is Before Sorted:- ",list)

Bubble_Sort(list,n)