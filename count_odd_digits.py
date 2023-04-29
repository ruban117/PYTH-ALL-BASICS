#Write a program to count the odd digits in an inputted number.

num=int(input("Enter any number: "))

c=0

while num!=0:
    r=num%10
    if r%2!=0:
        c+=1
    num//=10

print(c)
