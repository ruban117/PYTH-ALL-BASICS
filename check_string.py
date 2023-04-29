#write a program to count how many numbers of vowels consonents digits and punctuation marks in a given string
import string
word=input("Enter any string:- ")

v=c=d=p=0

for i in word:
    i=i.upper()
    if i in 'AEIOU':
        v+=1
    elif i in string.ascii_letters:
        c+=1
    elif i in string.digits:
        d+=1
    elif i in string.punctuation:
        p+=1

print(f"Vowels = {v}\nConsonents = {c}\nDigits = {d}\n Punctuation Marks = {p}")