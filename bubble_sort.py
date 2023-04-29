#Write a program in python to implement bubble sort.

n=int(input("Enter the range of the series: "))
list=[]

for i in range(n):
    x=int(input("Enter any number: "))
    list.append(x)

print("The List is (Before Sorted): ",list)

for i in range(n-1):
    for j in range(n-i-1):
        if list[j] > list[j+1] :
            temp=list[j]
            list[j]=list[j+1]
            list[j+1]=temp
print("The List is (After Sorted): ",end="")
print("[",end="")
for i in range(n):
    print(list[i],end=", ")

print("\b\b]")