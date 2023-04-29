# Write a  program to find the sum of the following series:1+3²+5³+7⁴+ ... upto N terms.

n=int(input("Enter the range of the series: "))

c=1
p=1
sum=0
for i in range(1,n+1):
    print(c ,"^", p," + ",end="")
    sum+=c**p
    p+=1
    c+=2

print("\b\b= ",sum)
