#Write a program to display all 3 digited Peterson number.
def facto(n):
    if n == 0 or n == 1:
        return 1
    else :
        return n*facto(n-1)
    
for i in range(100,999):
    sum=0
    temp=i
    while temp > 0:
        r=temp%10
        sum+=facto(r)
        temp//=10
    if i == sum:
        print(i,end="")