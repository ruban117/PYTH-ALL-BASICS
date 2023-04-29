#Write recursive Function for Find a^b ( equivalent to pow() )

def pow(b,e):
    if e == 0:
        return 1
    else :
        return (b * pow(b,e-1))


base=int(input("Enter the base value:- "))
exp=int(input("Enter the exponent value:- "))

print(f"The {base}^{exp}={pow(base,exp)}")
