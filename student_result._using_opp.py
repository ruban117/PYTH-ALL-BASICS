#define a class student containing name,roll,marks for a set of students find the highest marks also print the name of the student

class student:
    def __init__(self,roll,name,tot_marks):
        self.name=name
        self.roll=roll
        self.tot_marks=tot_marks
    def disp(self):
        print("\n")
        print("..................................")
        print("Student Roll Number:- ",self.roll)
        print("Student Name:- ",self.name)
        print("Obtained Marks=",self.tot_marks)
        print("..................................")
        print("\n")

lis=[]
n=int(input("How Many Students:- "))
for i in range(n):
    roll=int(input(f"Enter the roll of student {i+1}:- "))
    name=input(f"Enter the name of the student {i+1}:- ")
    tot_marks=int(input(f"Enter the obtained marks of {name}:- "))
    lis.append(student(roll,name,tot_marks))
print("\nMerit Sheet")
lis.sort(key=lambda x: x.tot_marks , reverse=True)
for i in lis:
    i.disp()