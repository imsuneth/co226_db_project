

from ModelDataEntering import *

#mycursor.execute("drop table Owner")
#mycursor.execute("drop table Vehicle")
#mycursor.execute("drop table Bank")
#mycursor.execute("drop table Records")

createTableOwner = "CREATE TABLE Owner(FirstName VARCHAR(20),LastName VARCHAR(20),NIC INTEGER,AddressLine1 VARCHAR(20),AddressLine2 VARCHAR(20),AddressLine3 VARCHAR(20),BloodGroup VARCHAR(5),LicenceExpireDate DATE,PRIMARY KEY (NIC))"
createTableVehicle = "CREATE TABLE Vehicle (LicenseNo VARCHAR(50),OwnerNIC INTEGER,VehicleType VARCHAR(50),LicenseValidity Boolean,InsuaranceValidity Boolean,EmissionTest Boolean,PRIMARY KEY (LicenseNo),FOREIGN KEY (OwnerNIC) REFERENCES Owner(NIC))"
createTableBankDetails = "CREATE TABLE Bank (AccNo INTEGER,BankName Varchar(50),OwnerNIC INTEGER,PRIMARY KEY (OwnerNIC),FOREIGN KEY (OwnerNIC) REFERENCES Owner(NIC))"
createTableRecords="CREATE TABLE Records (EntryNo INTEGER AUTO_INCREMENT,VehicleNumber VARCHAR(50), RecordDate DATE, ArrivalTime TIME,From_ VARCHAR(20), TO_ VARCHAR(20) DEFAULT NULL, ExitTime TIME DEFAULT NULL,Fee INTEGER DEFAULT NULL, PRIMARY KEY(EntryNo),FOREIGN KEY (VehicleNumber) REFERENCES Vehicle(LicenseNo))"

#mycursor.execute(createTableOwner) #This is the Parent table and no forign key
#mycursor.execute(createTableVehicle)
#mycursor.execute(createTableBankDetails)
#mycursor.execute(createTableRecords)
#print(datetime.datetime.now().time())
