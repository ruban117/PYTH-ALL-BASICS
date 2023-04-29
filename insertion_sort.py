#write a program to implement insertion sort by using function

def Insertion_Sort(list,n):
    for i in range(1,n):
        temp=list[i]
        j=i-1
        while((j>=0)and(list[j]>=temp)):
            list[j+1]=list[j]
            j-=1
        list[j+1]=temp
    Print_List(list)

def Print_List(list):
    print("The List Is After Sorted:- ",list)

list=[]
n=int(input("Enter the range of the list:- "))
for i in range(n):
    print("Enter arr[",i+1,"]",end=": ")
    x=int(input())
    list.append(x)
print("The List Is Before Sorted:- ",list)
Insertion_Sort(list,n)
