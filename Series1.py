#print the following series with it's sum 1-3+5-7+9............N

n=int(input("Enter the number of terms: "))

sum=0
count=1

for i in range(1,n+1):
    print(count,"")
    if i%2==0:
        print("+","")
        sum-=count
    else:
        print("-","")
        sum+=count
    count+=2
print(sum)