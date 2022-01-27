"""
 Author: Maola Sirzul
 Date started:8/1/2021
Version:1.0
Description: Shopping basket processing for AllAroundToys
"""

# Importing files from tkinter to make the GUI
import os
import random
import sqlite3
import subprocess
import tempfile
from tkinter import *

# Making the  screen as global
global screen

root = Tk()


# =========== function for add products to shopping basket=========
def add_product():
    """This function will create a pop-up window"""
    global add_product
    add_product = Toplevel(root)
    add_product.title("Add items")
    add_product.geometry("800x650")
    Label(add_product, text=" Item Added Successfully ").pack()
    Button(add_product, text="ok", command=delete_add_item).pack()


# Delete popups
def delete_add_item():
    """This function will delete the pop-up window"""
    add_product.destroy()


# # function for delete items from shopping basket
def delete_product():
    """This function will create a pop-up window"""
    global delete_product
    delete_product = Toplevel(root)
    delete_product.title("Add items")
    delete_product.geometry("250x100")
    Label(delete_product, text=" Item Deleted Successfully ").pack()
    Button(delete_product, text="ok", command=delete_removed_item).pack()


# Delete popups
def delete_removed_item():
    """This function will delete the pop-up window"""
    delete_product.destroy()

# ======================= class for shopping basket and Generate sales receipt (F3:Sub-feature)================
class Shopping_basket(object):
    """This class will make a window with
    all the function required"""

    def __init__(self, master):
        self.root = master
        self.root.maxsize(width=1370, height=720)
        self.root.minsize(width=1370, height=720)
        self.root.title("Welcome To ALLAroundToys")

        # this function for variables
        self.customer_name = StringVar()
        self.customer_contact_number = StringVar()

        # this function for Generating Random Invoice Numbers
        x = random.randint(1, 9999)
        self.customer_reference_number = StringVar()

        # This function is to Set Value to a variable
        self.customer_reference_number.set(str(x))
        self.wooden_number_bus = IntVar()
        self.nosh_ark = IntVar()
        self.wooden_cars = IntVar()
        self.dall_house = IntVar()
        self.willow_farm_tractor = IntVar()
        self.total_price = StringVar()
        self.delivery_charge = StringVar()

        #  Variable for colour
        bg_color = "#000000"
        fg_color = "red"
        lbl_color = 'red'
        bg_color_1 = "gray"
        # ======================Main frame==========================
        # This function for title frame
        Label(self.root, text="Shopping Basket", bd=12, relief=RAISED, fg=fg_color, bg=bg_color,
              font=("Calibre", 36, "bold"), pady=3).pack(fill=X)
        # This function for Customers Frame
        frame_1 = LabelFrame(text="Customer Information", font=("Calibre", 12, "bold"), fg="gold", bg=bg_color,
                             relief=RAISED, bd=10)
        frame_1.place(x=0, y=80, relwidth=1)

        # This function for delivery frame (button + label)

        delivery_frame_btn = Button(frame_1, text="Change Address:", bg=bg_color, fg=fg_color,
                                    font=("lucid", 12, "bold"), bd=7, relief=RAISED,
                                    command=self.total_section)
        delivery_frame_btn.grid(row=0, column=1, ipady=4, ipadx=30, pady=5)

        change_address_lbl = Label(frame_1, text="Delivery option", bg=bg_color, fg=fg_color,
                                   font=("Calibre", 15, "bold"))
        change_address_lbl.grid(row=0, column=0, padx=10, pady=5)

        # This function for Payment frame (button + label)
        payment_frame_lbl = Label(frame_1, text="Payment option", bg=bg_color, fg=fg_color,
                                  font=("Calibre", 15, "bold"))
        payment_frame_lbl.grid(row=0, column=2, padx=20, pady=10)
        payment_frame_btn = Button(frame_1, text="Online Payment ", bg=bg_color, fg=fg_color,
                                   font=("lucid", 12, "bold"), bd=7, relief=RAISED)

        payment_frame_btn.grid(row=0, column=3, ipady=4, ipadx=30, pady=5)

        # This function for customer reference number
        customer_reference_number_lbl = Label(frame_1, text="Customer Reference Number: .", bg=bg_color, fg=fg_color,
                                              font=("Calibre", 15, "bold"))
        customer_reference_number_lbl.grid(row=0, column=4, padx=20)
        customer_reference_number_en = Entry(frame_1, bd=8, relief=RAISED, textvariable=self.customer_reference_number)
        customer_reference_number_en.grid(row=0, column=5, ipadx=30, ipady=4, pady=5)

        # This function for Toys Name Frame
        frame_2 = LabelFrame(self.root, text="Toy's Name", bd=10, relief=RAISED, bg=bg_color, fg="gold",
                             font=("Calibre", 13, "bold"))
        frame_2.place(x=5, y=180, width=325, height=380)

        # This function for Wooden Number bus(Product)
        wooden_number_bus_lbl = Label(frame_2, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color,
                                      text="Wooden Number Bus")
        wooden_number_bus_lbl.grid(row=0, column=0, padx=10, pady=20)
        wooden_number_entry = Entry(frame_2, bd=8, relief=RAISED, textvariable=self.wooden_number_bus)
        wooden_number_entry.grid(row=0, column=1, ipady=5, ipadx=5)

        # This function for Noah's Ark (product)
        nosh_ark_lbl = Label(frame_2, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color, text="Noah's Ark")
        nosh_ark_lbl.grid(row=1, column=0, padx=10, pady=20)
        nosh_ark_en = Entry(frame_2, bd=8, relief=RAISED, textvariable=self.nosh_ark)
        nosh_ark_en.grid(row=1, column=1, ipady=5, ipadx=5)

        # This function for wooden cars (product)
        wooden_cars_lbl = Label(frame_2, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color, text="Wooden cars")
        wooden_cars_lbl.grid(row=2, column=0, padx=10, pady=20)
        wooden_cars_en = Entry(frame_2, bd=8, relief=RAISED, textvariable=self.wooden_cars)
        wooden_cars_en.grid(row=2, column=1, ipady=5, ipadx=5)
        # This function for dall's house (product)
        dall_house_lbl = Label(frame_2, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color, text="Dall's House")
        dall_house_lbl.grid(row=3, column=0, padx=10, pady=20)
        dall_house_en = Entry(frame_2, bd=8, relief=RAISED, textvariable=self.dall_house)
        dall_house_en.grid(row=3, column=1, ipady=5, ipadx=5)

        # This function for willow farm tractor(product)
        willow_farm_tractor_lbl = Label(frame_2, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color,
                                        text="Willow Farm Tractor")
        willow_farm_tractor_lbl.grid(row=4, column=0, padx=10, pady=20)
        willow_farm_tractor_en = Entry(frame_2, bd=8, relief=RAISED, textvariable=self.willow_farm_tractor)
        willow_farm_tractor_en.grid(row=4, column=1, ipady=5, ipadx=5)

        # ===========This function for Price Frame=====================
        frame_2 = LabelFrame(self.root, text='Price', bd=10, relief=RAISED, bg=bg_color, fg="gold",
                             font=("Calibre", 13, "bold"))
        frame_2.place(x=330, y=180, width=325, height=380)

        # This function for wooden number bus price(label)
        wooden_price_lbl = Label(frame_2, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color, text="£13")
        wooden_price_lbl.grid(row=0, column=0, padx=10, pady=20)

        # This function for Noah's Ark (Label)
        noah_ark_price_lbl = Label(frame_2, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color, text="£15")
        noah_ark_price_lbl.grid(row=1, column=0, padx=10, pady=20)

        # This function for wooden card (Label)
        wooden_card_price_lbl = Label(frame_2, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color, text="£20")
        wooden_card_price_lbl.grid(row=2, column=0, padx=10, pady=20)

        # This function for dall's house (Label)
        dall_house_price_lbl = Label(frame_2, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color, text="£85")
        dall_house_price_lbl.grid(row=3, column=0, padx=10, pady=20)
        # This function for willow farm tractor (Label)
        willow_farm_tractor_price_lbl = Label(frame_2, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color,
                                              text="£10")
        willow_farm_tractor_price_lbl.grid(row=4, column=0, padx=10, pady=20)

        # This function for Cream and Ointment
        frame_2 = LabelFrame(self.root, text='Option', bd=10, relief=RAISED, bg=bg_color, fg="gold",
                             font=("Calibre", 13, "bold"))
        frame_2.place(x=655, y=180, width=325, height=380)

        # ===============Button================
        # This function for wooden number bus button
        # Add button
        add_button_1 = Button(frame_2, text="Add", bg=bg_color, fg=fg_color, font=("lucid", 12, "bold"),
                              bd=7, relief=RAISED, command=self.download)
        add_button_1.grid(row=0, column=0, padx=10, pady=20)
        # Delete button
        delete_button_1 = Button(frame_2, text="delete", bg=bg_color, fg=fg_color, font=("lucid", 12, "bold"),
                                 bd=7, relief=RAISED, command=delete_product)
        delete_button_1.grid(row=0, column=1, padx=10, pady=20)

        # This function for Noah's ark button
        # Add button
        add_button_2 = Button(frame_2, text="Add", bg=bg_color, fg=fg_color, font=("lucid", 12, "bold"),
                              bd=7, relief=RAISED, command=add_product)
        add_button_2.grid(row=1, column=0, padx=10, pady=20)
        # Delete Button
        delete_button_2 = Button(frame_2, text="delete", bg=bg_color, fg=fg_color, font=("lucid", 12, "bold"),
                                 bd=7, relief=RAISED, command=delete_product)
        delete_button_2.grid(row=1, column=1, padx=10, pady=20)

        # This function for wooden cars button
        # Add button
        add_button_3 = Button(frame_2, text="Add", bg=bg_color, fg=fg_color, font=("lucid", 12, "bold"),
                              bd=7, relief=RAISED, command=add_product)
        add_button_3.grid(row=2, column=0, padx=10, pady=20)
        # Delete button
        delete_button_3 = Button(frame_2, text="delete", bg=bg_color, fg=fg_color, font=("lucid", 12, "bold"),
                                 bd=7, relief=RAISED, command=delete_product)
        delete_button_3.grid(row=2, column=1, padx=10, pady=20)

        # This function for dall's house button
        # Add button
        add_button_4 = Button(frame_2, text="Add", bg=bg_color, fg=fg_color, font=("lucid", 12, "bold"),
                              bd=7, relief=RAISED, command=add_product)
        add_button_4.grid(row=3, column=0, padx=10, pady=20)
        # # Delete button
        delete_button_4 = Button(frame_2, text="delete", bg=bg_color, fg=fg_color, font=("lucid", 12, "bold"),
                                 bd=7, relief=RAISED, command=delete_product)
        delete_button_4.grid(row=3, column=1, padx=10, pady=20)

        # This function for willow farm tractor button
        # Add button
        add_button_5 = Button(frame_2, text="Add", bg=bg_color, fg=fg_color, font=("lucid", 12, "bold"),
                              bd=7, relief=RAISED, command=add_product)
        add_button_5.grid(row=4, column=0, padx=10, pady=20)
        # Delete button
        delete_button_5 = Button(frame_2, text="delete", bg=bg_color, fg=fg_color, font=("lucid", 12, "bold"),
                                 bd=7, relief=RAISED, command=delete_product)
        delete_button_5.grid(row=4, column=1, padx=10, pady=20)

        # ============Receipt Area==========
        # This function for Receipt Area frames
        frame_3 = Label(self.root, bd=10, bg=bg_color_1, relief=RAISED)
        frame_3.place(x=1010, y=180, width=350, height=350)
        # ===========
        receipt_title = Label(frame_3, text="Receipt Area", font=("Lucid", 13, "bold"), bd=7, relief=RAISED)
        receipt_title.pack(fill=X)
        # This function for Scroll bar Button frames

        scroll_y = Scrollbar(frame_3, orient=VERTICAL)
        self.txt = Text(frame_3, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txt.yview)
        self.txt.pack(fill=BOTH, expand=1)

        # This function for Buttons Frame
        frame_4 = LabelFrame(self.root, text='Total Menu', bd=10, relief=RAISED, bg=bg_color, fg="gold",
                             font=("Calibre", 13, "bold"))
        frame_4.place(x=0, y=560, relwidth=1, height=145)

        # This function for Total price (label)
        total_price_lbl = Label(frame_4, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color, text="Total Price")
        total_price_lbl.grid(row=0, column=0, padx=10, pady=0)
        total_price_en = Entry(frame_4, bd=8, relief=RAISED, textvariable=self.total_price)
        total_price_en.grid(row=0, column=1, ipady=2, ipadx=5)

        # This function for product tax
        product_tax_lbl = Label(frame_4, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color,
                                text="Delivery Charge")
        product_tax_lbl.grid(row=0, column=2, padx=30, pady=0)
        product_tax_en = Entry(frame_4, bd=8, relief=RAISED, textvariable=self.delivery_charge)
        product_tax_en.grid(row=0, column=3, ipady=2, ipadx=5)

        # This function for Total Button
        total_btn = Button(frame_4, text="Total", bg=bg_color, fg=fg_color, font=("lucid", 12, "bold"), bd=7,
                           relief=RAISED,
                           command=self.total_section)
        total_btn.grid(row=0, column=4, ipadx=20, padx=30)

        # This function for Generate Bill
        generate_bill_button = Button(frame_4, text="Generate Bill", bg=bg_color, fg=fg_color,
                                      font=("lucid", 12, "bold"),
                                      bd=7, relief=RAISED, command=self.billing_section)
        generate_bill_button.grid(row=0, column=5, ipadx=20)
        # This function for Clear Button
        clear_button = Button(frame_4, text="Clear", bg=bg_color, fg=fg_color, font=("lucid", 12, "bold"), bd=7,
                              relief=RAISED, command=self.clear)
        clear_button.grid(row=0, column=6, ipadx=20, padx=30)

        # This function for Exit Button
        exit_button = Button(frame_4, text="Exit", bg=bg_color, fg=fg_color, font=("lucid", 12, "bold"), bd=7,
                             relief=RAISED, command=self.exit)
        exit_button.grid(row=0, column=7, ipadx=20)
        # This function for download Button
        download_button = Button(frame_4, text="Download Receipt", bg=bg_color, fg=fg_color, font=("lucid", 12, "bold"),
                                 bd=7,
                                 relief=RAISED, command=self.download)
        download_button.grid(row=2, column=5, ipadx=10)
        # This function for print Button
        print_button = Button(frame_4, text="print", bg=bg_color, fg=fg_color, font=("lucid", 12, "bold"),
                              bd=7,
                              relief=RAISED, command=self.print)
        print_button.grid(row=2, column=6, ipadx=10)
        # This function for to get total prices

    def total_section(self):
        """This function will add
        all the product price"""
        self.total_product_prices = (
                (self.wooden_number_bus.get() * 13) +
                (self.nosh_ark.get() * 12) +
                (self.wooden_cars.get() * 20) +
                (self.dall_house.get() * 85) +
                (self.willow_farm_tractor.get() * 10)
        )

        self.total_price.set("£ " + str(self.total_product_prices))
        self.delivery_charge.set("£ " + str(round(self.total_product_prices * 0.05)))

    def welcome_customer(self):
        """This function will
        insert the value in receipt area"""
        self.txt.delete('1.0', END)

        self.txt.insert(END, "       Welcome To ALLAroundToys \n")
        self.txt.insert(END, f"\nCustomer reference No. : {str(self.customer_reference_number.get())}")
        self.txt.insert(END, "\nProduct: Quantity: Price:")
        self.txt.insert(END, "\n___________________________________")

    # Function to clear the receipt area

    def clear(self):
        """ this function will clear the
        text from Receipt Area"""
        self.txt.delete('1.0', END)

    def billing_section(self):
        """ this function will add the
        product price in the total price entry"""
        self.welcome_customer()
        if self.wooden_number_bus.get() != 0:
            self.txt.insert(END, f"\nWooden Number Bus {self.wooden_number_bus.get()} "
                                 f"{self.wooden_number_bus.get() * 13}")
        if self.nosh_ark.get() != 0:
            self.txt.insert(END, f"\nNoah's Ark{self.nosh_ark.get()} {self.nosh_ark.get() * 15}")
        if self.wooden_cars.get() != 0:
            self.txt.insert(END, f"\nWooden Cars{self.wooden_cars.get()} {self.wooden_cars.get() * 15}")
        if self.dall_house.get() != 0:
            self.txt.insert(END, f"\nDall's House {self.dall_house.get()} {self.dall_house.get() * 38}")
        if self.willow_farm_tractor.get() != 0:
            self.txt.insert(END,
                            f"\nWillow Farm Tractor {self.willow_farm_tractor.get()} "
                            f"{self.willow_farm_tractor.get() * 5}")

        self.txt.insert(END,
                        f"\n Total :"
                        f"{self.total_product_prices + self.total_product_prices * 0.05}")

    def print(self):
        """This function will print
        the receipt from the GUI"""
        q = self.txt.get("1.0", "end-1c", )
        print(q)
        filename = tempfile.mktemp(".txt")
        open(filename, 'w').write(q)
        if sys.platform == "win32":
            os.startfile(filename, "print")
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

    # Function which will allow to save the receipt in .txt file
    def download(self):
        """this function will allow the customer
        to download the receipt in txt file"""

        file = open("receipt.txt", "w")
        file.write("Your receipt: \n")
        file.close()
        # appending the .txt file
        file = open("receipt.txt", "a")

        self.welcome_customer()
        if self.wooden_number_bus.get() != 0:
            file.write("Wooden Number Bus {bus1} {bus2} \n".format
                       (bus1=self.wooden_number_bus.get(), bus2=self.wooden_number_bus.get() * 13))

            self.nosh_ark.get() * 15
        if self.nosh_ark.get() != 0:
            file.write("Noah's Ark {noah_ark1} {noah_ark2} \n".format
                       (noah_ark1=self.nosh_ark.get(), noah_ark2=self.nosh_ark.get() * 15))
        if self.wooden_cars.get() != 0:
            file.write("Wooden Cars {data1} {data2} \n".format
                       (data1=self.wooden_cars.get(), data2=self.wooden_cars.get() * 15))
        if self.dall_house.get() != 0:
            file.write("Dall's House {data1} {data2} \n".format
                       (data1=self.dall_house.get(), data2=self.dall_house.get() * 38))
        if self.willow_farm_tractor.get() != 0:
            self.txt.insert(END,
                            f"\nWillow Farm Tractor {self.willow_farm_tractor.get()} "
                            f"{self.willow_farm_tractor.get() * 5}")
            file.write("Willow Farm Tractor {data1} {data2} \n".format
                       (data1=self.willow_farm_tractor.get(), data2=self.willow_farm_tractor.get() * 5))

        self.txt.insert(END, f"\nInvoice No. : {str(self.customer_reference_number.get())}")
        file.write("Total : {data1}  \n".format(data1=self.total_product_prices + self.total_product_prices * 0.05))
        file.close()

    def updaate(self):
        """ This function will update the
        product stock in database """

        global my_tree
        toy_delete = "Wooden_Number_Bus"

        conn = sqlite3.connect('Sql_Toys_Catalogue.db')
        c = conn.cursor()

        c.execute(str("DELETE FROM ID WHERE Toys_Catalogue = ?", toy_delete))
        c.fetchall()

        for record in my_tree.get_children():
            my_tree.delete(record)

    def exit(self):
        """This function will allow close the window"""
        self.root.destroy()


# the loop will continue
if __name__ == "__main__":
    Object = Shopping_basket(root)
    root.mainloop()
