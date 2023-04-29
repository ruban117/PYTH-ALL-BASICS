#Write a program to display the following series upto N number of terms: 1  10  101  1010  10101....

n = int(input("Enter number of lines of pattern: "))

for i in range(1,n+1):
    for j in range(1, i+1):
        print(j%2, end="")  #1+
    print(end=" ")