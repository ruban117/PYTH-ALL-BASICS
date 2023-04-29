#write a program in python to implement binary search

def BinarySearch(list,key,n):
    beg=0
    end=n-1
    mid=(beg+end)//2
    while((beg<=end)and(list[mid]!=key)):
        if key <list[mid]:
            end=mid-1
        else:
            beg=mid+1
        mid=(beg+end)//2
    if beg>end:
        return -1
    else:
        return mid


list=[]
n=int(input("Enter the range of the list:- "))
for i in range(n):
    print("Enter list[",i+1,"]",end=" ")
    x=int(input())
    list.append(x)

print("The List Is:- ",list)
key=int(input("Enter the element you want to search= "))
y=BinarySearch(list,key,n)

if y == -1:
    print("The element is not found")
else:
    print("The element is found at the position= ",y)