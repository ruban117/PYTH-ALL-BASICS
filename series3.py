# Write a  program to display the following series: 5  10  15  20  25  ....... upto N

n=int(input("Enter the range of the series: "))
c=5
for i in range(1,n+1):
    print(c,end=" ")
    c+=5