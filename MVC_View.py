from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pyodbc
from pubsub import pub


class View:
    def __init__(self, parent):
        # Initialize variables
        self.root = parent

        # create customer windows variable
        self.crmakh_var = StringVar()
        self.crhoten_var = StringVar()
        self.crngaysinh_var = StringVar()
        self.crgioitinh_var = StringVar()

        self.crdienthoai_var = StringVar()
        self.crdiachi_var = StringVar()

        # create customer windows variable
        self.vimakh_var = StringVar()
        self.vihoten_var = StringVar()
        self.vingaysinh_var = StringVar()
        self.vigioitinh_var = StringVar()

        self.vidienthoai_var = StringVar()
        self.vidiachi_var = StringVar()
        return

    def setup(self):
        """Call methods to setup the User Interface."""
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        """Create various widgets in the tkinter main window."""
        # Set up frames
        # ========== = Frame button on the head = ==========
        self.framebutton = Frame(self.root, bd=4, relief='ridge')
        self.bdk = Button(self.framebutton, text='BẢNG ĐIỀU KHIỂN', border=2, relief='ridge', fg='white', bg='#FF4500',
                          width=15, font=('tahoma', 20, 'bold'))
        self.nv = Button(self.framebutton, text='NHÂN VIÊN', border=2, relief='ridge', fg='white', bg='green', width=15,
                         font=('tahoma', 20, 'bold'))
        self.tt = Button(self.framebutton, text='THÔNG TIN', border=2, relief='ridge', fg='white', bg='purple',
                         width=15, font=('tahoma', 20, 'bold'))
        self.framebutton['bg'] = 'blue'

        # ========== = Frame Search Customer = ==========
        self.search_var = StringVar()
        self.framesearch = Frame(self.root)
        self.search_entry = ttk.Entry(self.framesearch, textvariable=self.search_var, width=35, font=('tahoma', 12))
        self.search_button = ttk.Button(self.framesearch, text='Search', command=self.search)

        # ========== = Frame Customer's Information Tabel = ==========
        self.table_frame = Frame(self.root, bd=2, relief='ridge')

        self.xscroll = ttk.Scrollbar(self.table_frame, orient='horizontal')
        self.yscroll = ttk.Scrollbar(self.table_frame, orient='vertical')

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("Treeview", background='white', foreground='black', rowheight=22, fieldbackground='white')
        self.style.map("Treeview", background=[('selected', '#344DF5')])

        self.library_table = ttk.Treeview(self.table_frame, column=("maso", "hoten", "namsinh", "gioitinh", "dienthoai"),
                                          xscrollcommand=self.xscroll.set, yscrollcommand=self.yscroll.set)

        self.xscroll.config(command=self.library_table.xview)
        self.yscroll.config(command=self.library_table.yview)

        self.library_table.heading("maso", text='Mã số')
        self.library_table.heading("hoten", text='Họ tên')
        self.library_table.heading("namsinh", text='Năm sinh')
        self.library_table.heading("gioitinh", text='Giới tính')
        self.library_table.heading("dienthoai", text='Điện thoại')

        self.library_table["show"] = "headings"

        self.library_table.column("maso", width=50, anchor='center')
        self.library_table.column("hoten", width=150)
        self.library_table.column("namsinh", width=80, anchor='center')
        self.library_table.column("gioitinh", width=60, anchor='center')
        self.library_table.column("dienthoai", width=100, anchor='e')

        self.library_table.bind('<ButtonRelease-1>', self.select_item)

        # =============================Frame Bill List Table================================
        self.bill_frame = Frame(self.root, bd=2, relief='ridge')

        self.y_scroll = ttk.Scrollbar(self.bill_frame, orient='vertical')

        self.bill_table = ttk.Treeview(self.bill_frame, column=("maso", "khachhang", "ngaylap", "thanhtien", "tinhtrang"),
                                       yscrollcommand=self.y_scroll.set)

        self.y_scroll.config(command=self.bill_table.yview)

        self.bill_table.heading("maso", text='Mã số')
        self.bill_table.heading("khachhang", text='Khách hàng')
        self.bill_table.heading("ngaylap", text='Ngày lập')
        self.bill_table.heading("thanhtien", text='Thành tiền')
        self.bill_table.heading("tinhtrang", text='Tình trạng')

        self.bill_table["show"] = "headings"

        self.bill_table.column("maso", width=40, anchor='center')
        self.bill_table.column("khachhang", width=140)
        self.bill_table.column("ngaylap", width=100, anchor='center')
        self.bill_table.column("thanhtien", width=60, anchor='w')
        self.bill_table.column("tinhtrang", width=110)

        # =================Button To Open The Create/View/Delete Customer Windows====================
        self.create_cus = Button(self.root, text="Tạo", font=('tahoma', 12), bg="#A9A9A9", relief="solid",
                            command=self.create_customer_windows)

        self.delete_cus = Button(self.root, text="Xóa", font=('tahoma', 12), bg="#A9A9A9", relief="solid",
                            command=self.delete_customer_windows)

        self.view_cus = Button(self.root, text="Xem", font=('tahoma', 12), bg="#A9A9A9", relief="solid",
                            command=self.view_customer_windows)

    def search(self):
        pub.sendMessage("Searching_Button_Pressed") # Sending message

    def select_item(self, item):
        pub.sendMessage("Select_Item_Pressed") # Sending message

    def create_customer_windows(self):
        """
        Windows to create a new customer
        """
        self.create_win = Toplevel()
        self.create_win.title("Tạo mới khách hàng")
        self.create_win.geometry("800x600")
        Label(self.create_win, text='Tạo mới khách hàng', font=('tahoma', 30, 'bold'), relief='groove').pack()

        Label(self.create_win, text='Thông tin cơ bản', font=('tahoma', 15)).place(x=320, y=70)

        self.crmakh = Label(self.create_win, text='Mã khách hàng:', font=('tahoma', 13)).place(x=20, y=110)
        self.crentry_makh = Entry(self.create_win, width = 80, font=('tahoma', 13),
                                  textvariable=self.crmakh_var).place(x=20, y=140)
        self.crhoten = Label(self.create_win, text='Họ tên:', font=('tahoma', 13)).place(x=20, y=170)
        self.crentry_hoten = Entry(self.create_win, width=80, font=('tahoma', 13),
                                   textvariable=self.crhoten_var).place(x=20, y=200)
        self.crngaysinh = Label(self.create_win, text='Ngày sinh (ngày/tháng/năm):', font=('tahoma', 13)).place(x=20, y=230)
        self.crentry_ngaysinh = Entry(self.create_win, width=80, font=('tahoma', 13),
                                      textvariable=self.crngaysinh_var).place(x=20, y=260)
        self.crgioitinh = Label(self.create_win, text='Giới tính:', font=('tahoma', 13)).place(x=20, y=290)
        self.crentry_gioitinh = ttk.Combobox(self.create_win, width=78, font=('tahoma', 13), values =('Nam', 'Nữ'),
                                              textvariable=self.crgioitinh_var).place(x=20, y=320)

        Label(self.create_win, text='Thông tin liên hệ', font=('tahoma', 15)).place(x=320, y=360)

        self.crdienthoai = Label(self.create_win, text='Điện thoại:', font=('tahoma', 13)).place(x=20, y=400)
        self.crentry_dienthoai = Entry(self.create_win, width=80, font=('tahoma', 13),
                                       textvariable=self.crdienthoai_var).place(x=20, y=430)
        self.crdiachi = Label(self.create_win, text='Địa chỉ:', font=('tahoma', 13)).place(x=20, y=460)
        self.crentry_diachi = Entry(self.create_win, width=80, font=('tahoma', 13),
                                    textvariable=self.crdiachi_var).place(x=20, y=490)

        self.crluu = Button(self.create_win, text="Lưu", font=('tahoma', 12), bg="#A9A9A9", relief="solid", width=5,
                                 command=self.save_customer).place(x=620, y=540)

        self.crdong = Button(self.create_win, text="Đóng", font=('tahoma', 12), bg="#A9A9A9", relief="solid", width=5,
                                 command=self.closeornot).place(x=690, y=540)

    def save_customer(self):
        pub.sendMessage("save_customer_pressed")  # Sending message

    def closeornot(self):
        response = messagebox.askyesno("Warning!", "Bạn có chắc muốn thoát?")
        if response:
            self.create_win.destroy()

    def delete_customer_windows(self):
        # Delete a customer
        pub.sendMessage("delete_customer_pressed")

    def view_customer_windows(self):
        """
        Windows to View/Update a new customer
        """
        curItem = self.library_table.item(self.library_table.focus())
        if curItem['values']:
            self.create_win = Toplevel()
            self.create_win.title("Thông tin khách hàng")
            self.create_win.geometry("800x600")
            Label(self.create_win, text='Thông tin khách hàng', font=('tahoma', 30, 'bold'), relief='groove').pack()

            Label(self.create_win, text='Thông tin cơ bản', font=('tahoma', 15)).place(x=320, y=70)

            self.vimakh = Label(self.create_win, text='Mã khách hàng:', font=('tahoma', 13)).place(x=20, y=110)
            self.vientry_makh = Entry(self.create_win, width=80, font=('tahoma', 13),
                                      textvariable=self.vimakh_var).place(x=20, y=140)
            self.vihoten = Label(self.create_win, text='Họ tên:', font=('tahoma', 13)).place(x=20, y=170)
            self.vientry_hoten = Entry(self.create_win, width=80, font=('tahoma', 13),
                                       textvariable=self.vihoten_var).place(x=20, y=200)
            self.vingaysinh = Label(self.create_win, text='Ngày sinh (ngày/tháng/năm):', font=('tahoma', 13)).place(x=20,
                                                                                                                    y=230)
            self.vientry_ngaysinh = Entry(self.create_win, width=80, font=('tahoma', 13),
                                          textvariable=self.vingaysinh_var).place(x=20, y=260)
            self.vigioitinh = Label(self.create_win, text='Giới tính:', font=('tahoma', 13)).place(x=20, y=290)
            self.vientry_gioitinh = ttk.Combobox(self.create_win, width=78, font=('tahoma', 13), values=('Nam', 'Nữ'),
                                                 textvariable=self.vigioitinh_var).place(x=20, y=320)

            Label(self.create_win, text='Thông tin liên hệ', font=('tahoma', 15)).place(x=320, y=360)

            self.vidienthoai = Label(self.create_win, text='Điện thoại:', font=('tahoma', 13)).place(x=20, y=400)
            self.vientry_dienthoai = Entry(self.create_win, width=80, font=('tahoma', 13),
                                           textvariable=self.vidienthoai_var).place(x=20, y=430)
            self.vidiachi = Label(self.create_win, text='Địa chỉ:', font=('tahoma', 13)).place(x=20, y=460)
            self.vientry_diachi = Entry(self.create_win, width=80, font=('tahoma', 13),
                                        textvariable=self.vidiachi_var).place(x=20, y=490)

            self.viluu = Button(self.create_win, text="Lưu", font=('tahoma', 12), bg="#A9A9A9", relief="solid", width=5,
                                command=self.change_customer).place(x=620, y=540)

            self.vidong = Button(self.create_win, text="Đóng", font=('tahoma', 12), bg="#A9A9A9", relief="solid", width=5,
                                 command=self.closeornot).place(x=690, y=540)

            pub.sendMessage("show_item")



    def change_customer(self):
        pub.sendMessage("change_customer_pressed")

    def setup_layout(self):
        # Pack all frame
        self.framebutton.pack(side='top', fill='x')
        self.framesearch.place(x=20, y=110)
        self.table_frame.place(x=15, y=160, width=405, height=420)
        self.bill_frame.place(x=450, y=160, width=730, height=420)
        # Pack widget
        self.bdk.pack(side='left', padx=5)
        self.nv.pack(side='left', padx=5, pady=10)
        self.tt.pack(side='left', padx=5, pady=10)

        self.search_entry.pack(side='left')
        self.search_button.pack(side='left')

        self.xscroll.pack(side='bottom', fill='x')
        self.yscroll.pack(side='right', fill='y')
        self.library_table.pack(fill='both', expand=1)

        self.y_scroll.pack(side='right', fill='y')
        self.bill_table.pack(fill='both', expand=1)
        # Pack changing customer buttom
        self.create_cus.place(x=15, y=600, width=50)
        self.delete_cus.place(x=305, y=600, width=50)
        self.view_cus.place(x=370, y=600, width=50)
# Test run
if __name__ == "__main__":
    root = Tk()
    root.title('Dental Clinic Management')
    root.geometry('1200x680')
    root.resizable(False, False)
    view = View(root)
    view.setup()
    root.mainloop()