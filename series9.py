#Find the sum of the following series:  X - X^2/3! + X^3/5! - X^4/7! +.... upto n terms. 

n=int(input("Enter the range of the series: "))
x=int(input("Enter the number: "))

def facto(n):
    if n == 0 or n == 1:
        return 1
    else :
        return n*facto(n-1)
    
c=1
sum=0
for i in range(1,n+1):
    if i%2==0:
        sum-=x**i/facto(c)
    else:
        sum+=x**i/facto(c)
    c+=2

print(sum)