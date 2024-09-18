print("Welcome To Adetech Stores. What Are You Buying From Us Today")
class PRODUCTS:
    def __init__(self, Products, ProductName, ProductsPrice, Quantity, Attendants) -> None:
        self.Products = Products
        self.ProductName = ProductName
        self.ProductPrice = ProductsPrice
        self.Quantity = Quantity
        self.Attendants = Attendants
class Products(PRODUCTS):
    def __init__(self, Products, Dangote, GoldenPenny, Kelllogs, Nasco, ProductName, ProductsPrice, Quantity, Attendants) -> None:
        super().__init__(Products, ProductName, ProductsPrice, Quantity, Attendants)
        self.Dangote = Dangote
        self.GoldenPenny = GoldenPenny
        self.Kellogs = Kelllogs
        self.Nasco = Nasco
import datetime
date = datetime.datetime.now()
print(date)
Products = input("Enter Your Product: ")  # Choose From Range Of Products
if Products == "Dangote":
    print("Thanks For Choosing Dangote")
elif Products == "Golden Penny":
    print("Thanks For Choosing Golden Penny")
elif Products == "Kellogs":
    print("Thanks For Choosing Kellogs")
elif Products == "Nasco":
    print("Thanks For Choosing Nasco")
else:
    print("Not a Product Try Again")     
class ProductsName(PRODUCTS):
    def __init__(self, Products, ProductName, DangoteProducts,  ProductsPrice, Quantity, Attendants) -> None:
        super().__init__(Products, ProductName, ProductsPrice, Quantity, Attendants)
        self.DangoteProducts = DangoteProducts       
DangoteProducts = ["Dangote Sugar", "Dangote Salt", "Dangote Spaghetti", "Dangote Noodles"]
if Products == "Dangote":
    for a in DangoteProducts:
        print(a) # Display Products Under Dangote
class ProductsPrice(PRODUCTS):
    def __init__(self, Products, ProductName, ProductsPrice, DangoteSugarPrice, DangoteSaltPrice, DangoteSpaghettiPrice, DangoteNoodlesPrice,  Quantity, Attendants) -> None:
        super().__init__(Products, ProductName, ProductsPrice, Quantity, Attendants)
        self.DangoteSugarPrice = DangoteSugarPrice
        self.DangoteSaltPrice = DangoteSaltPrice
        self.DangoteSpaghettiPrice = DangoteSpaghettiPrice
        self.DangoteNoodlesPrice = DangoteNoodlesPrice     
DangoteSugarPrice = 900
DangoteSaltPrice = 700
DangoteSpaghettiPrice = 1000
DangoteNoodlesPrice = 250
class ProductsName(PRODUCTS):
    def __init__(self, Products, ProductName, GoldenPennyProducts, ProductsPrice, Quantity, Attendants) -> None:
        super().__init__(Products, ProductName, ProductsPrice, Quantity, Attendants)
        self.GoldenPennyProducts = GoldenPennyProducts
GoldenPennyProducts = ["Golden Penny Noodles", "Golden Penny Spaghetti", "Golden Penny Sugar", "Golden Penny Spread"]
if Products == "Golden Penny":
    for b in GoldenPennyProducts:
        print(b) # Display Golden Penny Products
class ProductsPrice(PRODUCTS):
    def __init__(self, Products, ProductName, ProductsPrice, GoldenPennyNoodlesPrice, GoldenPennySpaghettiPrice, GoldenPennySugarPrice, GoldenPennySpreadPrice, Quantity, Attendants) -> None:
        super().__init__(Products, ProductName, ProductsPrice, Quantity, Attendants)
        GoldenPennyNoodlesPrice = GoldenPennyNoodlesPrice
        GoldenPennySpaghettiPrice = GoldenPennySpaghettiPrice
        GoldenPennySugarPrice = GoldenPennySugarPrice
        GoldenPennySpreadPrice = GoldenPennySpreadPrice
GoldenPennyNoodlesPrice = 150
GoldenPennySpaghettiPrice = 1000
GoldenPennySugarPrice = 300
GoldenPennySpreadPrice = 600
if ProductsPrice == "Golden Penny Noodles":
    print(GoldenPennyNoodlesPrice)
class ProducstName(PRODUCTS):
    def __init__(self, Products, ProductName, KellogsProducts, ProductsPrice, Quantity, Attendants) -> None:
        super().__init__(Products, ProductName, ProductsPrice, Quantity, Attendants)
        self.KellogsProducts = KellogsProducts
KellogsProducts = ["Kellogs Coco Pops", "Kellogs Corn Flakes", "Kellogs Frosties", "Kellogs Rice Cripses"]
if Products == "Kellogs":
    for c in KellogsProducts:
        print(c) # Display Kellogs Products
class ProductsPrice(PRODUCTS):
    def __init__(self, Products, ProductName, ProductsPrice,KellogosCocoPopsPrice, KellogsRiceCripsesPrice, KellogsCornFlakesPrice, KellogsFrostiesPrice,   Quantity, Attendants) -> None:
        super().__init__(Products, ProductName, ProductsPrice, Quantity, Attendants)
        self.KellogosCocoPopsPrice = KellogosCocoPopsPrice
        self.KellogsRiceCripsesPrice = KellogsRiceCripsesPrice
        self.KellogsCornFlakesPrice = KellogsCornFlakesPrice
        self.KellogsFrostiesPrice = KellogsFrostiesPrice
KellogosCocoPopsPrice = 150
KellogsRiceCripsesPrice = 200
KellogsCornFlakesPrice = 250
KellogsFrostiesPrice = 250 
class ProductsName(PRODUCTS):
    def __init__(self, Products, ProductName, NascoProducts,  ProductsPrice, Quantity, Attendants) -> None:
        super().__init__(Products, ProductName, ProductsPrice, Quantity, Attendants)
        self.NascoProducts = NascoProducts
NascoProducts = ["Nasco Corn Flakes", "Nasco Golden Morn"]  
class ProductsPrice(PRODUCTS):
    def __init__(self, Products, ProductName, ProductsPrice, NascoCornFlakesPrice, NascoGoldenMornPrice,  Quantity, Attendants) -> None:
        super().__init__(Products, ProductName, ProductsPrice, Quantity, Attendants)
        self.NascoCornFlakesPrice = NascoCornFlakesPrice
        self.NascoGoldenMorn = NascoGoldenMornPrice      
NascoCornFlakesPrice = 200        
NascoGoldenMornPrice = 300
if Products == "Nasco":
    for d in NascoProducts:
        print(d) # Display Nasco Products 
ProductsPrice = input("Enter Product Type: ")
if ProductsPrice == "Dangote Sugar":
    print("Price : ", DangoteSugarPrice)
elif ProductsPrice == "Dangote Salt":
    print("Price : ", DangoteSaltPrice)
elif ProductsPrice == "Dangote Spaghetti":
    print("Price :", DangoteSpaghettiPrice) 
elif ProductsPrice == "Dangote Noodles":
    print("Price :", DangoteNoodlesPrice) 
elif ProductsPrice == "Golden Penny Noodles":
    print("Price : ", GoldenPennyNoodlesPrice) 
elif ProductsPrice == "Golden Penny Spaghetti":
    print("Price :", GoldenPennySpaghettiPrice) 
elif ProductsPrice == "Golden Penny Sugar":
        print("Price :", GoldenPennySugarPrice) 
elif ProductsPrice == "Golden Penny Spread":
    print("Price : ", GoldenPennySpreadPrice) 
elif ProductsPrice == "Kellogs Coco Pops":
    print("Price :", KellogosCocoPopsPrice) 
elif ProductsPrice == "Kellogs Rice Cripses": 
    print("Price :", KellogsRiceCripsesPrice) 
elif ProductsPrice == "Kellogs Corn Flakes":
    print("Price :", KellogsCornFlakesPrice) 
elif ProductsPrice == "Kellogs Frosties":
    print("Price: ", KellogsFrostiesPrice)     
elif ProductsPrice == "Nasco Corn Flakes":
    print("Price :", NascoCornFlakesPrice) 
elif ProductsPrice == "Nasco Golden Morn3":
    print("Price :", NascoGoldenMornPrice) 
else:
    print("Not a Product Type")
class Quantity(PRODUCTS):
    def __init__(self, Products, ProductName, ProductsPrice, Quantity, Attendants) -> None:
        super().__init__(Products, ProductName, ProductsPrice, Quantity, Attendants)
        self.Quantity = Quantity
Quantity = int(input("Enter Your Quantity: ")) # Enter How Many Pieces You're getting 
Price = int(input("Enter Product Price: ")) 
def Total():
    total = Quantity * Price
    return total 
print(Total()) # Displays Total Price Of Items Got 
import random
class Attendants(PRODUCTS):
    def __init__(self, Products, ProductName, ProductsPrice, Quantity, Attendants, MaleAttendants, FemaleAttendants) -> None:
        super().__init__(Products, ProductName, ProductsPrice, Quantity, Attendants, MaleAttendants, FemaleAttendants)
        self.MaleAttendants = MaleAttendants
        self.FemaleAttendants = FemaleAttendants
MaleAttendants = ["Bayo", "Bode", "Timi", "Dave", "Tobi", "Toba", "Akin"]
FemaleAttendants = ["Bisi", "Bolu", "Faith", "Sandra", "Temi", "Layo", "Lara"]        
print(date.strftime("%B"))
print(date.strftime("%A"))
MaleAttendant = random.choice(MaleAttendants)
FemaleAttendant = random.choice(FemaleAttendants)
print("Checked By:", MaleAttendant)
print("Packaged By: ", FemaleAttendant)
print(date)