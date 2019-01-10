import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import datetime
from dateutil.parser import parse
from ModelDataEntering import *


class TestProg(QDialog):
    def __init__(self):
        super(TestProg, self).__init__()
        loadUi('DataEntering.ui', self)
        self.pushButton_submit.clicked.connect(self.submitClicked)
        self.pushButton_clear.clicked.connect(self.clear)

    @pyqtSlot()
    def clear(self):
        self.lineEdit_vehicleNumber.setText(None)
        self.lineEdit_firstname.setText(None)
        self.lineEdit_lastname.setText(None)
        self.lineEdit_licneceRegNum.setText(None)
        self.lineEdit_addr1.setText(None)
        self.lineEdit_addr2.setText(None)
        self.lineEdit_addr3.setText(None)
        self.lineEdit_blood.setText(None)
        self.lineEdit_AccNo.setText(None)
    def submitClicked(self):
        vehicleNumber = self.lineEdit_vehicleNumber.text()
        populateOwner(self.firstname(), self.lastname(), self.NIC(), self.addr1(), self.addr2(), self.addr3(),self.bloodGroup(),self.OwnerLicenceExpireDate())
        populateVehicle(str(vehicleNumber), str(self.NIC()), str(self.vehicleType()), str(self.licenceExpireCompare()),
                        str(self.insuranceExpireCompare()), str(self.emmisionExpireCompare()))

        populateBank(self.ACCNO(),self.selectedBank(),self.NIC())


    def checkValidVehicle(self):  # still not incluede

        while (True):
            getText = str(self.lineEdit_vehicleNumber.text())
            query = "SELECT RegNo FROM Vehicle WHERE RegNo={}".format(getText)
            if query == None:
                break
            else:
                self.label_validvehiclenumber.setText("Invalid")

    def vehicleType(self):
        if self.checkbox_car.isChecked():
            return "Car"
        elif self.checkbox_van.isChecked():
            return "Van"
        elif self.checkbox_jeep.isChecked():
            return "Jeep"
        elif self.checkbox_bus.isChecked():
            return "Bus"
        elif self.checkbox_lorry.isChecked():
            return "Lorry"

    def licenceExpireCompare(self):
        expireDate = str(self.dateEdit_licenceExpire.date().toPyDate())
        toDay = str(datetime.datetime.now().strftime("%Y-%m-%d"))
        if parse(toDay) > parse(expireDate):
            return 0
        else:
            return 1
    def OwnerLicenceExpireDate(self):
            return str(self.dateEdit_ownerLicneceExpire.date().toPyDate())
    def insuranceExpireCompare(self):
        expireDate = str(self.dateEdit_insuranceExpire.date().toPyDate())
        toDay = str(datetime.datetime.now().strftime("%Y-%m-%d"))
        if parse(toDay) > parse(expireDate):
            return 0
        else:
            return 1

    def emmisionExpireCompare(self):
        expireDate = str(self.dateEdit_emmisionExpire.date().toPyDate())
        toDay = str(datetime.datetime.now().strftime("%Y-%m-%d"))
        if parse(toDay) > parse(expireDate):
            return 0
        else:
            return 1

    def firstname(self):
        return str(self.lineEdit_firstname.text())

    def lastname(self):
        return str(self.lineEdit_lastname.text())

    def addr1(self):
        return str(self.lineEdit_addr1.text())

    def addr2(self):
        return str(self.lineEdit_addr2.text())

    def addr3(self):
        return str(self.lineEdit_addr3.text())

    def bloodGroup(self):
        return str(self.lineEdit_blood.text())

    def NIC(self):
        return str(self.lineEdit_licneceRegNum.text())

    def ACCNO(self):
        return str(self.lineEdit_AccNo.text())

    def selectedBank(self):
        return str(self.bankList.currentText())



app = QApplication(sys.argv)
test = TestProg()
test.setWindowTitle("Real Time Vehicle identification system")
test.setGeometry(30000, 10000, 10000, 10000)
test.show()
sys.exit(app.exec())
