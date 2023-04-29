#Write a  program to find the sum of the following series: 1+2+4+7+11+16+... upto N terms

n=int(input("Enter the range of the series: "))

c=1
sum=0

for i in range(1,n+1):
    print(c," + ",end="")
    sum+=c
    c+=i
print("\b\b=",sum)
