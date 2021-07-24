from tkinter import *
from Center import *
def Continue() :
    hsa.set('')
    hsb.set('')
    kq.set('')
def activate() :
    a = float(hsa.get())
    b = float(hsb.get())
    if a == 0 and b == 0 :
        kq.set('Vô Số Nghiệm!')
    elif a == 0 and b != 0 :
        kq.set('Vô Nghiệm!')
    else:
        kq.set('x = ' + str(-b/a))

root = Tk()
hsa = StringVar()
hsb = StringVar()
kq = StringVar()

root.title('Phương Trình Bậc 1')
root.minsize(height =100, width=310)
root.resizable(height=True, width=True)
center(root)
Label(root, text = 'Phương Trình Bậc 1 : ax + b = 0', fg = 'red', font = ('tohama', 16), justify = CENTER).grid(row = 0, columnspan = 2)

Label(root, text ="Hệ số a : ").grid(row = 1, column = 0)
Entry(root, width = 30, textvariable = hsa).grid(row = 1, column = 1)

Label(root, text ="Hệ số b : ").grid(row = 2, column = 0)
Entry(root, width = 30, textvariable = hsb).grid(row = 2, column = 1)

framebutton = Frame()
Button(framebutton, text = 'Giải', command = activate).pack(side = LEFT)
Button(framebutton, text = 'Tiếp', command = Continue).pack(side = LEFT)
Button(framebutton, text = 'Thoát', command = root.quit).pack(side = LEFT)
framebutton.grid(row = 3, columnspan = 2)

Label(root, text ="Kết quả : ").grid(row = 4, column = 0)
Entry(root, width = 30, textvariable = kq).grid(row = 4, column = 1)

root.mainloop()