# python program to print student result using dictionary

def input_dictionary(my_dict):
    sum = 0
    Student_roll = int(input("Enter The Roll Of Student:- "))
    my_dict[Student_roll] = {}
    stu_name=input("Enter The Name Of The Student:- ")
    Dept_Name = input("Enter The Name Of The Department:- ")
    n = int(input("How many Subjects?:- "))
    for i in range(n):
        sub = input(f"Enter The subject {i} Name:- ")
        mark = int(input(f"Enter Mark Of {sub}:- "))
        sum += mark
        my_dict[Student_roll]['Student Name']=stu_name
        my_dict[Student_roll]['Dept_Name'] = Dept_Name
        my_dict[Student_roll][sub] = mark
        my_dict[Student_roll]['All Total'] = sum
        my_dict[Student_roll]['Average Mark'] = sum/n


def Print_Dict(my_dict):
    print(my_dict)

def search(my_dict,roll):
    if roll in my_dict:
        print(my_dict[roll])
    else:
        print("\nNOT FOUND")

my_dict = {}
while 1:
   print("Press 1 to add values:- ")
   print("Press 2 to display :- ")
   print("Press 3 to search and display student record:- ")
   a= int(input("Enter Your Choice:- "))
   if a == 1:
       input_dictionary(my_dict)
   elif a == 2:
       Print_Dict(my_dict)
   elif a == 3:
       roll=int(input("Enter The Student Details You Want To Search According To Roll Number:- "))
       search(my_dict,roll) 

