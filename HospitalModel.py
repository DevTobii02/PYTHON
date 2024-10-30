class HospitalManagementSystem:
    def __init__(self) -> None:
        self.Patients = []
        self.MedicalStaffs = []
        self.NonMedicalStaffs = []
        self.MedicalRecords = []
        self.FeeRecords = {}
        self.RegistrationCriteria = {
            'Min Age' : 18,
        }
    def RegisterNewPatient(self):
        name = input("Enter Patient Name : ") 
        age = int(input("Enter Patient Age : "))  
        phonenumber = int(input("Enter Patient's Phone Number : ")) 
        email = input("Enter Patient's Email Address : ")
        address = input("Enter Patient's Address : ") 
        if self.CheckRegistrationCriteria(name, age,  phonenumber, email, address):
            Patient = {
                'name' : name,
                'age'  : age,
                'phonenumber' : phonenumber,
                'email' : email,
                'address' : address
            }
            self.Patients.append(Patient) 
            # Initialize Payment For New Patient 
            self.FeeRecords[name] = {'totalfee' : 0, 'paidfee' : 0}
            print(f"Patient{name} Added Successfully") 
        else:
            print("Patient Does Not Meet Registration Criteria")
    def CheckRegistrationInfo(self, name, age):
        if age  < self.RegistrationCriteria ['Min Age'] :
            print("Patients Below 18 Cannot Be Registered By Themselves")
    def ViewPatients(self):
        self.ViewPatients()
        if not self.Patients:
            return
        print("List Of Patients : ") 
        for i, patient in enumerate(self.Patients, start=1):
            print(f"{i}, Name : {patient['name']}, Age : {patient['age']}, NIN : {patient['nin']}, Email : {patient['email']}, Address : {patient['address']}") 
        print()
    def DeletePatients(self):
        self.ViewPatients()
        if not self.Patients:
            return
        try:
            PatientIndex = int(input("Enter Patient Number To Be Deleted : ")) -1
            if 0 <= PatientIndex < len(self.Patients):
                RemovedPatient = self.Patients.pop(PatientIndex)
                self.FeeRecords.pop(RemovedPatient['name'], None)
                print(f"Patient {RemovedPatient['name']} Deleted Successfully ! \n")
            else:
                print("Invalid Patient Number")
        except ValueError:
            print("Please Enter A Valid Patient Number")
    def SubmitFee(self):
        self.ViewPatients()
        if not self.Patients:
            return
        name = input("Enter Patient Name To Be Submitted : ").lstrip() 
        if name in self.FeeRecords:
            try:
                totalfee = float(input("Enter Total Amount Fee : "))
                paidfee = float(input("Enter Amount To Be Paid : "))
                if paidfee > totalfee:
                    print("Paid Fee Cannot be Greater Than Total Fee ")
                    return
                self.FeeRecords[name]['totalfee'] = totalfee
                self.FeeRecords[name]['paidfee'] += paidfee
                print(f"Fee Of {paidfee} Submitted Successfully For {name}. \n") 
            except ValueError:
                print("Please Enter A Valid Number") 
            else:
                print("Patient Not Found. \n") 
    def ViewFee(self):
        if not self.FeeRecords:
            print("No Fee Records Found ")  
            return
        print("Fee Records: ")     
        for name, record in self.FeeRecords.items():
            print(f"Name : {name}, Total Fee{record['totalfee']}, Paid Fee : {record['paidfee']}") 
            print()
    def run(self):
         while True:
             print("1 Add Patient")
             print("2. View Patient") 
             print("3. Delete Patient") 
             print("4. Submit Fee") 
             print("5. View Fee Records")
             print("6. Exit")
             Choice = input("Pick A Choice From Range Of Choices") 
             if Choice == "1":
                 self.RegisterNewPatient()
             elif Choice == "2":
                 self.ViewPatients()
             elif Choice == "3":
                 self.DeletePatients()
             elif Choice == "4":
                 self.SubmitFee()
             elif Choice == "5":
                 self.ViewFee()
             elif Choice == "6":
                 print("Exiting The System Goodbye")
                 break
             else:
                 print("Invalid Choice Please Try Again")
if __name__ == "__main__":
    system = HospitalManagementSystem()
    system.run                 