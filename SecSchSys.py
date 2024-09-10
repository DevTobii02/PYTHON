print("Welcome To KingsField College")
class Senior_Secondary_School:
    def __init__(self, Department, Teachers, Name, Students, Subjects, Addmission_Number) -> None:
        self.Department = Department
        self.Teachers = Teachers
        self.Name = Name
        self.Students = Students
        self.Subjects = Subjects
        self.Addmission_Number = Addmission_Number 
        self.email = Last_Name + First_Name + 'SecSch'+'@kfc.edu.ng'
class Department(Senior_Secondary_School):
    def __init__(self, Department, Teachers, Students, Addmission_Number, Science,  Arts, Commercial):
        super().__init__(Department, Teachers, Students, Addmission_Number)
class Teachers(Senior_Secondary_School):
    def __init__(self, Department, Teachers, Students, Subjects, Science_Teachers, Arts_Teachers, Commercial_Teachers) -> None:
        super().__init__(Department, Teachers, Students, Subjects)
Science_Teachers = ["Mr Bright", "Mrs Onuorah"]
Arts_Teachers = ["Mrs Olomo", "Mr Love"] 
Commercial_Teachers = ["Mr Joshua", "Mrs Madu"]
class Name(Senior_Secondary_School):
    def __init__(self, Department, Teachers, Name, Last_Name, First_Name, Middle_Name,  Students, Subjects, Addmission_Number) -> None:
        super().__init__(Department, Teachers, Name, Students, Subjects, Addmission_Number)
Last_Name = input("Enter Your Last Name: ")
First_Name = input("Enter Your First Name:")
Middle_Name = input("Enter Your Middle Name: ") 
class Students(Senior_Secondary_School):
    def __init__(self, Department, Teachers, Students, Science_Students, Arts_Students, Commercial_Students, Addmission_Number, email) -> None:
        super().__init__(Department, Teachers, Students, Addmission_Number, email) 
class addmission_number(Senior_Secondary_School):
    def __init__(self, Department, Teachers, Students, Subjects, Addmission_Number ) -> None:
        super().__init__(Department, Teachers, Students, Subjects, Addmission_Number)
        self.addmission_number = addmission_number
addmission_number = (1 , 100)
addmission_number = int(input("Enter Your Addmission Number: ")) # Takes In Students Addmission Number
class email(Senior_Secondary_School):
    def __init__(self, Department, Teachers, Students, Subjects, addmission_number, email) -> None:
        super().__init__(Department, Teachers, Students, Subjects, addmission_number, email)
        self.email = email
email = Last_Name + First_Name + '@kfc.edu.ng'   
class Subjects(Senior_Secondary_School):
    def __init__(self, Department, Teachers, Students, Subjects, addmission_number, Science_Subjects, Arts_Subjects, Commercial_Subjecets) -> None:
        super().__init__(Department, Teachers, Students, Subjects, addmission_number) 
Science_Subjects = ["Physics", "Chemistry", "Biology"]
Arts_Subjects = ["Literaturs", "Government"]
Commercial_Subjects = ["Financial Accounting", "Commerce"]
dept = input("Enter your Department:")
if dept == "Science":
    print("Welcome to Science Depatment")
    print(addmission_number)
    print(email)
    for a in Science_Subjects:
        print(a) # Display Science Subjects 
    for b in Science_Teachers:
        print(b) # Display Science Teachers 
    print(len(Science_Subjects))
    print(len(Science_Teachers))
elif dept == "Arts":
    print("Welcome to Arts Department")
    print(addmission_number)
    print(email)
    for c in Arts_Subjects:
        print(c) # Display Arts Subjects 
    for d in Arts_Teachers:
        print(d) # Display Arts Teachers    
    print(len(Arts_Teachers))
    print(len(Arts_Subjects))
elif dept == "Commercial":
    print("Welcome to Commercial Department")
    print(addmission_number)
    print(email)
    for e in Commercial_Subjects:
        print(e) # Display Commmercial Subjects
    for f in Commercial_Teachers:
        print(f) # Display Commercial Teachers 
    print(len(Commercial_Teachers))
    print(len(Commercial_Subjects))
else:
    print("Try Again")   

    