#write a program to sort a list using selection sort by using function

def Selection_Sort(list,n):
    for i in range(n-1):
        min=list[i]
        pos=i
        for j in range(i+1,n):
            if list[j]<min:
                min=list[j]
                pos=j
        if pos!=j:
            temp=list[i]
            list[i]=list[pos]
            list[pos]=temp
    Print_List(list)

def Print_List(list):
    print("The List Is After Sorted:- ",list)

list=[]
n=int(input("Enter the range of the list:- "))
for i in range(n):
    print("Enter List[",i+1,"]",end=":")
    x=int(input())
    list.append(x)

print("The List Is Before Sorted:- ",list)

Selection_Sort(list,n)