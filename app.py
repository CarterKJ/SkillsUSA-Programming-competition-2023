from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import sys, os
import pyndb
from ui.main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('ui/main.ui', self)
        self.connect()
        self.user_info = {}
        self.db = pyndb.PYNDatabase("data.pyn")

    def connect(self):
        # paring buttons to their functions
        self.CalcpushButton.clicked.connect(self.connect_output)
        self.ExitpushButton.clicked.connect(self.close_app)
        self.ClearButton.clicked.connect(self.clear)
        return

    def connect_output(self):
        # sets up the data
        self.setup_data()
        # checks data
        # W solution
        if self.validate_info() == 0:
            os.system("python output.py")

    def setup_data(self):
        info = self.db
        # Setting values to map for passing
        info.set("FirstName", self.FirstNamelineEdit.text())
        info.set("LastName", self.LastNamelineEdit.text())
        info.set("Address", self.AdresslineEdit.text())
        info.set("City", self.CitylineEdit.text())
        info.set("State", self.StatelineEdit.text())
        info.set("Zip", self.ZiplineEdit.text())
        info.set("Phone", self.PhonelineEdit.text())
        info.set("Email", self.EmaillineEdit.text())
        info.set("CarPlan", self.CarPlancomboBox.currentText())
        info.set("NumCars", self.NumCarspinBox.value())
        info.set("Bill", self.PaymentcomboBox.currentText())
        info.save()
        return

    def validate_info(self):
        # Makes sure all the current information is correct
        txt = ""
        Stat_code = 0
        # Zip Test
        try:
            int(self.ZiplineEdit.text())
        except:
            txt = "Zip is incorrect"
            Stat_code = 1

        # Phone test
        try:
            int(self.PhonelineEdit.text())
        except:
            txt = "Phone is incorrect"
            Stat_code = 1

        self.push_error(txt)
        return Stat_code

    def clear(self):
        # Clears inputs
        self.FirstNamelineEdit.setText("")
        self.LastNamelineEdit.setText("")
        self.AdresslineEdit.setText("")
        self.CitylineEdit.setText("")
        self.StatelineEdit.setText("")
        self.ZiplineEdit.setText("")
        self.PhonelineEdit.setText("")
        self.EmaillineEdit.setText("")

    def push_error(self, error):
        # puts error code for user to see what is incorrect
        self.errorTxt.setText(error)

    def close_app(self):
        # closes application
        exit("0")


if __name__ == '__main__':
    # Starts environment and app
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec_())
