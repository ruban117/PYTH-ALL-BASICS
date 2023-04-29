#Write recursive Function for g.c.d of two integers

def GCD(a,b):
    if b == 0:
        return a
    else:
        temp=a%b
        return GCD(b,temp)
a=int(input("Enter the first number:- "))
b=int(input("Enter The second number:- "))

print(f"GCD of {a},{b} is {GCD(a,b)}")
