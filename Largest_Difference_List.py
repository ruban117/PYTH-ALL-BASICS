# Write a program in python to find the largest difference between the elements of a list.

n=int(input("Enter the range of the list: "))
list=[]
for i in range(n):
    x=int(input("Enter any number: "))
    list.append(x)
max=list[0]
min=list[0]
for i in range(n):
    if list[i] > max:
        max=list[i]
    if list[i]< min:
        min=list[i]

print("The Created List Is : ",list)

print("The Maximum Difference is: ",max,"-",min,"=",max-min)