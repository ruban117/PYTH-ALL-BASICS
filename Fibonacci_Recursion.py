#Write recursive Function for Find n-th fibonacci number. 

def fibonacci(num):
    if num<=1:
        return num
    else:
        return (fibonacci(num-1)+fibonacci(num-2))
    

num=int(input("Enter the range:- "))
print(f"The fibonacci number of {num} is {fibonacci(num)}")

