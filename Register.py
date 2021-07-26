from tkinter import *

def checkname() :
    flag = True
    name = namee.get()
    size = len(name)
    if size < 10 :
        flag = False
    else:
        for i in range(size) :
            if flag :
                flag = True
            else:
                flag = False
                break
    if flag == False :
        namee.set(namee.get() + '   ' + '(vui lòng nhập đúng format tên)')
    return flag
def checkemail() :
    mail = email.get().strip()
    size = len(mail)
    flag = True
    if size < 16 or size > 40 or mail[0] == '.' or mail[-11] == '.':
        flag = False
    elif mail[-1] != 'm' or mail[-2] != 'o' or mail[-3] != 'c' or mail[-4] != '.' or mail[-5] != 'l' or mail[-6] != 'i' or mail[-7] != 'a' or mail[-8] != 'm' or mail[-9] != 'g' or mail[-10] != '@' :
        flag = False
    else :
        for i in range(-size,-10) :
            if mail[i] == '.' and mail[i+1] == '.' :
                flag = False
                break
            elif 'a' <= mail[i].lower() <= 'z' or mail[i] == '.' or '0' <= mail[i] <= '9':
                flag = True
            else :
                flag = False
                break
    if flag == False :
        Label(root, text='(vui lòng nhập đúng format Email!)', font=('tahoma', 8), fg = 'red', justify = LEFT).grid(row=3, column=1)
    return flag

def multiaction() :
    pass

root = Tk()
root.title('Register')
root.minsize(height=360, width=270)

#textvariable
namee = StringVar()
email = StringVar()
password = StringVar()
cfpassword = StringVar()
number = StringVar()
address = StringVar
inform = StringVar()

# Tiêu đề
Label(root, text='Đăng ký tài khoản', font = ('timenewroman', 16, 'bold'),width=22, justify = CENTER, bg = 'blue', fg = 'white').grid(row=0, columnspan=4)

# Phần Tên
Label(root, width=1).grid(row=1, column=0)
Label(root, text = 'Tên'.ljust(45), font = 'tahoma', justify = LEFT).grid(row=1,column=1)
Entry(root,font = 'tahoma', text = 'cc').grid(row=1,column=1)
Label(root, width=1).grid(row=1, column=3)

Label(root, width=1).grid(row=2, column=0)
Entry(root, width = 40, textvariable = namee).grid(row=2,column=1)
Label(root, width=1).grid(row=2, column=2)

#Phần Email
Label(root, width=1).grid(row=3, column=0)
Label(root, text = 'Email'.ljust(45), font = 'tahoma', justify = LEFT, bg ='red').grid(row=3,column=1)
Label(root).grid(row=3,column=2)
Label(root, width=1).grid(row=3, column=3)

Label(root, width=1).grid(row=4, column=0)
Entry(root, width = 40, textvariable = email).grid(row=4,column=1)
Label(root, width=1).grid(row=4, column=2)

#Phần Mật Khẩu
Label(root, width=1).grid(row=5, column=0)
Label(root, text = 'Mật khẩu'.ljust(43), font = 'tahoma', justify = LEFT).grid(row=5,column=1)
Label(root, width=1).grid(row=5, column=2)

Label(root, width=1).grid(row=6, column=0)
Entry(root, width = 40, textvariable = password).grid(row=6,column=1)
Label(root, width=1).grid(row=6, column=2)

#Phần xác nhận mật khẩu
Label(root, width=1).grid(row=7, column=0)
Label(root, text = 'Xác nhận mật khẩu'.ljust(37), font = 'tahoma', justify = LEFT).grid(row=7,column=1)
Label(root, width=1).grid(row=7, column=2)

Label(root, width=1).grid(row=8, column=0)
Entry(root, width = 40, textvariable = cfpassword).grid(row=8,column=1)
Label(root, width=1).grid(row=8, column=2)

#Phần số điện thoại
Label(root, width=1).grid(row=9, column=0)
Label(root, text = 'Số điện thoại'.ljust(42), font = 'tahoma', justify = LEFT).grid(row=9,column=1)
Label(root, width=1).grid(row=9, column=2)

Label(root, width=1).grid(row=10, column=0)
Entry(root, width = 40, textvariable = number).grid(row=10,column=1)
Label(root, width=1).grid(row=10, column=2)

#Phần địa chỉ
Label(root, width=1).grid(row=11, column=0)
Label(root, text = 'Nhập địa chỉ'.ljust(42), font = 'tahoma', justify = LEFT).grid(row=11,column=1)
Label(root, width=1).grid(row=11, column=2)

Label(root, width=1).grid(row=12, column=0)
Entry(root, width = 40, textvariable = address).grid(row=12,column=1)
Label(root, width=1).grid(row=12, column=2)

#Nút tạo tài khoản
Label(root, height=0, textvariable = inform).grid(row=13, columnspan=3)
Button(root, text='TẠO TÀI KHOẢN', font = ('timenewroman', 10), relief = RAISED, bg = 'blue', fg = 'white', borderwidth=0, command = checkemail).grid(row = 14, column=1)

root.mainloop()