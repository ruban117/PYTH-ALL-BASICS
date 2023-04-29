# Write functions for- A. Linear search

def Linier_Search(list, key):
    for i in range(len(list)):
        if list[i] == key:
            return i
    return -1


n = int(input("Enter the range of the list:- "))
list = []
for i in range(n):
    x = int(input("Enter any number:- "))
    list.append(x)

print("The List Is:- ", list)

key = int(input("Enter the element you want to search:- "))
y = Linier_Search(list, key)
if y < 0:
    print("Not Found")
else:
    print("The Element is found at the position:- ", y)
