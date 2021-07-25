from tkinter import *
def plus() :
    A = float(a.get())
    B = float(b.get())
    result.set(A+B)
def minus() :
    A = float(a.get())
    B = float(b.get())
    result.set(A - B)
def multi() :
    A = float(a.get())
    B = float(b.get())
    result.set(A*B)
def devide() :
    A = float(a.get())
    B = float(b.get())
    if B == 0 :
            result.set('Cannot Devide By Zero!')
    else:
        result.set(A / B)
root = Tk()
a = StringVar()
b = StringVar()
result = StringVar()
root.title('Simple Calculator')
root.minsize(height=150, width=270)
Label(root, text = 'SimPle Calculator', justify = CENTER, font = ('tahoma', 16), fg = 'blue').grid(row=0, columnspan = 3)

framebutton = Frame(root)
Button(framebutton, text = 'Plus', command = plus).pack(side = TOP, fill = X)
Button(framebutton, text = 'Minus', command = minus).pack(side = TOP, fill = X)
Button(framebutton, text = 'Multiply', command = multi).pack(side = TOP, fill = X)
Button(framebutton, text = 'Devide', command = devide).pack(side = TOP, fill = X)
framebutton.grid(row=1, column=0, rowspan=4)

Label(root, text = 'Number A = ').grid(row = 1, column = 1)
Entry(root, width = 20, textvariable = a).grid(row = 1, column = 2)

Label(root, text = 'Number B = ').grid(row = 2, column = 1)
Entry(root, width = 20, textvariable = b).grid(row = 2, column = 2)

Label(root, text = 'Result = ').grid(row = 3, column = 1)
Entry(root, width = 20, textvariable = result).grid(row = 3, column = 2)

Button(root, text ='Exit', command = root.quit).grid(row = 4, column = 2)
root.mainloop()
