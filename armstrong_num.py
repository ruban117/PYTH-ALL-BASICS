#Write a program to display all 3 digited Armstrong numbers.
for i in range(100,999):
   sum = 0
   temp = i
   while temp > 0:
      digits = temp %10
      sum += digits ** 3
      temp //= 10
   if i == sum:
      print(i)