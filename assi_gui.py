from tkinter import *
from tkinter.messagebox import showinfo, showerror


class Loan:
    def __init__(self, years, amount):
        self.years = years
        self.amount = amount

    def total(self):
        if self.years == 1:
            total = self.amount * 0.1376
        elif self.years == 3:
            total = self.amount * 0.1406
        elif self.years == 5:
            total = self.amount * 0.1487
        elif self.years == 7:
            total = self.amount * 0.1571
        else:
            raise ValueError("unknown")
        return int(total)

    def per_y(self):
        return self.total() / self.years

    def per_m(self):
        return self.total() / 12


def show_mass():
    amount = L_amount.get()
    if not amount.isdigit():
        showerror("ERROR","Please enter a valid number")
        return

    amount = float(amount)
    years = var.get()
    loan_obj = Loan(years, amount)
    total_amount = loan_obj.total()
    per_year_amount = loan_obj.per_y()
    per_month_amount = loan_obj.per_m()

    showinfo("INFO", f"The total amount of loan is {total_amount}\n"
                     f"The total amount per year is {per_year_amount}\n"
                     f"The total amount per month is {per_month_amount}")


win = Tk()
win.title("Loan Calculator")
win.iconphoto(True, PhotoImage(file="logo-misr-paris-black-retina.png"))
win.geometry("700x350")
win.configure(bg='#8B0000')


Label(win, text="welcome At Bank Misr".upper(), font=("Arial", 16), fg=("#f0f0f0"), bg=("#8b0000")).pack(pady=10)
Label(win, text="Enter loan amount".upper(), font=("Arial", 12), fg=("#ffd700"), bg=("#8b0000")).pack(pady=10)

L_amount = Entry(win, font=("Arial"), fg=("#ffd700"), bg=("#8b0010"))

L_amount.pack(pady=10)

var = IntVar()
R1 = Radiobutton(win, text="1 year", value=1, bg=("#8b0010"), pady=5, variable=var)
R1.pack()
R3 = Radiobutton(win, text="3 years", value=3, bg=("#8b0010"), pady=5, variable=var)
R3.pack()
R2 = Radiobutton(win, text="5 years", value=5, bg=("#8b0010"), pady=5, variable=var)
R2.pack()
R4 = Radiobutton(win, text="7 years", value=7, bg=("#8b0010"), pady=5, variable=var)
R4.pack()

b1 = Button(win, text="result", command=show_mass)
b1.pack()

win.mainloop()