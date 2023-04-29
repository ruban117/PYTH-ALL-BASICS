#Write a program to count the occurrence of each word in a string

word=input("Enter any string:- ").split()
for i in range(len(word)):
    count=0
    for j in word:
        if word[i]==j:
            count+=1
    print(word[i] ,"=",count)