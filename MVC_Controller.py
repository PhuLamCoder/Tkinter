from MVC_View import View
from MVC_Model import Model
from tkinter import *
from pubsub import pub

class Controller:
    def __init__(self, parent): # Parent is the tkinter main window
        # Initialize variables
        self.root = parent
        self.model = Model() # Point to model object
        self.view = View(parent) # Point to view object
        self.view.setup() # run the view setup()
        pub.subscribe(self.searching_button_press, "Searching_Button_Pressed")
        pub.subscribe(self.select_item_press, "Select_Item_Pressed")
        pub.subscribe(self.save_customer_press, "save_customer_pressed")
        pub.subscribe(self.delete_customer_press, "delete_customer_pressed")
        pub.subscribe(self.change_customer_press, "change_customer_pressed")
        pub.subscribe(self.show_item_press, "show_item")

        # Show table from database
        self.model.fatch_data(self.view.library_table)
        self.model.show_all_bill(self.view.bill_table)

    def searching_button_press(self):
        # This will call load_search method in Model
        self.model.load_search(self.view.library_table, self.view.search_var)

    def select_item_press(self):
        self.model.select_item(self.view.library_table, self.view.bill_table)

    def save_customer_press(self):
        self.model.check_to_save(self.view.crmakh_var, self.view.crhoten_var, self.view.crngaysinh_var, self.view.crdienthoai_var,
                                 self.view.crdiachi_var, self.view.crgioitinh_var)
        self.model.fatch_data(self.view.library_table)

    def delete_customer_press(self):
        self.model.delete_item(self.view.library_table)
        self.model.fatch_data(self.view.library_table)

    def show_item_press(self):
        self.model.show_item(self.view.library_table, self.view.vimakh_var,  self.view.vihoten_var, self.view.vingaysinh_var,
                             self.view.vigioitinh_var, self.view.vidienthoai_var, self.view.vidiachi_var)

    def change_customer_press(self):
        self.model.change_item(self.view.library_table, self.view.vimakh_var,  self.view.vihoten_var, self.view.vingaysinh_var,
                               self.view.vigioitinh_var, self.view.vidienthoai_var, self.view.vidiachi_var)
        self.model.fatch_data(self.view.library_table)

# Application entry point main method
if __name__ == "__main__":
    # Create instance of TK
    root = Tk()
    root.title('Dental Clinic Management')
    root.geometry('1200x680')
    root.resizable(False, False)

    app = Controller(root)
    root.mainloop()