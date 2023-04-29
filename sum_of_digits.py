#Write a program to find the sum of the digits of a number. [ For example,  if the inputted number is 283, output will be 2+8+3=13]

num=int(input("Enter any number: "))
sum=0
while num!=0:
    r=num%10
    sum+=r
    num//=10

print(sum)