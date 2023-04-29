#print the following series with it's sum 1!+3!+5!+7!+9!............N

n=int(input("Enter the number of terms: "))

c=1
sum=0
def facto(n):
    if n==0 or n==1:
        return 1
    else:
        return n*facto(n-1)

for i in range(1,n+1):
    sum+=facto(c)
    c+=2
print(sum)