# Write a program to find the partial abbreviation of a name. (Ex: Ram Kumar Sharma => R.K.Sharma)
import string
name=input("Enter Any Name:- ").split()
new_name=[]
print("Original Name Is:- ")
for i in range(len(name)):
    print(name[i],end=" ")
print("\nAbbreviated Name Is:- ") 
for x in name:
    new_name.append(x[0].upper())
new_name.remove(new_name[-1])

for i in range(len(new_name)):
    print(new_name[i],end=".")
print(name[-1].title())