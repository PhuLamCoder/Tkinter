from tkinter import *
root = Tk()
root.title('NewPassword')
root.minsize(height=100,width=340)

Label(root, text='Old Password : ', width=23, justify = LEFT).grid(row=0, column=0)
Entry(root, width = 25).grid(row=0, column=1)

Label(root, text='New Password : ', width=23, justify = LEFT).grid(row=1, column=0)
Entry(root, width = 25).grid(row=1, column=1)

Label(root, text='Enter New Password Again : ', width=23).grid(row=2, column=0)
Entry(root, width = 25).grid(row=2, column=1)

Label(root).grid(row=3)

Button(root, text ='Ok', width = 10, justify = RIGHT).grid(row=4, column =0)
Button(root, text ='Cancel', width = 10, justify = LEFT, command = root.quit).grid(row=4, column = 1)

root.mainloop()