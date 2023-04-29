#Write a program in python to spilt a list into odd and even two different list.

n=int(input("Enter the range of the list: "))

list1=[]
list_odd=[]
list_even=[]
for i in range(n):
    x=int(input("Enter any number: "))
    list1.append(x)
    if list1[i] % 2 == 0:
        list_even.append(list1[i])
    else :
        list_odd.append(list1[i])

print("The Original List Is : ",list1)
print("The Even List Is : ",list_even)
print("The Odd List Is : ",list_odd)
