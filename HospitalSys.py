class Hospital_Management:
    def __init__(self, Staffs, Patients,) -> None:
        self.Staffs = Staffs
        self.Patients = Patients
class Staffs(Hospital_Management):
    def __init__(self, Staffs, Medical_Staffs, Non_Medical_Staffs, Patients) -> None:
        super().__init__(Staffs, Patients)
        self.Medical_Staffs = Medical_Staffs
        self.Non_Medial_Staffs = Non_Medical_Staffs
Medical_Staffs = ["General Doctors", "Nurses", "Specialist Doctors"]
Non_Medical_Staffs = ["Drivers", "Cleaners", "Gatemen"] 
'''
for a in Medical_Staffs:
    print(a)
for b in Non_Medical_Staffs:
    print(b)    
class Patients(Hospital_Management):
    def __init__(self, Staffs, Patients) -> None:
        super().__init__(Staffs, Patients)
'''

PatientsName  = input("Enter Your Name:")
PatientsAge = int(input("Enter Your Age: "))
if PatientsAge <= 5:
    print("You Are Seeing The Padiatrics") 
elif PatientsAge > 5 and PatientsAge <= 17:
    print("You Are Seeing The General Doctor ")   
#elif PatientsAge >= 18    