# Write a program in python to create a list of unique names. Program should generate appropriate message for duplicate inputs.

n=int(input("Enter the range of the list: "))

list=[]
duplicates=[]
unique=[]
for i in range(n):
    x=input("Enter Any Name: ")
    list.append(x)
print("The All items are: ",list)

for i in list:
    if i not in unique:
        unique.append(i)
    else:
        duplicates.append(i)

print("The Duplicate Elements are: ",duplicates)
print("The Unique Elements are: ",unique)