# Grocery Billing System with Stock Management
from tkinter import *
import random
from tkinter import messagebox
import os

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.title("Grocery Billing System")
        self.root.geometry("1280x720")
        self.root.config(bg="#2284E6")

        # Variables
        self.cus_name = StringVar()
        self.cus_phone = StringVar()
        self.bill_no = StringVar()
        self.last_bill_no = 1000  # প্রথম বিল
        self.bill_no.set(str(self.last_bill_no))


        # Items and Prices
        self.items = {
            "Milk (L)": (IntVar(), 80),
            "Eggs (pcs)": (IntVar(), 50),
            "Bread (pcs)": (IntVar(), 50),
            "Rice (kg)": (IntVar(), 70),
            "Potato (kg)": (IntVar(), 30),
            "Sugar (kg)": (IntVar(), 110),
            "Water (L)": (IntVar(), 50),
            "Coffee (kg)": (IntVar(), 150),
            "Juice (L)": (IntVar(), 200),
            "Chicken (kg)": (IntVar(), 250)
        }

        # Title
        title = Label(self.root, text="Grocery Billing System", bd=10, relief=GROOVE,
                      font=("Times New Roman", 25, "bold"), bg="#16A085", fg="white", pady=10)
        title.pack(fill=X)

        # Customer Details Frame
        F1 = LabelFrame(self.root, text="Customer Details", font=("Times New Roman", 12, "bold"),
                        bg="#1ABC9C", fg="white", bd=10, relief=GROOVE)
        F1.place(x=0, y=80, relwidth=1)

        Label(F1, text="Customer Name", font=("Times New Roman", 15, "bold"), bg="#1ABC9C", fg="white").grid(row=0,
                                                                                                             column=0,
                                                                                                             padx=20,
                                                                                                             pady=5)
        Entry(F1, bd=5, relief=GROOVE, textvariable=self.cus_name).grid(row=0, column=1, padx=10, pady=5, ipadx=30)

        Label(F1, text="Phone No", font=("Times New Roman", 15, "bold"), bg="#1ABC9C", fg="white").grid(row=0, column=2,
                                                                                                        padx=20)
        Entry(F1, bd=5, relief=GROOVE, textvariable=self.cus_phone).grid(row=0, column=3, padx=10, pady=5, ipadx=30)

        Label(F1, text="Bill No", font=("Times New Roman", 15, "bold"), bg="#1ABC9C", fg="white").grid(row=0, column=4,
                                                                                                       padx=20)
        Entry(F1, bd=5, relief=GROOVE, textvariable=self.bill_no, state="readonly").grid(row=0, column=5, padx=10,
                                                                                         pady=5, ipadx=30)

        # Product Frame
        self.F2 = LabelFrame(self.root, text="Products", font=("Times New Roman", 12, "bold"), bg="#F39C12", fg="white",
                        bd=10, relief=GROOVE)
        self.F2.place(x=5, y=180, width=400, height=400)

        # Products UI
        self.display_products()

        # Add to Bill Button
        Button(self.F2, text="Add to Bill", font=("Times New Roman", 12, "bold"), bg="#2ECC71", fg="white", bd=7,
               relief=GROOVE, command=self.add_to_bill).grid(row=len(self.items), columnspan=2, pady=10, ipadx=20)

        # Bill Area
        F3 = Frame(self.root, bd=10, relief=GROOVE)
        F3.place(x=420, y=180, width=400, height=400)

        Label(F3, text="Bill List", font=("Times New Roman", 15, "bold"), bd=7, relief=GROOVE).pack(fill=X)
        scroll_y = Scrollbar(F3, orient=VERTICAL)
        self.txt = Text(F3, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txt.yview)
        self.txt.pack(fill=BOTH, expand=1)

        # Buttons Frame
        F4 = Frame(self.root, bd=10, relief=GROOVE)
        F4.place(x=830, y=180, width=400, height=400)

        Button(F4, text="Add to Bill", font=("Times New Roman", 12, "bold"), bg="#2ECC71", fg="white", bd=7,
               relief=GROOVE, command=self.add_to_bill).pack(pady=10, ipadx=20)
        Button(F4, text="Total", font=("Times New Roman", 12, "bold"), bg="#27AE60", fg="white", bd=7, relief=GROOVE,
               command=self.total).pack(pady=10, ipadx=20)
        Button(F4, text="Generate Bill", font=("Times New Roman", 12, "bold"), bg="#2980B9", fg="white", bd=7,
               relief=GROOVE, command=self.bill_area).pack(pady=10, ipadx=20)
        Button(F4, text="Save Bill", font=("Times New Roman", 12, "bold"), bg="#8E44AD", fg="white", bd=7,
               relief=GROOVE, command=self.save_bill).pack(pady=10, ipadx=20)
        Button(F4, text="Clear", font=("Times New Roman", 12, "bold"), bg="#D35400", fg="white", bd=7, relief=GROOVE,
               command=self.clear).pack(pady=10, ipadx=20)
        Button(F4, text="Exit", font=("Times New Roman", 12, "bold"), bg="#C0392B", fg="white", bd=7, relief=GROOVE,
               command=self.exit).pack(pady=10, ipadx=20)

        # Stock Management Frame
        F5 = LabelFrame(self.root, text="Stock Management", font=("Times New Roman", 12, "bold"),
                        bg="#34495E", fg="white", bd=10, relief=GROOVE)
        F5.place(x=5, y=600, width=1225, height=100)

        self.new_item_name = StringVar()
        self.new_item_price = StringVar()
        self.new_item_qty = StringVar()

        Label(F5, text="Item Name", font=("Times New Roman", 12, "bold"), bg="#34495E", fg="white").grid(row=0, column=0, padx=10, pady=10)
        Entry(F5, textvariable=self.new_item_name, bd=5, relief=GROOVE).grid(row=0, column=1, padx=10, pady=10)

        Label(F5, text="Price", font=("Times New Roman", 12, "bold"), bg="#34495E", fg="white").grid(row=0, column=2, padx=10, pady=10)
        Entry(F5, textvariable=self.new_item_price, bd=5, relief=GROOVE).grid(row=0, column=3, padx=10, pady=10)

        Label(F5, text="Quantity", font=("Times New Roman", 12, "bold"), bg="#34495E", fg="white").grid(row=0, column=4, padx=10, pady=10)
        Entry(F5, textvariable=self.new_item_qty, bd=5, relief=GROOVE).grid(row=0, column=5, padx=10, pady=10)

        Button(F5, text="Add/Update Stock", font=("Times New Roman", 12, "bold"), bg="#E67E22", fg="white", bd=7, relief=GROOVE,
               command=self.add_update_stock).grid(row=0, column=6, padx=10, pady=10, ipadx=10)

    # ----------------- Functions -----------------

    def display_products(self):
        """Display products dynamically in Products frame"""
        for widget in self.F2.winfo_children():
            if isinstance(widget, Entry) or isinstance(widget, Label):
                widget.destroy()

        for i, (text, (var, price)) in enumerate(self.items.items()):
            Label(self.F2, text=f"{text} - {price} tk", font=("Times New Roman", 15, "bold"), bg="#F39C12", fg="white").grid(
                row=i, column=0, padx=10, pady=10)
            Entry(self.F2, bd=5, relief=GROOVE, textvariable=var).grid(row=i, column=1, ipadx=5, ipady=5)

    def add_to_bill(self):
        self.txt.insert(END, "\n--- Items Added ---\n")
        for name, (var, price) in self.items.items():
            if var.get() > 0:
                self.txt.insert(END, f"{name}: {var.get()} x {price} tk = {var.get() * price} tk\n")

    def total(self):
        self.total_cost = sum(var.get() * price for var, price in self.items.values())
        self.txt.insert(END, f"\nTotal Cost: {self.total_cost} tk\n")

    def bill_area(self):
        self.txt.delete('1.0', END)
        self.txt.insert(END, "========== Grocery Store ==========\n")
        self.txt.insert(END, f"Bill No: {self.bill_no.get()}\nCustomer: {self.cus_name.get()}\nPhone: {self.cus_phone.get()}\n")
        self.txt.insert(END, "----------------------------------\n")
        self.txt.insert(END, "Items\tQty\tPrice\tTotal\n")
        self.txt.insert(END, "----------------------------------\n")
        for name, (var, price) in self.items.items():
            if var.get() > 0:
                total_item = var.get() * price
                self.txt.insert(END, f"{name}\t{var.get()}\t{price}\t{total_item}\n")
        self.total()
        self.txt.insert(END, "==================================\n")
        self.txt.insert(END, "Thank you for shopping with us!\n")

    def save_bill(self):
        if not os.path.exists("bills"):
            os.mkdir("bills")
        bill_data = self.txt.get('1.0', END)
        if bill_data.strip() == "":
            messagebox.showwarning("Warning", "No bill to save!")
            return
        filename = f"bills/{self.bill_no.get()}.txt"
        with open(filename, "w") as f:
            f.write(bill_data)
        messagebox.showinfo("Saved", f"Bill saved successfully as {filename}")

    def clear(self):
        self.txt.delete('1.0', END)
        self.cus_name.set("")
        self.cus_phone.set("")
        self.last_bill_no += 1
        self.bill_no.set(str(self.last_bill_no))

        for var, price in self.items.values():
            var.set(0)

    def exit(self):
        self.root.destroy()

    # ----------------- Stock Management -----------------
    def add_update_stock(self):
        name = self.new_item_name.get().strip()
        try:
            price = int(self.new_item_price.get())
            qty = int(self.new_item_qty.get())
        except:
            messagebox.showerror("Error", "Price and Quantity must be numbers!")
            return

        if name == "":
            messagebox.showerror("Error", "Item name cannot be empty!")
            return

        if name in self.items:
            self.items[name][0].set(self.items[name][0].get() + qty)
            self.items[name] = (self.items[name][0], price)
            messagebox.showinfo("Updated", f"Stock updated for {name}")
        else:
            self.items[name] = (IntVar(value=qty), price)
            messagebox.showinfo("Added", f"New item {name} added to stock")

        # Clear input fields
        self.new_item_name.set("")
        self.new_item_price.set("")
        self.new_item_qty.set("")

        # Refresh Products Frame
        self.display_products()


# ----------------- Main -----------------
root = Tk()
app = Bill_App(root)
root.mainloop()
