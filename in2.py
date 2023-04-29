#bubble sort

def Insertion_Sort(lis,n):
    for i in range(1,n):
        temp=lis[i]
        j=i-1
        while((j>=0)and(lis[j]>=temp)):
            lis[j+1]=lis[j]
            j-=1
        lis[j+1]=temp
    Print_List(lis)

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
