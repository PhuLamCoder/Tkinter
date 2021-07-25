from tkinter import *
def b1():
    eva.set(eva.get() +'1')
def b2():
    eva.set(eva.get() +'2')
def b3():
    eva.set(eva.get() +'3')
def b4():
    eva.set(eva.get() +'4')
def b5():
    eva.set(eva.get() +'5')
def b6():
    eva.set(eva.get() +'6')
def b7():
    eva.set(eva.get() +'7')
def b8():
    eva.set(eva.get() +'8')
def b9():
    eva.set(eva.get() +'9')
def b10():
    eva.set(eva.get() +'-')
def b11():
    eva.set(eva.get() +'0')
def b12():
    eva.set(eva.get() +'.')
def b13():
    eva.set(eva.get() +'+')
def b14():
    eva.set(eva.get() +'-')
def b15():
    eva.set(eva.get() +'*')
def b16():
    eva.set(eva.get() +'/')
def b17():
    try:
        x = eval(eva.get())
        eva.set(eva.get() +'=' + str(x))
    except:
        eva.set('Cannot Devide By Zero!')
def b18():
    eva.set('')
root = Tk()
root.title('Calculator')
root.minsize(height=180, width=100)
eva = StringVar()

Entry(root, width=40, textvariable = eva).grid(row=0, columnspan=5)

rowone = Frame(root)
Button(rowone, text = '1', width = 10, command = b1).pack(side = LEFT)
Button(rowone, text = '2', width = 10, command = b2).pack(side = LEFT)
Button(rowone, text = '3', width = 10, command = b3).pack(side = LEFT)
rowone.grid(row=1, columnspan=5)

rowtwo = Frame(root)
Button(rowtwo, text = '4', width = 10, command = b4).pack(side = LEFT)
Button(rowtwo, text = '5', width = 10, command = b5).pack(side = LEFT)
Button(rowtwo, text = '6', width = 10, command = b6).pack(side = LEFT)
rowtwo.grid(row=2, columnspan=5)

rowthree = Frame(root)
Button(rowthree, text = '7', width = 10, command = b7).pack(side = LEFT)
Button(rowthree, text = '8', width = 10, command = b8).pack(side = LEFT)
Button(rowthree, text = '9', width = 10, command = b9).pack(side = LEFT)
rowthree.grid(row=3, columnspan=5)

rowfour = Frame(root)
Button(rowfour, text = '-', width = 10, command = b10).pack(side = LEFT)
Button(rowfour, text = '0', width = 10, command = b11).pack(side = LEFT)
Button(rowfour, text = '.', width = 10, command = b12).pack(side = LEFT)
rowfour.grid(row=4, columnspan=5)

rowfive = Frame(root)
Button(rowfive, text = '+', width = 6, command = b13).pack(side = LEFT)
Button(rowfive, text = '-', width = 5, command = b14).pack(side = LEFT)
Button(rowfive, text = '*', width = 5, command = b15).pack(side = LEFT)
Button(rowfive, text = '/', width = 5, command = b16).pack(side = LEFT)
Button(rowfive, text = '=', width = 6, command = b17).pack(side = LEFT)
rowfive.grid(row=5, columnspan=5)

Button(root, text = 'Clr', width = 33, command = b18).grid(row = 6, columnspan = 5)

root.mainloop()
