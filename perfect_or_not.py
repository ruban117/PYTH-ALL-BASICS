# Write a program to check whether an inputted number is perfect or not. If the sum of the factors (excluding the  number itself) of a number is same as the number, the number is known as Perfect number.
# [Ex: 6=1+2+3, 28=1+2+4+7+14 ]

num=int(input("Enter any number: "))

sum=0

for i in range(1,num):
    if num % i == 0:
        sum+=i
if sum == num:
    print("The number is perfect number")
else:
    print("The number is not perfect number")