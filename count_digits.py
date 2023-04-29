#Write a  program to count the digits of a number.

num=int(input("Enter any number: "))

c=0

while num>=0:
    r=num%10
    c+=1
    num//=10

print(c)