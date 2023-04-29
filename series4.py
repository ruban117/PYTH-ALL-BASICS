#Write a  program to find the sum of the following series: 2+5+8+11+14+ ........ upto N terms

n=int(input("Enter the range of the series: "))

c=2
sum=0
for i in range(1,n+1):
    print(c," + ",end="")
    sum+=c
    c+=3

print("\b\b=",sum)