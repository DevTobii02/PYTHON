print("Welcome To Osun State University Hostel Generating Portal")
class HostelManagement:
    def __init__(self, FirstName, LastName, Age, Gender, MatricNo, Level, CourseOfStudy, Tribe, Religion, HostelName, RoomNumber) -> None:
        self.FirstName  = FirstName
        self.LastName = LastName
        self.Age = Age
        self.Gender = Gender
        self.MatricNo = MatricNo
        self.Level = Level 
        self.CourseOfStudy = CourseOfStudy
        self.Tribe = Tribe
        self.Religion = Religion
        self.HostelName = HostelName
        self.RoomNumber = RoomNumber
        self.Email =  LastName  + FirstName  + '.' + "Uniosun.edu.ng"
import datetime
date = datetime.datetime.now()
print(date)        
class FirstName(HostelManagement):
    def __init__(self, FirstName, Age, Gender, MatricNo, Level, CourseOfStudy, Tribe, Religion, HostelName, ) -> None:
        super().__init__(FirstName, Age, Gender, MatricNo, Level, CourseOfStudy, Tribe, Religion, HostelName) 
        self.FirstName = FirstName
FirstName = input("Enter Your First Name: ")
class LastName(HostelManagement):
    def __init__(self, FirstName, LastName, Age, Gender, MatricNo, Level, CourseOfStudy, Tribe, Religion, HostelName, RoomNumber) -> None:
        super().__init__(FirstName, LastName, Age, Gender, MatricNo, Level, CourseOfStudy, Tribe, Religion, HostelName, RoomNumber)
        self.LastName = LastName
LastName = input("Enter Your Last Name: ")        
class Age(HostelManagement):
    def __init__(self, Name, Age, Gender, MatricNo, Level, CourseOfStudy, Tribe, Religion, HostelName) -> None:
        super().__init__(Name, Age, Gender, MatricNo, Level, CourseOfStudy, Tribe, Religion, HostelName)
        self.Age = Age
Age = int(input("Enter Your Age: "))
class Gender(HostelManagement):
    def __init__(self, Name, Age, Gender, MatricNo, Level, CourseOfStudy, Tribe, Religion, HostelName) -> None:
        super().__init__(Name, Age, Gender, MatricNo, Level, CourseOfStudy, Tribe, Religion, HostelName) 
        self.Gender = Gender
Gender = input("Enter Your Gender: ") 
class MatricNo(HostelManagement):
    def __init__(self, Name, Age, Gender, MatricNo, Level, CourseOfStudy, Tribe, Religion, HostelName) -> None:
        super().__init__(Name, Age, Gender, MatricNo, Level, CourseOfStudy, Tribe, Religion, HostelName) 
        self.MatricNo  = MatricNo
MatricNo = input("Enter Your Matric Number: ")
class Level(HostelManagement):
    def __init__(self, Name, Age, Gender, MatricNo, Level, CourseOfStudy, Tribe, Religion, HostelName) -> None:
        super().__init__(Name, Age, Gender, MatricNo, Level, CourseOfStudy, Tribe, Religion, HostelName) 
        self.Level = Level
Level = [100, 700]
Level = int(input("Enter Your Level: "))
class CourseOfStudy(HostelManagement):
    def __init__(self, Name, Age, Gender, MatricNo, Level, CourseOfStudy, Tribe, Religion, HostelName) -> None:
        super().__init__(Name, Age, Gender, MatricNo, Level, CourseOfStudy, Tribe, Religion, HostelName)   
        self.CourseOfStudy = CourseOfStudy
CourseOfStudy = input("Enter Your Course: ")
class Tribe(HostelManagement):
    def __init__(self, Name, Age, Gender, MatricNo, Level, CourseOfStudy, Tribe, Religion, HostelName) -> None:
        super().__init__(Name, Age, Gender, MatricNo, Level, CourseOfStudy, Tribe, Religion, HostelName)
        self.Tribe = Tribe
Tribe = input("Enter Your Tribe: ")
class Religion(HostelManagement):
    def __init__(self, Name, Age, Gender, MatricNo, Level, CourseOfStudy, Tribe, Religion, HostelName) -> None:
        super().__init__(Name, Age, Gender, MatricNo, Level, CourseOfStudy, Tribe, Religion, HostelName)   
        self.Religion = Religion 
Religion = input("Enter Your Religion: ")
import random
class HostelName(HostelManagement):
    def __init__(self, Name, Age, Gender, MatricNo, Level, CourseOfStudy, Tribe, Religion, HostelName, MaleHostels, FemaleHostels) -> None:
        super().__init__(Name, Age, Gender, MatricNo, Level, CourseOfStudy, Tribe, Religion, HostelName)            
        self.MaleHostels = MaleHostels
        self.FemaleHostels = FemaleHostels
MaleHostels = ["WellSpring", "Olayanju", "Awolowo", "Angola"] 
FemaleHostels = ["Ataoja", "Amurite", "304", "Moremi", "Mozambique"] 
if Gender == "Male":
    print("Hostel Name: ", random.choice(MaleHostels))
elif Gender == "Female":
    print("Hostel Name: ", random.choice(FemaleHostels))    
class RoomNumber(HostelManagement):
    def __init__(self, Name, Age, Gender, MatricNo, Level, CourseOfStudy, Tribe, Religion, HostelName, RoomNumber) -> None:
        super().__init__(Name, Age, Gender, MatricNo, Level, CourseOfStudy, Tribe, Religion, HostelName, RoomNumber) 
        self.RoomNumber = RoomNumber
RoomNumber = random.randint(1, 101)
print("Room Number: ", RoomNumber)           
class Email(HostelManagement):
    def __init__(self, Name, Age, Gender, MatricNo, Level, CourseOfStudy, Tribe, Religion, HostelName) -> None:
        super().__init__(Name, Age, Gender, MatricNo, Level, CourseOfStudy, Tribe, Religion, HostelName)
        self.Email = Email
Email =  LastName  + FirstName + "@Uniosun.edu.ng"
print(Email)
print(date)


def more_num(A, B = 7, C = 10):
    print("a is ", A, "and b is ", B, "While c is ",  C)
    more_num(3, 7)
    more_num(23, c = 17)
    more_num(c = 40, a = 80)    



#print("Hostel Name: ", random.choice(FemaleHostels))  