'''
Author: Sage Johnson, with help from GeeksForGeeks
Date: 06/21/2024
Goal: First program using Tkinter, a Python toolkit for GUI applications.
'''
from tkinter import *
class LoanCalculator:


    def __init__(self):
        window = Tk()
        window.title('Loan Calculator by Sage, with help from GeeksForGeeks')

        annual_interest_rate = Label(window, text = 'Annual Interest Rate').grid(row = 1, column = 1, sticky = W)
        number_of_years = Label(window, text = 'Number of Years').grid(row = 2, column = 1, sticky = W)
        loan_amount = Label(window, text = 'Loan Amount').grid(row = 3, column = 1, sticky = W)
        monthly_payment = Label(window, text = 'Monthly Payment').grid(row = 4, column = 1, sticky = W)
        total_payment = Label(window, text = 'Total Payment').grid(row = 5, column = 1, sticky = W)

        self.annual_interest_rate_variable = StringVar()
        Entry(window, textvariable = self.annual_interest_rate_variable, justify = RIGHT).grid(row = 1, column = 2)

        self.number_of_years_variable = StringVar()
        Entry(window, textvariable = self.number_of_years_variable, justify = RIGHT).grid(row = 2, column = 2)

        self.loan_amount_variable = StringVar()
        Entry(window, textvariable = self.loan_amount_variable, justify = RIGHT).grid(row = 3, column = 2)

        self.monthly_payment_variable = StringVar()
        label_monthly_payment = Label(window, textvariable = self.monthly_payment_variable).grid(row = 4, column = 2, sticky = E)

        self.total_payment_variable = StringVar()
        label_total_payment = Label(window, textvariable = self.total_payment_variable).grid(row = 5, column = 2, sticky = E)

        button_compute_payment = Button(window, text = 'Calculate', command = self.get_payment).grid(row = 6, column = 2, sticky = E)

        window.mainloop()


    def get_payment(self):
        # need interest rate to be decimal (so divide percentage by 100), then converted to a monthly rate (so divide by 12)
        interest_rate = float(self.annual_interest_rate_variable.get()) / 1200
        number_of_months = int(self.number_of_years_variable.get()) * 12
        loan_amount = float(self.loan_amount_variable.get())

        # below equation sourced from CalculatorSoup.com
        numerator = (loan_amount * interest_rate * ((1 + interest_rate) ** number_of_months))
        denominator = (((1 + interest_rate) ** number_of_months)) - 1
        # below is result of equation -- to find monthly payment for life of loan
        monthly_payment = float(numerator / denominator)
        # (monthly payment * life of loan) == total paid back, including interest
        total_payment = float(monthly_payment * number_of_months)

        self.monthly_payment_variable.set(format(monthly_payment, '10.2f'))
        self.total_payment_variable.set(format(total_payment, '10.2f'))
LoanCalculator()
