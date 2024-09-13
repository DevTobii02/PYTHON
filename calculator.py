# Building A Calculator GUI 
from tkinter import *
root = Tk()
root.title("Simple Calculator") # Gives The GUI Interface A Title 
a = Entry(root, width=35, borderwidth=5)
a.grid(row=0, column=0, columnspan=5, padx=10, pady=10) 
def Add_Button():
    return
def Subtract_Button():
    return
def Multiply_Button():
    return
def Divide_Button():
    return
Button_1 = Button(root, text="1", padx=20, pady=20, command=Add_Button)
Button_2 = Button(root, text="2", padx=20, pady=20, command=Add_Button)
Button_3 = Button(root, text="3", padx=20, pady=20, command=Add_Button)
Button_4 = Button(root, text="4", padx=20, pady=20, command=Add_Button)
Button_5 = Button(root, text="5", padx=20, pady=20, command=Add_Button)
Button_6 = Button(root, text="6", padx=20, pady=20, command=Add_Button)
Button_7 = Button(root, text="7", padx=20, pady=20, command=Add_Button)
Button_8 = Button(root, text="8", padx=20, pady=20, command=Add_Button)
Button_9 = Button(root, text="9", padx=20, pady=20, command=Add_Button) 
Button_0 = Button(root, text="0", padx=20, pady=20, command=Add_Button)

Button_1.grid(row=1, column=0)
Button_2.grid(row=1, column=1)
Button_3.grid(row=1, column=2)

Button_4.grid(row=2, column=0)
Button_5.grid(row=2, column=1)
Button_6.grid(row=2, column=2)

Button_7.grid(row=3, column=0)
Button_8.grid(row=3, column=1)
Button_9.grid(row=3, column=2)

Button_0.grid(row=4, column=1)

root.mainloop()