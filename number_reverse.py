#Write a  program to reverse a number. 

num=int(input("Enter any number: "))

while num!=0:
    r=num%10
    print(r,end="")
    num//=10