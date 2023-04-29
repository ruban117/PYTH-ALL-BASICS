# Write a  program to find the sum of the following series: 1+11+111+1111+.... upto N terms

n=int(input("Enter the range of the series: "))
sum=0
c=1

for i in range(1,n+1):
    print(c,end=" + ")
    sum+=c
    c=(c*10)+1

print("\b\b=",sum)