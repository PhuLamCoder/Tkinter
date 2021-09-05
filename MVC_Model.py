from pubsub import pub
from tkinter import messagebox
import pyodbc
from MVC_View import View

class Model:
    def __init__(self):
        return

    def load_search(self, library_table, search_var):
        """
                Show the customer info when searching their name
                """
        if search_var.get().strip == '':
            self.fatch_data()
        else:
            conn = pyodbc.connect('Driver={SQL Server};'
                                  'Server=DESKTOP-3PB63QQ\PHULAMCODER;'
                                  'Database=DentalManagement;'
                                  'Trusted_Connection=yes;')
            my_cursor = conn.cursor()
            my_cursor.execute(
                f"select MaKH, HoTen, format(NgaySinh, 'dd/MM/yyyy'), GioiTinh, Dienthoai from DentalManagement.dbo.Customer where HoTen like N'%{search_var.get().strip()}%'")
            rows = my_cursor.fetchall()
            if len(rows) != 0 or True:
                library_table.delete(*library_table.get_children())
                count = 0
                for i in rows:
                    if count % 2 == 0:
                        library_table.insert(parent='', index='end', text='',
                                                  values=(i[0], i[1], i[2], i[3], i[4]), tags=("evenrow",))
                    else:
                        library_table.insert(parent='', index='end', text='',
                                                  values=(i[0], i[1], i[2], i[3], i[4]), tags=("oodrow",))
                    count += 1
                conn.commit()
            conn.close()

    def select_item(self, library_table, bill_table):
        """
                Select MaKH of customer table and convert info into the bill table
                """
        curItem = library_table.item(library_table.focus())
        MaKH = curItem['values'][0]
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-3PB63QQ\PHULAMCODER;'
                              'Database=DentalManagement;'
                              'Trusted_Connection=yes;')

        my_cursor = conn.cursor()
        my_cursor.execute(f"select MaHD, HoTen, format(Ngaylap,'dd/MM/yyyy'), Tongtrigia, tinhtrang from \
                     DentalManagement.dbo.hoadon as a,DentalManagement.dbo.customer as b where a.makh = b.makh and a.makh = {MaKH}")
        rows = my_cursor.fetchall()
        bill_table.delete(*bill_table.get_children())
        for i in rows:
            bill_table.insert(parent='', index='end', text='', values=(i[0], i[1], i[2], i[3], i[4]))
        conn.commit()
        conn.close()

    def fatch_data(self, library_table):
        """
        Show the data in SQL server in the table customer information
        """
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-3PB63QQ\PHULAMCODER;'
                              'Database=DentalManagement;'
                              'Trusted_Connection=yes;')

        my_cursor = conn.cursor()
        my_cursor.execute("select MaKH, HoTen, format(NgaySinh, 'dd/MM/yyyy'), GioiTinh, Dienthoai from DentalManagement.dbo.Customer")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            library_table.delete(*library_table.get_children())
            library_table.tag_configure("oddrow", background="white")
            library_table.tag_configure("evenrow", background="lightblue")
            for i in rows:
                if i[0] % 2 == 0:
                    library_table.insert(parent='', index='end', text='', values=(i[0], i[1], i[2], i[3], i[4]),
                                              tags=("evenrow",))
                else:
                    library_table.insert(parent='', index='end', text='', values=(i[0], i[1], i[2], i[3], i[4]),
                                              tags=("oodrow",))
            conn.commit()
        conn.close()

    def show_all_bill(self, bill_table):
        """
        Show all bill of customer in the bill_table
        """
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-3PB63QQ\PHULAMCODER;'
                              'Database=DentalManagement;'
                              'Trusted_Connection=yes;')

        my_cursor = conn.cursor()
        my_cursor.execute("select MaHD, HoTen, format(Ngaylap,'dd/MM/yyyy'), Tongtrigia, tinhtrang from \
                          DentalManagement.dbo.hoadon as a, DentalManagement.dbo.customer as b where a.makh = b.makh")
        rows = my_cursor.fetchall()
        bill_table.delete(*bill_table.get_children())
        for i in rows:
            bill_table.insert(parent='', index='end', text='', values=(i[0], i[1], i[2], i[3], i[4]))
        conn.commit()
        conn.close()

    def check_to_save(self, makh, hoten, ngaysinh, dienthoai, diachi, gioitinh):
        if makh.get().strip() == '' or hoten.get().strip() == '' or dienthoai.get().strip() == '':
            messagebox.showwarning("Warning!", "Không được để trống mã khách hàng, họ tên hoặc số điện thoại")
        elif (not dienthoai.get().strip().isdigit()) or not ((10<=len(dienthoai.get().strip()) <=11)):
            messagebox.showwarning("Warning!", "Số điện thoại không hợp lệ")
        else:
            ngsinh = ngaysinh.get().strip()
            ngsinh = ngsinh.split('/')
            ngsinh = ngsinh[2] + ngsinh[1] + ngsinh[0]

            conn = pyodbc.connect('Driver={SQL Server};'
                                  'Server=DESKTOP-3PB63QQ\PHULAMCODER;'
                                  'Database=DentalManagement;'
                                  'Trusted_Connection=yes;')

            my_cursor = conn.cursor()
            try:
                my_cursor.execute(f"insert into DentalManagement.dbo.Customer (makh, hoten, ngaysinh, dienthoai, diachi, gioitinh)\
                                   values ({makh.get()}, N'{hoten.get()}', '{ngsinh}', '{dienthoai.get()}', N'{diachi.get()}', N'{gioitinh.get()}')")

                conn.commit()
                conn.close()
                messagebox.showinfo('Message!', 'Tạo thành công!')
            except:
                messagebox.showwarning("Warning!", "Một vài thông tin không hợp lệ. Có thể Mã Khách hàng đã bị trùng")

    def delete_item(self, library_table):
        curItem = library_table.item(library_table.focus())
        if curItem['values']:
            response = messagebox.askyesno("Warning!", "Bạn có chắc muốn xóa khách hàng này?")
            if response:
                MaKH = curItem['values'][0]
                conn = pyodbc.connect('Driver={SQL Server};'
                                      'Server=DESKTOP-3PB63QQ\PHULAMCODER;'
                                      'Database=DentalManagement;'
                                      'Trusted_Connection=yes;')

                my_cursor = conn.cursor()
                my_cursor.execute(f"delete DentalManagement.dbo.hoadon where MaKH = {MaKH}")
                my_cursor.execute(f"delete DentalManagement.dbo.customer where MaKH = {MaKH}")
                conn.commit()
                conn.close()

    def show_item(self, library_table, makh, hoten, ngaysinh, gioitinh, dienthoai, diachi):
        curItem = library_table.item(library_table.focus())
        if curItem['values']:
            MaKH = curItem['values'][0]
            conn = pyodbc.connect('Driver={SQL Server};'
                                  'Server=DESKTOP-3PB63QQ\PHULAMCODER;'
                                  'Database=DentalManagement;'
                                  'Trusted_Connection=yes;')

            my_cursor = conn.cursor()
            my_cursor.execute(f"select * from DentalManagement.dbo.customer where makh = {MaKH}")
            rows = my_cursor.fetchall()
            makh.set(rows[0][0])
            hoten.set(rows[0][1])
            ngaysinh.set(rows[0][2][-2:] + "/"+rows[0][2][-5:-3] + "/" + rows[0][2][0:4])
            gioitinh.set(rows[0][5])
            dienthoai.set(rows[0][3])
            diachi.set(rows[0][4])
            conn.commit()
            conn.close()

    def change_item(self, library_table, makh, hoten, ngaysinh, gioitinh, dienthoai, diachi):
        curItem = library_table.item(library_table.focus())
        MaKH = curItem['values'][0]
        if makh.get().strip() == '' or hoten.get().strip() == '' or dienthoai.get().strip() == '':
            messagebox.showwarning("Warning!", "Không được để trống mã khách hàng, họ tên hoặc số điện thoại")
        elif (not dienthoai.get().strip().isdigit()) or not ((10<=len(dienthoai.get().strip()) <=11)):
            messagebox.showwarning("Warning!", "Số điện thoại không hợp lệ")
        else:
            ngsinh = ngaysinh.get().strip()
            ngsinh = ngsinh.split('/')
            ngsinh = ngsinh[2] + ngsinh[1] + ngsinh[0]

            conn = pyodbc.connect('Driver={SQL Server};'
                                  'Server=DESKTOP-3PB63QQ\PHULAMCODER;'
                                  'Database=DentalManagement;'
                                  'Trusted_Connection=yes;')

            my_cursor = conn.cursor()
            try:
                my_cursor.execute(f"update DentalManagement.dbo.Customer set makh={makh.get()}, hoten =N'{hoten.get()}',\
                                   ngaysinh='{ngsinh}', dienthoai='{dienthoai.get()}', diachi=N'{diachi.get()}', \
                                    gioitinh = N'{gioitinh.get()}' where makh ={MaKH}")

                conn.commit()
                conn.close()
                messagebox.showinfo('Message!', 'Lưu thành công!')
            except:
                messagebox.showwarning("Warning!", "Một vài thông tin không hợp lệ. Có thể Mã Khách hàng đã bị trùng")




