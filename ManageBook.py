from tkinter import *
from  FileBook import *

def add() :
    if ma.get() != '' and ten.get() != '' and nam.get() != '' :
        line = ma.get() + ';' + ten.get() + ';' + nam.get()
        savefile(line)
        ma.set('')
        ten.set('')
        nam.set('')
        showbook()
def showbook() :
    arrsach = readfile()
    listbox.delete(0,END)
    for item in arrsach:
        listbox.insert(END, item)
def sortbook() :
    arrsach = readfile()
    for i in range(len(arrsach)-1) :
        for j in range(i+1, len(arrsach)) :
            if arrsach[i][2] > arrsach[j][2] :
                arrsach[i], arrsach[j] = arrsach[j], arrsach[i]
    listbox.delete(0, END)
    for item in arrsach:
        listbox.insert(END, item)
def find() :
    f1 = ma.get()
    f2 = ten.get()
    f3 = nam.get()
    arrsach = readfile()
    found = False
    listbox.delete(0, END)
    for book in arrsach :
        if (book[0] == f1 or f1 =='') and (book[1] == f2 or f2 =='') and (book[2] == f3 or f3 =='') :
            listbox.insert(END, book)
            found = True
    if not found :
        listbox.insert(END, 'Not Found!')

root = Tk()
root.title('Quản Lý Sách')
root.minsize(height=290, width=310)

ma = StringVar()
ten = StringVar()
nam = StringVar()

Label(root, text ='Quản lý sách', fg='blue', font =('cambria',16)).grid(row =0, columnspan=2)

listbox = Listbox(root, width=50)
listbox.grid(row=1, columnspan=2)
showbook()

Label(root, text ='Mã sách :').grid(row=2, column=0)
Entry(root, width=30, textvariable=ma).grid(row=2, column=1)

Label(root, text ='Tên sách :').grid(row=3, column=0)
Entry(root, width=30, textvariable=ten).grid(row=3, column=1)

Label(root, text ='Năm xuất bản :').grid(row=4, column=0)
Entry(root, width=30, textvariable=nam).grid(row=4, column=1)

framebutton = Frame(root)
Button(framebutton, text='Thêm', width=5, command = add).pack(side = LEFT)
Button(framebutton, text='Tìm', width=5, command = find).pack(side = LEFT)
Button(framebutton, text='Sắp xếp', width=6, command=sortbook).pack(side = LEFT)
Button(framebutton, text='Thoát', width=5, command=root.quit).pack(side = LEFT)
framebutton.grid(row = 5, column =1)

root.mainloop()
