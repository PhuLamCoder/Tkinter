from tkinter import *

def checkname() :
    flag = True
    name = namee.get().strip()
    size = len(name)
    if size < 10 :
        flag = False
    else:
        for i in range(size) :
            if 'a' <= name[i].lower() <= 'z' or name[i].lower() == 'ê' or name[i].lower() == 'ư' or name[i].lower() == 'ô' or name[i].lower() == 'ơ' or name[i].lower() == 'ă' or name[i].lower() == 'â' or name[i].lower() == 'đ' or name[i].lower() == ' ' :
                flag = True
            elif name[i].lower() == 'ế' or name[i].lower() == 'ứ' or name[i].lower() == 'ố' or name[i].lower() == 'ớ' or name[i].lower() == 'ắ' or name[i].lower() == 'ấ' or name[i].lower() == 'ó' or name[i].lower() == 'á' or name[i].lower() == 'é' or name[i].lower() == 'ú' or name[i].lower() == 'í' or name[i].lower() == 'ý' :
                flag = True
            elif name[i].lower() == 'ề' or name[i].lower() == 'ừ' or name[i].lower() == 'ồ' or name[i].lower() == 'ờ' or name[i].lower() == 'ằ' or name[i].lower() == 'ầ' or name[i].lower() == 'ò' or name[i].lower() == 'à' or name[i].lower() == 'è' or name[i].lower() == 'ù' or name[i].lower() == 'ì' or name[i].lower() == 'ỳ' :
                flag = True
            elif name[i].lower() == 'ể' or name[i].lower() == 'ử' or name[i].lower() == 'ổ' or name[i].lower() == 'ở' or name[i].lower() == 'ẳ' or name[i].lower() == 'ẩ' or name[i].lower() == 'ỏ' or name[i].lower() == 'ả' or name[i].lower() == 'ẻ' or name[i].lower() == 'ủ' or name[i].lower() == 'ỉ' or name[i].lower() == 'ỷ' :
                flag = True
            elif name[i].lower() == 'ễ' or name[i].lower() == 'ữ' or name[i].lower() == 'ỗ' or name[i].lower() == 'ỡ' or name[i].lower() == 'ẵ' or name[i].lower() == 'ẫ' or name[i].lower() == 'õ' or name[i].lower() == 'ã' or name[i].lower() == 'ẽ' or name[i].lower() == 'ũ' or name[i].lower() == 'ĩ' or name[i].lower() == 'ỹ' :
                flag = True
            elif name[i].lower() == 'ễ' or name[i].lower() == 'ữ' or name[i].lower() == 'ỗ' or name[i].lower() == 'ỡ' or name[i].lower() == 'ẵ' or name[i].lower() == 'ẫ' or name[i].lower() == 'õ' or name[i].lower() == 'ã' or name[i].lower() == 'ẽ' or name[i].lower() == 'ũ' or name[i].lower() == 'ĩ' or name[i].lower() == 'ỹ' :
                flag = True
            elif name[i].lower() == 'ệ' or name[i].lower() == 'ự' or name[i].lower() == 'ộ' or name[i].lower() == 'ợ' or name[i].lower() == 'ặ' or name[i].lower() == 'ậ' or name[i].lower() == 'ọ' or name[i].lower() == 'ạ' or name[i].lower() == 'ẹ' or name[i].lower() == 'ụ' or name[i].lower() == 'ị' or name[i].lower() == 'ị' :
                flag = True
            else:
                flag = False
                break
    if flag == False :
        Label(root, text = 'Vui lòng nhập đúng format Tên!', font =('tahoma', 8), fg ='red').grid(row=13, columnspan=3)
    else:
        Label(root, text = ' '*60).grid(row=13, columnspan=3)
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
        Label(root, text = 'Vui lòng nhập đúng format Email!', font =('tahoma', 8), fg ='red').grid(row=13, columnspan=3)
    else:
        Label(root, text = ' '*60).grid(row=13, columnspan=3)
    return flag
def checkpassword() :
    flag = True
    pword = password.get().strip()
    size = len(pword)
    dem = 0
    if size > 30 or size < 5 :
        flag = False
    else :
        for i in range(size) :
            if 'A' <= pword[i] <= 'Z' :
                dem += 1
        if dem == 0 :
            flag = False
    if flag == False :
        Label(root, text = 'Vui lòng nhập đúng format Mật khẩu!', font =('tahoma', 8), fg ='red').grid(row=13, columnspan=3)
    else:
        Label(root, text = ' '*60).grid(row=13, columnspan=3)
    return flag
def checkpwagain() :
    flag = True
    pword = password.get().strip()
    cfpword = cfpassword.get().strip()
    if cfpword != pword :
        flag = False
    if flag == False :
        Label(root, text = 'Vui lòng nhập đúng format và giống với Mật khẩu!', font =('tahoma', 8), fg ='red').grid(row=13, columnspan=3)
    else:
        Label(root, text = ' '*100).grid(row=13, columnspan=3)
    return flag
def checknumber() :
    nber = number.get().strip()
    flag = True
    size = len(nber)
    if size <= 1 or size > 11 :
        flag = False
    else:
        for i in range(size) :
            if not nber[i] in ('0','1','2','3','4','5','6','7','8','9') :
                flag = False
                break
    if flag == False :
        Label(root, text = 'Vui lòng nhập đúng format Số điện thoại!', font =('tahoma', 8), fg ='red').grid(row=13, columnspan=3)
    else:
        Label(root, text = ' '*100).grid(row=13, columnspan=3)
    return flag
def checkaddress() :
    adr = address.get().strip()
    size = len(adr)
    flag = True
    if size == 0 or size > 50 :
        flag =False
    if flag == False :
        Label(root, text = 'Vui lòng nhập không quá giới hạn 50 ký tự!', font =('tahoma', 8), fg ='red').grid(row=13, columnspan=3)
    else:
        Label(root, text = ' '*100).grid(row=13, columnspan=3)
    return flag

def multiaction() :
    flag = False
    if checkname():
        if checkemail():
            if checkpassword():
                if checkpwagain():
                    if checknumber():
                        if checkaddress() :
                            flag = True
    if flag :
        Label(root, text = 'Đăng kí thành công!', font =('tahoma', 8), fg ='green').grid(row=13, columnspan=3)
root = Tk()
root.title('Register')
root.minsize(height=360, width=270)

#textvariable
namee = StringVar()
email = StringVar()
password = StringVar()
cfpassword = StringVar()
number = StringVar()
address = StringVar()
inform = StringVar()

# Tiêu đề
Label(root, text='Đăng ký tài khoản', font = ('tahoma', 16, 'bold'),width=28, justify = CENTER, bg = 'blue', fg = 'white').grid(row=0, column=0, columnspan=3)

# Phần Tên
Label(root, width=3).grid(row=1, column=0)
Label(root, text = 'Tên'.ljust(58), font = 'tahoma', justify = LEFT).grid(row=1,column=1)
Label(root, width=3).grid(row=1, column=2)

Label(root, width=3).grid(row=2, column=0)
Entry(root, width = 50, textvariable = namee).grid(row=2,column=1)
Label(root, width=3).grid(row=2, column=2)

#Phần Email
Label(root, width=3).grid(row=3, column=0)
Label(root, text = 'Email'.ljust(58), font = 'tahoma', justify = LEFT).grid(row=3,column=1)
Label(root, width=3).grid(row=3, column=2)

Label(root, width=3).grid(row=4, column=0)
Entry(root, width = 50, textvariable = email).grid(row=4,column=1)
Label(root, width=3).grid(row=4, column=2)

#Phần Mật Khẩu
Label(root, width=3).grid(row=5, column=0)
Label(root, text = 'Mật khẩu'.ljust(56), font = 'tahoma', justify = LEFT).grid(row=5,column=1)
Label(root, width=3).grid(row=5, column=2)

Label(root, width=3).grid(row=6, column=0)
Entry(root, width = 50, textvariable = password, show='*').grid(row=6,column=1)
Label(root, width=3).grid(row=6, column=2)

#Phần xác nhận mật khẩu
Label(root, width=3).grid(row=7, column=0)
Label(root, text = 'Xác nhận mật khẩu'.ljust(50), font = 'tahoma', justify = LEFT).grid(row=7,column=1)
Label(root, width=3).grid(row=7, column=2)

Label(root, width=3).grid(row=8, column=0)
Entry(root, width = 50, textvariable = cfpassword, show='*').grid(row=8,column=1)
Label(root, width=3).grid(row=8, column=2)

#Phần số điện thoại
Label(root, width=3).grid(row=9, column=0)
Label(root, text = 'Số điện thoại'.ljust(55), font = 'tahoma', justify = LEFT).grid(row=9,column=1)
Label(root, width=3).grid(row=9, column=2)

Label(root, width=3).grid(row=10, column=0)
Entry(root, width = 50, textvariable = number).grid(row=10,column=1)
Label(root, width=3).grid(row=10, column=2)

#Phần địa chỉ
Label(root, width=3).grid(row=11, column=0)
Label(root, text = 'Nhập địa chỉ'.ljust(55), font = 'tahoma', justify = LEFT).grid(row=11,column=1)
Label(root, width=3).grid(row=11, column=2)

Label(root, width=3).grid(row=12, column=0)
Entry(root, width = 50, textvariable = address).grid(row=12,column=1)
Label(root, width=3).grid(row=12, column=2)

#Nút tạo tài khoản
Label(root).grid(row=13, columnspan=3)
Button(root, text='TẠO TÀI KHOẢN', font = ('tahoma', 10), relief = RAISED, bg = 'blue', fg = 'white', borderwidth=0, command = multiaction).grid(row = 14, column=1)

root.mainloop()