import datetime
import requests
import numpy as np

import cv2
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from PyQt5.uic.properties import QtCore
from PyQt5 import QtCore
from ModelDataRetrieve import *
from commandLine import *
from Tables import *

class DataOutput(QDialog):
    def __init__(self):
        super(DataOutput, self).__init__()
        loadUi('untitled.ui', self)
        self.loadbutton.clicked.connect(self.loadimage)
        self.submitbutton.clicked.connect(self.loadData)
        self.nextButton.clicked.connect(self.nextVehicle)

    @pyqtSlot()
    def nextVehicle(self):
        self.vehicleNumbInput.setText(None)
        self.checkVehicleNumb.setText(None)
        self.progressBar1.setValue(0)
        self.progressBar2.setValue(0)
        self.progressBar3.setValue(0)
        self.Fname.setText(None)
        self.Lname.setText(None)
        self.line1.setText(None)
        self.line2.setText(None)
        self.line3.setText(None)
        self.nic.setText(None)
        self.expDate.setText(None)
        self.blood.setText(None)

    def loadData(self):
        EnteredVehicleNumber = self.getVehicleNumberInput();
        if checkValidNumber(EnteredVehicleNumber):
            self.checkVehicleNumb.setText("Valid Number")

            if (checkLicence(EnteredVehicleNumber)):
                self.progressBar1.setValue(100);
            else:
                self.progressBar1.setValue(5);

            if (checkInsuranceValidity(EnteredVehicleNumber)):
                self.progressBar2.setValue(100);
            else:
                self.progressBar2.setValue(5);
            if (checkEmmisionTest(EnteredVehicleNumber)):
                self.progressBar3.setValue(100);
            else:
                self.progressBar3.setValue(5);

            self.Fname.setText(getFname(EnteredVehicleNumber))
            self.Lname.setText(getLname(EnteredVehicleNumber))
            self.line1.setText(getAddr1(EnteredVehicleNumber))
            self.line2.setText(getAddr2(EnteredVehicleNumber))
            self.line3.setText(getAddr3(EnteredVehicleNumber))
            self.nic.setText(getNIC(EnteredVehicleNumber))
            self.expDate.setText(getOwnerLicenceExpireDate(EnteredVehicleNumber))
            self.blood.setText(getBloodGroup(EnteredVehicleNumber))

            toDay = str(datetime.datetime.now().strftime("%Y-%m-%d"))
            currentTime = datetime.datetime.now().time()
            from_ = str(self.location.currentText())
            populateRecords(EnteredVehicleNumber, toDay, currentTime, from_)



        else:
            self.checkVehicleNumb.setText("In-Valid Number")

    def getVehicleNumberInput(self):
        #return str(self.getNumber.text())
        return str(self.vehicleNumbInput.text())

    def newCamer(self):
        while (True):
            #url = "http://192.168.8.100:8080/shot.jpg"

            img_resp = requests.get(url)
            img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
            img = cv2.imdecode(img_arr, -1)
            cv2.imwrite(filename='img2.png', img=img)
            # cv2.imshow("cam", img)

            break


    def capturePhoto(self):
        cam = cv2.VideoCapture(0)
        frame = cam.read()[1]
        cv2.imwrite(filename='img2.png', img=frame)

    def loadimage(self):
        #self.capturePhoto()
        self.newCamer()
        self.loadImage('img2.png')

    def loadImage(self, fname):
        self.image = cv2.imread(fname)
        self.displayImage()

    def displayImage(self):
        qformat = QImage.Format_Indexed8
        if len(self.image.shape) == 3:
            if (self.image.shape[2]) == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        img = QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.strides[0], qformat)

        img = img.rgbSwapped()

        self.imagelabel.setPixmap(QPixmap.fromImage(img))
        self.imagelabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        #self.commandlineHandle()
        print("now commandline stage")
        self.getNumber.setText(commandlineHandle())


app = QApplication(sys.argv)
test = DataOutput()
test.setWindowTitle("Highway Entrance")
test.setGeometry(30000, 10000, 10000, 10000)
test.show()
sys.exit(app.exec())
