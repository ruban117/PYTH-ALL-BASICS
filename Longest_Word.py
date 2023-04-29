#Write a program to find the length of the longest word in a string

list=input("Enter Any String:- ").split()
max=0

for x in list:
    if len(x)>max:
        max=len(x)
        name=x

print(f"The Longest length is {max} and the word is{name}")