#program to convert centrigrade temperature into fahrenheit and vice versa

temperature=int(input("Enter any temperature: "))

fahrenheit=(temperature*(9/5))+32
centrigrade=(temperature - 32)*5/9


print("centrigrade to fahrenheit = %d"%fahrenheit)

print("fahrenheit to centigrade = %.4f"%centrigrade)