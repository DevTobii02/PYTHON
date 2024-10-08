from tkinter import *
#from PIL import Image, ImageTk 
class Store_System:
    def __init__(self,root) -> None:
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System |  Developed By : Adebayo Abdullahi(DevTobii)")

        #self.icon_title = PhotoImage()
        title = Label(self.root, text = "Inventory Management System", font=("times new roman", 40, "bold" ), bg="Blue", fg="White", anchor= "center").place(x = 0, y=0, relwidth = 1, height=70  )
root = Tk()
obj = Store_System(root)
root.mainloop() 