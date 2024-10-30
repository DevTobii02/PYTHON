class SchoolManagementSystem:
    def __init__(self) -> None:
        self.students = []
        self.FeeRecords = {}
        self.AddmissionCriteria = {
            'MinAge' : 5,
            'MaxAge' : 18,
            'MinClass' : 1,
            'MaxClass' : 12
        }
    def AddStudent(self):
        name = input("Enter Student's Name : ")
        age = int(input("Enter Student's Age : "))
        studentclass = int(input("Enter Student Class : "))
        if self.CheckAddmissionCriteria(age, studentclass):
            student = {
                'name' : name,
                'age' : age,
                'class' : studentclass
            }
            self.students.append(student)
            # Initialize Fee Record For New Student
            self.FeeRecords[name] = {'totalfee' : 0, 'paidfee' : 0}
            print(f"Student {name} Added Successfully")
        else:
            print("Student Does Not Meet Addmission Criteria. \n")
    def CheckAddmissionCriteria(self, age, studentclass) :
        if age < self.AddmissionCriteria['MinAge']:
            print("Student Is Too Young For Addmission.")
            return False
        if age > self.AddmissionCriteria['MaxAge']:
            print("Student Class Is Out Of Range. ")
            return False
        return True
    def ViewStudents(self):
        if not self.students:
            print("No Student Found. \n")
            return
        print("List Of Student : ")
        for i, student in enumerate(self.students, start=1):
            print(f"{i}, Name: {student['name']}, Age:{student['age']}, class: {student['class']}")
        print()
    def DeleteStudents(self):
        self.ViewStudents()   
        if not self.students:
            return
        try:
            StudentIndex = int(input("Enter The Student Number To Be Deleted : ")) -1
            if 0 <= StudentIndex < len(self.students):
                RemovedStudent = self.students.pop(StudentIndex) 
                # Remove Record Fee For Deleted Student 
                self.FeeRecords.pop(RemovedStudent['name'], None)
                print(f"Student {RemovedStudent['name']} Deleted Successfully ! \n")
            else:
                print("Invalid Student Number. \n")
        except ValueError:
            print("Please Enter A Valid Number. \n")  
    def SubmitFee(self):
        self.ViewStudents()
        if not self.students:
            return       
        name = input("Enter The Student's Name To Submit Fee For: ").strip() 
        if name in self.FeeRecords:
            try:
                totalfee = float(input("Enter The Total Fee Amount : "))
                paidfee = float(input("Enter The Amount Of Fee To Be Paid : "))
                if paidfee > totalfee:
                    print("Paid Fee Cannot Be Greater Than Total Fee. \n")
                    return
                self.FeeRecords[name]['totalfee'] = totalfee
                self.FeeRecords[name]['paidfee'] += paidfee 
                print(f"Fee Of {paidfee} Submitttedd Successfully For {name}.\n")
            except ValueError:
                print("Please Enter A Valid Number : \n")
            else:
                print("Student Not Found. \n")
    def ViewFee(self):
        if not self.FeeRecords:
            print("No Fee Records Found. \n")      
            return
        print("Fee Records: ")  
        for name, record in self.FeeRecords.items():
            print(f"Name: {name}, Total Fee : {record['totalfee']}, paidfee: {record['paidfee']}")
            print()
    def run(self):
        while True:
            print("1 Add Student")
            print("2. View Student")
            print("3. Delete Student")
            print("4. Submt Fee")
            print("5. View Fee Records")
            print("6. Exit")
            Choice = input("Enter Your Choice : ")
            if Choice == "1":
                self.AddStudent()
            elif Choice == "2":
                self.ViewStudents
            elif Choice == "3":
                self.DeleteStudents()
            elif Choice == "4":
                self.SubmitFee()
            elif Choice == "5":
                self.ViewFee()
            elif Choice == "6":
                print("Exiting The System. GoodBye!!!")
                break
            else:
                print("Invalid Choice.Please Try Again ")
                
if __name__ == "__main__":
    system = SchoolManagementSystem()
    system.run()                