from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import sys, os
import pyndb as pyn

from ui.output import Ui_OutputWindow

class OutWindow(QMainWindow, Ui_OutputWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('ui/output.ui', self)
        self.db = pyn.PYNDatabase('data.pyn')
        self.connect()
        self.show_output()

    def connect(self):
        self.ClosepushButton.clicked.connect(self.close_app)

    def show_output(self):
        # import database
        info = self.db

        # setting up the pricing information

        # Finding out price plan
        charge = None
        plan = ""
        if info.CarPlan.val == "Gold Plan ($36/month)":
            charge = 36
            plan = "Gold"
        elif info.CarPlan.val == "Silver Plan ($30/month)":
            charge = 30
            plan = "Silver"
        else:
            charge = 20
            plan = "Bronze"


        # Finding out car nums

        if info.NumCars.val == 3:
            charge *= 1.75
        elif info.NumCars.val == 2:
            charge *= 1.5

        bill_type = ""
        if info.Bill.val == "Monthly Subscription":
            bill_type = "Monthly"
        else:
            bill_type = "Yearly"
        # setting month / annual subscriptions
        subtotal = charge if info.Bill.val == "Monthly Subscription" else charge * 11
        tax = subtotal * .07
        total = tax + subtotal


        # Updating Text vals
        self.FirstName.setText(f"First Name: {info.FirstName.val}")
        self.LastName.setText(f"Last Name: {info.LastName.val}")
        self.Adress.setText(f"Address: {info.Address.val}")
        self.label_5.setText(f"City: {info.City.val}")
        self.State.setText(f"State: {info.State.val}")
        self.Ziptxt.setText(f"Zip: {info.Zip.val}")
        self.Phone.setText(f"Phone: {info.Phone.val}")
        self.Email.setText(f"Email: {info.Email.val}")
        self.CarPlan.setText(f"Car Wash Plan: {plan}")
        self.NumOfCars.setText(f"Nuber of Cars: {info.NumCars.val}")
        self.PayPlan.setText(f"Subscription: {bill_type}")
        self.SubTotal.setText(f"Subtotal: ${round(subtotal, 2)}")
        self.Tax.setText(f"Tax: ${round(tax, 2)}")
        self.TotalDue.setText(f"Total: ${round(total, 2)}")
        self.Monthly.setText(f"Monthly: ${round(charge, 2)}")


    def close_app(self):
        # closes application
        exit("0")




if __name__ == '__main__':
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QApplication(sys.argv)
    window = OutWindow()
    window.show()
    sys.exit(app.exec_())

