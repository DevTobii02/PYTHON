class SchoolManagementSystem:
    def __init__(self) -> None:
        self.students = []
        self.FeeCriteria = {}
        self.AddmissionCriteria = {
            "Min Age" : 5, 
            "Max Age" : 19,
            "Min Class" : 1, 
            "Max Class" : 12
        }
    def AddStudent(self):
        name = input("Enter Student Name : ") 
        age = int(input("Enter Student Age : ")) 
        studentclass = int(input("Enter Student Class :"))
        if self.CheckAddmissionCriteria(age, studentclass):
            student = {
                "name" : name,
                "age" : age,
                "class" : studentclass 
            }
            self.students.append(student)
            #Initialize fee for new student 
            
            self.FeeRecords[name] = {"TotalFee" : 0, "PaidFee" : 0}
            print(f"Student {name} added successfully. \n ")
        else:
            print("Student Does Not Meet Addmission Criteria. \n")
    def CheckAddmissionCriteria(self, age, studentclass):
        if age < self.AddmissionCriteria["Min Age"]:
            print("student Is Too Young For Addmission.")
            return False
        if age > self.AddmissionCriteria["Max Age"]:
            print("Student Class Is Out Of Range.")
            return False
        return True 
    def ViewStudent(self):
        if not self.students:
            print("No Students Found. \n")
            return
        print("List Of Students : ")
        for i, student in enumerate(self.students, start=1):
            print(f"{i}.Name: {student["name"]}, Age: {student["age"]}, class: {student["class"]}")   
            print()
    def DeleteStudents(self):
        if not self.students:
            return
        try:
            StudentIndex = int(input("Enter Student Number To Be Deleted : "))
            if 0 <= StudentIndex < len(self.students):
                RemovedStudent = self.students.pop(StudentIndex)
                #Remove Fee Record 
                self.FeeRecord.pop(RemovedStudent["name"], None)
                print(f"Student {RemovedStudent["name"]} Deleted Successfully \n") 
            else:
                print("Invalid Student Number.\n")
        except ValueError:
            print("Please Enter A Valid Number.\n") 
    def SubmitFee(self):
        self.ViewStudent()
        if not self.students:
            return
        name = input("Enter The Student's Name To Submit Fee For: ").strip()
        if name in self.FeeRecord:
            try:
                TotalFee = float(input("Enter Total Amount Paid"))
                PaidFee = float(input("Enter The Amount Of Fee To Be Paid : "))
                if PaidFee > TotalFee:
                    print("Paid Fee Cannot Be Greater Than Total Fee.\n")
                    return
                self.FeeRecord[name]["TotalFee"] = TotalFee 
                self.FeeRecord[name]["PaidFee"] += PaidFee
                print(f"Fee of {PaidFee} Submitted Succesfully For {name}.\n ")
            except ValueError:
                print("Please Enter A Valid Number. \n ")
            else:
                print("Student Not Found. \n")
    def ViewFee(self):
        if not self.FeeRecord:
            print("No Fee Record Found. \n")
            return
        print("Fee Records : ")
        for name, record in self.FeeRecord.items():
            print(f"Name: {name}, Total Fee : {record["TotalFee"]}, Paid Fee : {record["PaidFee"]}")
            print() 
    def Run(self):
        while True:
            print("1. Add Student")
            print("2.View Student")
            print("3. Delete Student")
            print("4. Submit Fee")
            print("5. View Fee Records")
            print("6. Exit")
            Choice = input("Enter Your Choice :")
            if Choice == "1":
                self.AddStudent()
            elif Choice == "2":
                self.ViewStudent()
            elif Choice == "3":
                self.DeleteStudents()
            elif Choice == "4":
                self.SubmitFee()
            elif Choice == "5":
                self.ViewFee()
            elif Choice == "6":
                print("Exiting The System .GoodBye")
                break
            else:
                print("Invalid Choice. Please Try Again. \n")
if __name__ == "__main__" :
    System = SchoolManagementSystem()
    System.Run()      