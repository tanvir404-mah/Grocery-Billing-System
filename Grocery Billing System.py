from tkinter import *
import random


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.title("Grocery Billing System")
        self.root.geometry("1280x720")
        self.root.config(bg="#2C3E50")

        # Variables
        self.cus_name = StringVar()
        self.cus_phone = StringVar()
        self.bill_no = StringVar()
        self.bill_no.set(str(random.randint(1000, 9999)))

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

        # Customer Name
        Label(F1, text="Customer Name", font=("Times New Roman", 15, "bold"), bg="#1ABC9C", fg="white").grid(row=0,
                                                                                                             column=0,
                                                                                                             padx=20,
                                                                                                             pady=5)
        Entry(F1, bd=5, relief=GROOVE, textvariable=self.cus_name).grid(row=0, column=1, padx=10, pady=5, ipadx=30)

        # Phone Number
        Label(F1, text="Phone No", font=("Times New Roman", 15, "bold"), bg="#1ABC9C", fg="white").grid(row=0, column=2,
                                                                                                        padx=20)
        Entry(F1, bd=5, relief=GROOVE, textvariable=self.cus_phone).grid(row=0, column=3, padx=10, pady=5, ipadx=30)

        # Bill No
        Label(F1, text="Bill No", font=("Times New Roman", 15, "bold"), bg="#1ABC9C", fg="white").grid(row=0, column=4,
                                                                                                       padx=20)
        Entry(F1, bd=5, relief=GROOVE, textvariable=self.bill_no, state="readonly").grid(row=0, column=5, padx=10,
                                                                                         pady=5, ipadx=30)

        # Product Frame
        F2 = LabelFrame(self.root, text="Products", font=("Times New Roman", 12, "bold"), bg="#F39C12", fg="white",
                        bd=10, relief=GROOVE)
        F2.place(x=5, y=180, width=400, height=400)

        # Product Labels and Entries
        for i, (text, (var, price)) in enumerate(self.items.items()):
            Label(F2, text=f"{text} - {price} tk", font=("Times New Roman", 15, "bold"), bg="#F39C12", fg="white").grid(
                row=i, column=0, padx=10, pady=10)
            Entry(F2, bd=5, relief=GROOVE, textvariable=var).grid(row=i, column=1, ipadx=5, ipady=5)

        # Add to Bill Button
        Button(F2, text="Add to Bill", font=("Times New Roman", 12, "bold"), bg="#2ECC71", fg="white", bd=7,
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

        Button(F4, text="Total", font=("Times New Roman", 12, "bold"), bg="#27AE60", fg="white", bd=7, relief=GROOVE,
               command=self.total).pack(pady=10, ipadx=20)
        Button(F4, text="Generate Bill", font=("Times New Roman", 12, "bold"), bg="#2980B9", fg="white", bd=7,
               relief=GROOVE, command=self.bill_area).pack(pady=10, ipadx=20)
        Button(F4, text="Clear", font=("Times New Roman", 12, "bold"), bg="#D35400", fg="white", bd=7, relief=GROOVE,
               command=self.clear).pack(pady=10, ipadx=20)
        Button(F4, text="Exit", font=("Times New Roman", 12, "bold"), bg="#C0392B", fg="white", bd=7, relief=GROOVE,
               command=self.exit).pack(pady=10, ipadx=20)

    def add_to_bill(self):
        self.txt.insert(END, "\n--- Items Added ---\n")
        for name, (var, price) in self.items.items():
            if var.get() > 0:
                self.txt.insert(END, f"{name}: {var.get()} x {price} tk = {var.get() * price} tk\n")

    def total(self):
        total_cost = sum(var.get() * price for var, price in self.items.values())
        self.txt.insert(END, f"\nTotal Cost: {total_cost} tk\n")

    def bill_area(self):
        self.txt.insert(END,
                        f"\nBill No: {self.bill_no.get()}\nCustomer: {self.cus_name.get()}\nPhone: {self.cus_phone.get()}\n")

    def clear(self):
        self.txt.delete('1.0', END)

    def exit(self):
        self.root.destroy()


root = Tk()
app = Bill_App(root)
root.mainloop()
