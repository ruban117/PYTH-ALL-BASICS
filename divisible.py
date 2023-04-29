#Write a program to display all 3 digited numbers which are divisible by 3 but not divisible by 9.

for i in range(100,999):
    if i % 3 == 0 and i % 9 !=0:
        print(i,end=" ")