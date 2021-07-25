from tkinter import *
def Continue() :
    hsa.set('')
    hsb.set('')
    hsc.set('')
    kq.set('')
def activate() :
    a = float(hsa.get())
    b = float(hsb.get())
    c = float(hsc.get())
    denta = b*b - 4*a*c
    if a == 0 :
        if b == 0 and c == 0 :
            kq.set('Phương Trình Vô Số Nghiệm!')
        elif b == 0 and c != 0 :
            kq.set('Phương Trình Vô Nghiệm!')
        else :
            kq.set('x đơn = ' + str(-c/b))
    elif denta < 0 :
        kq.set('Phương Trình Vô Nghiệm!')
    elif denta == 0 :
        kq.set('x kép = ' + str(-b/(2*a)))
    else:
        x1 = (-b + denta**0.5)/(2*a)
        x2 = (-b - denta**0.5)/(2*a)
        kq.set('x1 = '+str(x1) + ' , x2 = ' + str(x2))
root = Tk()
hsa = StringVar()
hsb = StringVar()
hsc = StringVar()
kq = StringVar()

root.title('Phương Trình Bậc 2')
root.minsize(height =150, width=330)
Label(root, text = 'Phương Trình Bậc 2 : ax^2 + bx + c = 0', fg = 'blue', font = ('tohama', 16), justify = CENTER).grid(row = 0, columnspan = 2)

Label(root, text ="Hệ số a : ").grid(row = 1, column = 0)
Entry(root, width = 30, textvariable = hsa).grid(row = 1, column = 1)

Label(root, text ="Hệ số b : ").grid(row = 2, column = 0)
Entry(root, width = 30, textvariable = hsb).grid(row = 2, column = 1)

Label(root, text ="Hệ số c : ").grid(row = 3, column = 0)
Entry(root, width = 30, textvariable = hsc).grid(row = 3, column = 1)

framebutton = Frame(root)
Button(framebutton, text = 'Giải', command = activate).pack(side = LEFT)
Button(framebutton, text = 'Tiếp', command = Continue).pack(side = LEFT)
Button(framebutton, text = 'Thoát', command = root.quit).pack(side = LEFT)
framebutton.grid(row = 4, columnspan = 2)
'''
#Đoạn này khác với trên kia, không xài frame với pack
Button(root, text = 'Giải', command = activate).grid(row = 4, column = 0)
Button(root, text = 'Tiếp', command = Continue).grid(row = 4, column = 1)
Button(root, text = 'Thoát', command = root.quit).grid(row = 4, column = 2)
'''

Label(root, text ="Kết quả : ").grid(row = 5, column = 0)
Entry(root, width = 30, textvariable = kq).grid(row = 5, column = 1)

root.mainloop()