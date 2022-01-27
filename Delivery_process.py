"""
 Author: Maola Sirzul
 Date started:8/1/2021
Version:1.0
Description: Delivery  processing for AllAroundToys
"""

# Importing files from tkinter to make the GUI
from tkinter import *
import sqlite3
from tkinter import font
# Making the  screen as global
global screen

# DATABASE 2 for customer address
# Connecting the database with gui
connect_delivery = sqlite3.connect('customer_addresses.db')
cursor = connect_delivery.cursor()
# Making the table to insert the data in correct order
cursor.execute("""CREATE TABLE IF NOT EXISTS address_information(address TEXT NOT NULL,
post_code INTEGER, city TEXT, country TEXT)""")
connect_delivery.commit()
connect_delivery.close()


# function for save and default button
def add_address():
    """This function will create a pop-up window"""
    global add_address
    add_address = Toplevel(root)
    add_address.title("Add items")
    add_address.geometry("250x100")
    Label(add_address, text=" Address saved Successfully ").pack()
    Button(add_address, text="ok", command=delete_add_address).pack()


# Delete popups
def delete_add_address():
    """This function will delete the pop-up window"""
    add_address.destroy()

# ======================= class for Check-out (F3:Sub-feature)================
class Delivery_process(object):
    """This class will make a window with
    all the function required"""
    def __init__(self, master):
        self.root = master

        # root.title("Welcome to AllAroundToys")  # title for first window
        # root.geometry("800x550")

        self.font_large = font.Font(family='Georgia',
                                    size='24',
                                    weight='bold')
        self.font_small = font.Font(family='Georgia',
                                    size='12')
        #  colour Variables
        bg_color = "#000000"
        fg_color = "red"
        # Database variables
        self.address = StringVar()
        self.post_code = StringVar()
        self.city = StringVar()
        self.country = StringVar()

        # This function for title frame
        Label(self.root, text="Delivery Information", bd=12, relief=RAISED, fg=fg_color, bg=bg_color,
              font=("Calibre", 36, "bold"), pady=3).pack(fill=X)
        self.delivery_information_frame = Frame(master)
        self.delivery_information_frame.pack(fill='both', expand=1)
        # Adding button for saving
        Button_for_submit = Button(self.delivery_information_frame, text="Save", font=("arial", 18, "bold"),
                                   height=2, width=15, bg='silver', fg="blue", command=add_address)
        Button_for_submit.place(x=30, y=380)
        # Adding a heading name
        lbl_heading_work = Label(self.delivery_information_frame,
                                 text='Delivery Details',
                                 font=self.font_large)
        lbl_heading_work.pack()
        Label(self.delivery_information_frame, text="1st line of address:", font=("arial", 22, "bold"),
              height=2, width=20, bg='silver', fg='blue').place(x=20, y=50)

        Label(self.delivery_information_frame, text="PostCode:", font=("arial", 22, "bold"),
              height=2, width=20, bg='silver', fg='blue').place(x=20, y=110)

        Label(self.delivery_information_frame, text="City:", font=("arial", 22, "bold"),
              height=2, width=20, bg='silver', fg='blue').place(x=20, y=170)

        Label(self.delivery_information_frame, text="Country::", font=("arial", 22, "bold"),
              height=2, width=20, bg='silver', fg='blue').place(x=20, y=230)

        # Buttons for submit or cancel payment process

        Button_for_cancel = Button(self.delivery_information_frame, text="Cancel", font=("arial", 18, "bold"), height=2,
                                   width=15,
                                   bg='silver', fg="blue", command=quit)
        Button_for_cancel.place(x=280, y=380)
        Button_for_default = Button(self.delivery_information_frame, text="Save as default", font=("arial", 18, "bold"),
                                    height=2,
                                    width=15,
                                    bg='silver', fg="blue", command=self.default)
        Button_for_default.place(x=480, y=380)

        # Entry for payment details

        city_entry = Entry(self.delivery_information_frame, textvariable=self.address)
        city_entry.place(x=300, y=50)
        postcode_entry = Entry(self.delivery_information_frame, textvariable=self.post_code)
        postcode_entry.place(x=300, y=110)
        city_entry = Entry(self.delivery_information_frame, textvariable=self.city)
        city_entry.place(x=290, y=170)
        country_entry = Entry(self.delivery_information_frame, textvariable=self.country)
        country_entry.place(x=300, y=240)

    # Making a function which can be applied in button
    def default(self):
        """This function will save the customer
         address details into the database"""
        connect = sqlite3.connect('customer_addresses.db')
        cursor_address = connect.cursor()

        cursor_address.execute(
            "INSERT INTO address_information VALUES (:address, :post_code , :city, :country)",
            {'address': self.address.get(), 'post_code': self.post_code.get(), 'city': self.city.get(),
             'country': self.country.get()})

        connect.commit()


if __name__ == "__main__":
    root = Tk()
    root.title("Welcome To ALLAroundToys")
    root.geometry("800x550")
    Object = Delivery_process(root)
    root.mainloop()
