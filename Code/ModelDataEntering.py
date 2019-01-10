# from Model import *

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="CO226DataBase"
)
mycursor = mydb.cursor()


# print(mydb)

# mycursor.execute("CREATE DATABASE CO226DataBase")
# mycursor.execute("show databases")
# mycursor.execute("USE CO226DataBase")


def populateVehicle(LicenseNo, OwnerNIC, VehicleType, LicenseValidity, InsuaranceValidity, EmissionTest):
    query = "INSERT INTO Vehicle(LicenseNo,OwnerNIC,VehicleType,LicenseValidity,InsuaranceValidity,EmissionTest) VALUES (%s,%s,%s,%s,%s,%s)"
    data = (LicenseNo, OwnerNIC, VehicleType, LicenseValidity, InsuaranceValidity, EmissionTest)
    mycursor.execute(query, data)
    mydb.commit()


def populateOwner(FirstName, Lastname, NIC, Addr1, Addr2, Addr3, BloodGroup,LicenceExpireDate):
    query = "INSERT INTO Owner(FirstName,Lastname,NIC,AddressLine1,AddressLine2,AddressLine3,BloodGroup,LicenceExpireDate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    data = (FirstName, Lastname, NIC, Addr1, Addr2, Addr3, BloodGroup,LicenceExpireDate)
    mycursor.execute(query, data)
    mydb.commit()

def populateBank(AccNo,BankName,NIC):
    query="INSERT INTO Bank(AccNo,BankName,OwnerNIC) VALUES (%s,%s,%s)"
    data=(AccNo,BankName,NIC)
    mycursor.execute(query,data)
    mydb.commit()

def populateRecords(VehicleNumber,RecordDate,ArrivalTime,From_):
    query = "INSERT INTO Records(VehicleNumber,RecordDate,ArrivalTime,From_) VALUES (%s,%s,%s,%s)"
    data=(VehicleNumber,RecordDate,ArrivalTime,From_)
    mycursor.execute(query, data)
    mydb.commit()


