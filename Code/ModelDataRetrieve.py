from ModelDataEntering import *


def checkValidNumber(vehicleNumber):
    query = "SELECT LicenseNo FROM Vehicle"
    mycursor.execute(query)
    result = mycursor.fetchall()
    for i in result:
        data = " ".join(i)
        if data == vehicleNumber:
            return True
    return False


def checkLicence(vehicleNumber):
    tupleData = (str(vehicleNumber),)  # %s should give as a tuple to execute
    query = "SELECT LicenseValidity FROM Vehicle WHERE LicenseNo = %s"
    mycursor.execute(query, tupleData)
    result = mycursor.fetchall()
    if result == [(0,)]:
        return False
    else:
        return True


# print(checkLicence("KH-0746"))
def checkInsuranceValidity(vehicleNumber):
    tupleData = (str(vehicleNumber),)  # %s should give as a tuple to execute
    query = "SELECT InsuaranceValidity FROM Vehicle WHERE LicenseNo = %s"
    mycursor.execute(query, tupleData)
    result = mycursor.fetchall()
    if result == [(0,)]:
        return False
    else:
        return True


def checkEmmisionTest(vehicleNumber):
    tupleData = (str(vehicleNumber),)  # %s should give as a tuple to execute
    query = "SELECT EmissionTest FROM Vehicle WHERE LicenseNo = %s"
    mycursor.execute(query, tupleData)
    result = mycursor.fetchall()
    if result == [(0,)]:
        return False
    else:
        return True


def getFname(vehicleNumber):
    tupleData = (str(vehicleNumber),)  # %s should give as a tuple to execute
    query = "SELECT Owner.FirstName FROM Owner,Vehicle WHERE Owner.NIC=Vehicle.OwnerNIC AND Vehicle.LicenseNo= %s"  # using the forign key NIC
    mycursor.execute(query, tupleData)
    result = mycursor.fetchall()
    for i in result:
        data = " ".join(i)
        return data


def getLname(vehicleNumber):
    tupleData = (str(vehicleNumber),)  # %s should give as a tuple to execute
    query = "SELECT Owner.LastName FROM Owner,Vehicle WHERE Owner.NIC=Vehicle.OwnerNIC AND Vehicle.LicenseNo= %s"  # using the forign key NIC
    mycursor.execute(query, tupleData)
    result = mycursor.fetchall()
    for i in result:
        data = " ".join(i)
        return data


def getAddr1(vehicleNumber):
    tupleData = (str(vehicleNumber),)  # %s should give as a tuple to execute
    query = "SELECT Owner.AddressLine1 FROM Owner,Vehicle WHERE Owner.NIC=Vehicle.OwnerNIC AND Vehicle.LicenseNo= %s"  # using the forign key NIC
    mycursor.execute(query, tupleData)
    result = mycursor.fetchall()
    for i in result:
        data = " ".join(i)
        return data


def getAddr2(vehicleNumber):
    tupleData = (str(vehicleNumber),)  # %s should give as a tuple to execute
    query = "SELECT Owner.AddressLine2 FROM Owner,Vehicle WHERE Owner.NIC=Vehicle.OwnerNIC AND Vehicle.LicenseNo= %s"  # using the forign key NIC
    mycursor.execute(query, tupleData)
    result = mycursor.fetchall()
    for i in result:
        data = " ".join(i)
        return data


def getAddr3(vehicleNumber):
    tupleData = (str(vehicleNumber),)  # %s should give as a tuple to execute
    query = "SELECT Owner.AddressLine3 FROM Owner,Vehicle WHERE Owner.NIC=Vehicle.OwnerNIC AND Vehicle.LicenseNo= %s"  # using the forign key NIC
    mycursor.execute(query, tupleData)
    result = mycursor.fetchall()
    for i in result:
        data = " ".join(i)
        return data


def getNIC(vehicleNumber):
    tupleData = (str(vehicleNumber),)
    query = "SELECT OwnerNIC FROM Vehicle WHERE LicenseNo = %s"
    mycursor.execute(query, tupleData)
    result = mycursor.fetchall()
    data = result[0][0]
    return str(data)


def getOwnerLicenceExpireDate(vehicleNumber):
    tupleData = (str(vehicleNumber),)
    query = "SELECT Owner.LicenceExpireDate FROM Owner,Vehicle WHERE Owner.NIC=Vehicle.OwnerNIC AND Vehicle.LicenseNo= %s"  # using the forign key NIC
    mycursor.execute(query, tupleData)
    result = mycursor.fetchall()
    data = result[0][0]
    return str(data)


def getBloodGroup(vehicleNumber):
    tupleData = (str(vehicleNumber),)
    query = "SELECT Owner.BloodGroup FROM Owner,Vehicle WHERE Owner.NIC=Vehicle.OwnerNIC AND Vehicle.LicenseNo= %s"  # using the forign key NIC
    mycursor.execute(query, tupleData)
    result = mycursor.fetchall()
    data = result[0][0]
    return str(data)

def getEntrance(vehicleNumber):
    tupleData = (str(vehicleNumber),)  # %s should give as a tuple to execute
    query = "SELECT From_ FROM Records WHERE VehicleNumber= %s"  # using the forign key NIC
    mycursor.execute(query, tupleData)
    result = mycursor.fetchall()
    for i in result:
        data = " ".join(i)
        return data



#have to check
def getArrivalTime(vehicleNumber):
    tupleData = (str(vehicleNumber),)  # %s should give as a tuple to execute
    query = "SELECT ArrivalTime FROM Records WHERE VehicleNumber= %s"  # using the forign key NIC
    mycursor.execute(query, tupleData)
    result = mycursor.fetchall()
    print(result)
    return result

#getArrivalTime("KC-2210") have to check
