"""
 Author: Maola Sirzul
 Date started:1/10/2020
Version:1.0
Description: Payment  processing for AllAroundToys
"""

# Importing files from tkinter to make the GUI
from tkinter import *
import sqlite3
from tkinter import font, messagebox
# Making the  screen as global
global screen

root = Tk()

# ==============DATABASE 1 for sales transaction=======
# Connecting the database with gui
connect = sqlite3.connect('sales transaction.db')
cursor = connect.cursor()
# Making the table to insert the data in correct order
cursor.execute("""CREATE TABLE IF NOT EXISTS users_card(card_number INTEGER, name_on_card TEXT, expiry_date INTEGER,
billing_address TEXT, post_code INTEGER, city TEXT, country TEXT)""")
connect.commit()
connect.close()

# ===============Messagebox==========================
# Messagebox for submit button commands
def submit():
    # messagebox.showinfo("VISACheck emulator", "Your payment method has been verified")
    messagebox._show("VISACheck emulator", "Your payment method has been verified")

    # Messagebox for cancel button commands


def cancel():
    messagebox.showinfo("VISACheck emulator", "Your payment method has been unverified")

# ======================= class for PAYMENT (F3:Sub-feature)================
class Payment_process(object):
    """This class will make a window with
    all the function required"""
    def __init__(self, master):
        self.root = master

        master.title("Welcome to AllAroundToys")  # title for first window
        master.geometry("800x650")

        self.font_large = font.Font(family='Georgia',
                                    size='24',
                                    weight='bold')
        self.font_small = font.Font(family='Georgia',
                                    size='12')
        #  colour Variables
        bg_color = "#000000"
        fg_color = "red"
        # Database variables
        self.card_number = StringVar()
        self.name_on_card = StringVar()
        self.expiry_date = StringVar()
        self.billing_address = StringVar()
        self.post_code = StringVar()
        self.city = StringVar()
        self.country = StringVar()
        # =============================Main frame==================
        # This function for title frame
        Label(self.root, text="Payment Information", bd=12, relief=RAISED, fg=fg_color, bg=bg_color,
              font=("Calibre", 36, "bold"), pady=3).pack(fill=X)
        self.payment_detail_frame = Frame(master)
        self.payment_detail_frame.pack(fill='both', expand=1)
        Button_for_submit = Button(self.payment_detail_frame, text="Save", font=("arial", 18, "bold"),
                                   height=2, width=15, bg='silver', fg="blue", command=self.save)
        Button_for_submit.place(x=30, y=480)
        # ==================Adding frame==================
        # Adding a heading name
        lbl_heading_work = Label(self.payment_detail_frame,
                                 text='Payment Details',
                                 font=self.font_large)
        lbl_heading_work.pack()
        Label(self.payment_detail_frame, text="Card Number:", font=("arial", 22, "bold"),
              height=2, width=20, bg='silver', fg='blue').place(x=20, y=50)

        Label(self.payment_detail_frame, text="Name on card:", font=("arial", 22, "bold"),
              height=2, width=20, bg='silver', fg='blue').place(x=20, y=110)

        Label(self.payment_detail_frame, text="Expiry Date:", font=("arial", 22, "bold"),
              height=2, width=20, bg='silver', fg='blue').place(x=20, y=170)

        Label(self.payment_detail_frame, text="Billing address:", font=("arial", 22, "bold"),
              height=2, width=20, bg='silver', fg='blue').place(x=20, y=230)

        Label(self.payment_detail_frame, text="Post Code:", font=("arial", 22, "bold"),
              height=2, width=20, bg='silver', fg='blue').place(x=20, y=290)

        Label(self.payment_detail_frame, text="City:", font=("arial", 22, "bold"),
              height=2, width=20, bg='silver', fg='blue').place(x=20, y=350)

        Label(self.payment_detail_frame, text="Country:", font=("arial", 22, "bold"),
              height=2, width=20, bg='silver', fg='blue').place(x=20, y=410)
        # ===================Adding Button=============================
        # Buttons for submit or cancel payment process
        Button_for_cancel = Button(self.payment_detail_frame, text="Cancel", font=("arial", 18, "bold"), height=2,
                                   width=15,
                                   bg='silver', fg="blue", command=quit)
        Button_for_cancel.place(x=280, y=480)
        Button_for_verify = Button(self.payment_detail_frame, text="verify", font=("arial", 18, "bold"), height=2,
                                   width=15,
                                   bg='silver', fg="blue", command=submit)
        Button_for_verify.place(x=480, y=480)
        # ==================Adding entry============================
        # Entry for payment details
        month_entry = Entry(self.payment_detail_frame, textvariable=self.expiry_date)
        month_entry.place(x=290, y=170)

        entry_card_number = Entry(self.payment_detail_frame, textvariable=self.card_number)
        entry_card_number.place(x=300, y=50)
        entry_name = Entry(self.payment_detail_frame, textvariable=self.name_on_card)
        entry_name.place(x=300, y=110)
        entry_billing_address = Entry(self.payment_detail_frame, textvariable=self.billing_address)
        entry_billing_address.place(x=300, y=240)
        entry_postcode = Entry(self.payment_detail_frame, textvariable=self.post_code)
        entry_postcode.place(x=300, y=300)
        entry_city = Entry(self.payment_detail_frame, textvariable=self.city)
        entry_city.place(x=300, y=360)
        entry_country = Entry(self.payment_detail_frame, textvariable=self.country)
        entry_country.place(x=300, y=420)

    # Making a function which can be applied in button
    def save(self):
        """This function will save the customer
         bank details into the database"""
        connecting = sqlite3.connect('sales transaction.db')
        cursor = connecting.cursor()

        cursor.execute(
            "INSERT INTO users_card VALUES (:card_number, :name_on_card , :expiry_date, :billing_address, :post_code, "
            ":city, :country)",
            {'card_number': self.card_number.get(), 'name_on_card': self.name_on_card.get(),
             'expiry_date': self.expiry_date.get(), 'billing_address': self.billing_address.get(),
             'post_code': self.post_code.get(), 'city': self.city.get(), 'country': self.country.get()})

        connecting.commit()


if __name__ == "__main__":
    Object = Payment_process(root)
    root.mainloop()
