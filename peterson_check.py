#krishnamurti Number
#[147=1!+4!+7!=147]
def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
def peterson(n):
    c=0
    temp=n
    while n>0:
        r=n%10      
        c+=fact(r)
        n//=10 
    if c==temp:
        print("peterson number")
    else:
        print("Not a peterson number")
n=int(input("Enter a number : "))
peterson(n) 