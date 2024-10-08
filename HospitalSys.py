print("Welcome To Newgate Hospital")
import datetime
date = datetime.datetime.now()
print(date) 
class Hospital_Management:
    def __init__(self, Non_Medical_Staffs, Medical_Staffs, Patients_Data, Patients_Category, ComplainSection_and_FeedBack) -> None:
        self.Non_Medical_Staffs = Non_Medical_Staffs
        self.Medical_Staffs = Medical_Staffs
        self.Patients_Data = Patients_Data
        self.Patients_Category = Patients_Category
        self.ComplainSection_and_FeedBack = ComplainSection_and_FeedBack
class Non_Medical_Staffs(Hospital_Management): 
    Non_Medical_Staffs = ("Accountant", "Cleaner", "Receptionist", "Driver")
    for a in Non_Medical_Staffs:
        print(a)
class Medical_Staffs(Hospital_Management):
    Medical_Staffs = ("Paediatrics", "General Doctors", "Nurses", "Matrons")
    for b in Medical_Staffs:
        print(b)
class Patient_Category(Hospital_Management):
    Patient_Category = input("")
#print(date) 



"""
print("Welcome To Newgate Hospital ")
import datetime
date = datetime.datetime.now()
print(date)
class Hospital_Management:
    def __init__(self, Medical_Staffs, Non_Medical_Staffs, Patients_Category, Patients_Data, Complain_Section) -> None:
        self.Medical_Staffs = Medical_Staffs
        self.Non_Medical_Staffs = Non_Medical_Staffs
        self.Patients_Category = Patients_Category
        self.Patients_Data = Patients_Data 
        self.Complain_Section = Complain_Section
class Medical_Staffs(Hospital_Management):
    def __init__(self, Medical_Staffs, General_Doctors, Pediatrics, Nurses, Surgeon, Specialist_Doctors, Gyneacologist,  Non_Medical_Staffs, Patients_Category, Patients_Data, Complain_Section) -> None:
        super().__init__(Medical_Staffs, Non_Medical_Staffs, Patients_Category, Patients_Data, Complain_Section)  
        self.General_Doctors = General_Doctors
        self.Pediatrics = Pediatrics
        self.Nurses = Nurses
        self.Surgeon = Surgeon
        self.Specialist_Doctors = Specialist_Doctors
        self.Gyneacologist = Gyneacologist
Gyneacologist = ["Pregnancy",  "Ante-Natal", "Child Birth", "Delivery"]
Surgeon = ["Operations"]
Specialist_Doctors = ["Kidney Doctors", "Heart Doctors", "Skin Specialist"]   
Pediatrics = ["Children from Childbirth - 4 Years Of Age "]     
Nurses = ["Auxillary Nurses, Matrons"]
General_Doctors = ["Malaria", "Typhoid", "e.t.c"]
class Non_Medical_Staffs(Hospital_Management):
    def __init__(self, Medical_Staffs, Non_Medical_Staffs, Cleaners, Drivers, Chef, Accountant, Receiptionist,  Patients_Category, Patient_Data, Complain_Section) -> None:
        super().__init__(Medical_Staffs, Non_Medical_Staffs, Patients_Category, Patient_Data, Complain_Section)
        self.Cleaners = Cleaners
        self.Drivers = Drivers
        self.Chef = Chef
        self.Accountant = Accountant
        self.Receiptionist = Receiptionist
Cleaners = ["Maintains Hospital's Neatness"]
Drivers = ["Ambulance", "Errands", "Drugs PickUp"]
Chef = ["In Charge Of Addmitted Patients Feeding"] 
Accountant = ["Finance Of The Hospital"]
Receiptionist = ["Attends and Directs Patients To Rightful Doctors"] 



class Patient_Category(Hospital_Management):
    def __init__(self, Medical_Staffs, Non_Medical_Staffs, Patients_Category, Infants, Children, Teenagers, Adult, Elderly, Patients_Data) -> None:
        super().__init__(Medical_Staffs, Non_Medical_Staffs, Patients_Category, Patients_Data)
        self.Infants = Infants
        self.Children = Children
        self.Teenagers = Teenagers
        self.Adult = Adult
        self.Elderly = Elderly

        
class Patients_Data(Hospital_Management):
    def __init__(self, Medical_Staffs, Non_Medical_Staffs, Patients_Category, Patients_Data, Name, Age, Date_Of_Birth, Nationality, State_Of_Origin, Card_Number, Blood_Group, Genotype, Email, Phone_Number, Residence, Complain_Section) -> None:
        super().__init__(Medical_Staffs, Non_Medical_Staffs, Patients_Category, Patients_Data, Complain_Section)        
        self.Name = Name
        self.Age = Age
        self.Date_Of_Birth = Date_Of_Birth
        self.Nationality = Nationality 
        self.State_Of_Origin = State_Of_Origin
        self. Card_Number = Card_Number
        self.Blood_Group = Blood_Group
        self.Genotype = Genotype 
        self.Email = Email 
        self.Phone_Number = Phone_Number 
        self.Residence = Residence
Name = input("Name: ") 
Age = int(input("Age: "))
if Age >= 0 and Age <= 4:
    print("Infant")
    for a in Pediatrics:
        print(a)
elif Age >= 5 and Age <= 12:
    print("Children")
elif Age >= 13 and Age <= 17:
    print("Teenager")
elif Age >= 18 and Age <= 65:
    print("Adult")
else:
    print("Elderly")          
Date_Of_Birth = input("Date Of Birth: ")
Nationality = input("Nationality: ") 
State_Of_Origin = input("State Of Origin: ")
Card_Number = int(input("Card Number: ")) 
Blood_Group = input("Blood Group: ")
Genotype = input("Genotype: ")
Email = input("Email: ")
Phone_Number = int(input("Phone Number: "))
Residence = input("Residence: ")
class Complain_Section(Hospital_Management):
    def __init__(self, Medical_Staffs, Non_Medical_Staffs, Patients_Category, Patients_Data, Complain_Section) -> None:
        super().__init__(Medical_Staffs, Non_Medical_Staffs, Patients_Category, Patients_Data, Complain_Section)
        self.Complain = []
        
import json
import sqlite3
print(date) 



print("Welcome To Newgate Medical Center")
class Hospital_Management:
    def __init__(self, Staffs, Patients_Category, Patients_Data) -> None:
        self.Staffs = 
        self.Patients_Category  = Patients_Category
        self.Patients_Data = Patients_Data
class Staffs(Hospital_Management):
    def __init__(self, Staffs, Medical_Staffs, Non_Medical_Staffs, Patients_Category, Patients_Data) -> None:
        super().__init__(Staffs, Patients_Category, Patients_Data)
        self.Medical_Staffs = Medical_Staffs
        self.Non_Medial_Staffs = Non_Medical_Staffs
Medical_Staffs = ["General Doctors", "Nurses", "Specialist Doctors"]
Non_Medical_Staffs = ["Drivers", "Cleaners", "Gatemen"] 
class Medical_Staffs(Hospital_Management):
    def __init__(self, Staffs, Genearal_Doctors, Nurses, Lab_Attendeants, Patients_Category, Patients_Data) -> None:
        super().__init__(Staffs, Patients_Category, Patients_Data)
class Patients_Category(Hospital_Management):
    def __init__(self, Staffs, Patients_Category, Infants, Children, Teenagers, Adult) -> None:
        super().__init__(Staffs, Patients_Category)
        self.Infants = Infants
        self.Children = Children
        self.Teenagers = Teenagers
        self.Adult = Adult                
class Patients_Data(Hospital_Management):
    def __init__(self, Staffs, Patients_Category, Patients_Data, Patient_Name,  Date_Of_Birth, Age, Complexion, Nationlatity, State_Of_Origin, Card_Number, Blood_Group, Genotype, Phone_Number, Email, Address, Next_Of_Kin_Name, Next_Of_Kin_Age,  Next_Of_Kin_Address, Next_Of_Kin_Phone_Number, Next_Of_Kin_Relationship_To_Patient) -> None:
        super().__init__(Staffs, Patients_Category, Patients_Data)        
        self.Patient_Name = Patient_Name
        self.Date_Of_Birth = Date_Of_Birth
        self.Age = Age 
        self.Complexion = Complexion
        self.Nationality =Nationlatity
        self.State_Of_Origin = State_Of_Origin
        self.Card_Number = Card_Number 
        self.Blood_Group = Blood_Group
        self.Genotype = Genotype
        self.Phone_Number = Phone_Number
        self.Email = Email
        self.Address = Address
        self.Next_Of_Kin_Name = Next_Of_Kin_Name
        self.Next_Of_Kin_Age = Next_Of_Kin_Age 
        self.Next_Of_Kin_Address = Next_Of_Kin_Address
        self.Next_Of_Kin_Phone_Number = Next_Of_Kin_Phone_Number
        self.Next_Of_Kin_Relationship_To_Patient = Next_Of_Kin_Relationship_To_Patient
Patient_Name = input("Enter Your Name: ")      
Date_Of_Birth = input("Date Of Birth: ")
Age = int(input("Enter Your Age: "))
if Age > 0 and Age  <= 5:
    print("Infants")
elif Age >= 6 and Age <= 12:
    print("Children")    
elif Age >= 13 and Age <= 17:
    print("Teenager")    
elif Age > 17 and Age <= 65:
    print("Adult")
else:
    print("Elderly")         
Complexion = input("Complexion: ")
Nationality = input("Nationality: ")
State_Of_Origin = input("State Of Origin: ") 
Card_Number = input("Card Number: ")
Blood_Group = input("Blood Group: ")
Genotype = input("Genotype: ")
Phone_Number = int(input("Phone Number: "))
Email = input("Email Address: ") 
Address = input("Address: ")
print("Patients Next Of Kin Information") 
Next_Of_Kin_Name = input("Enter Your Name: ")
Next_Of_Kin_Age = int(input("Age: "))
Next_Of_Kin_Address = input("Address: ")
Next_Of_Kin_Phone_Number = int(input("Phone Number: "))
Next_Of_Kin_Relationship_To_Patient = input("Relationship To Patient: ")

class Patient_Category(Hospital_Management):
    def __init__(self, Medical_Staffs, Non_Medical_Staffs, Patients_Category, Infants, Children, Teenagers, Adult, Elderly, Patients_Data) -> None:
        super().__init__(Medical_Staffs, Non_Medical_Staffs, Patients_Category, Patients_Data)
        self.Infants = Infants
        self.Children = Children
        self.Teenagers = Teenagers
        self.Adult = Adult
        self.Elderly = Elderly
"""