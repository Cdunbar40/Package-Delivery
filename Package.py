import csv

from PackageHashTable import PackageHashTable


# Holds all data members for a package, and defines a string method for outputting package info.
class Package:

    def __init__(self, id, address, city, state, zip, deadline, weight, status):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.status = status

    # Defines the output for if a package is printed or cast to a string. Makes storing information in the Recorder class
    # easier
    def __str__(self):
        return f'Package: {self.id}, Status: {self.status}, Deadline: {self.deadline}, Delivery Address: {self.address}, City: {self.city}, State: {self.state}, Zip Code: {self.zip}, Weight: {self.weight}'

    # Takes the imported csv from main and iterates through it, generating new package objects and storing them in the
    # hash table. O(N)
    @staticmethod
    def loadPackages(fileName):
        with open(fileName) as packageInfo:
            packages = csv.reader(packageInfo, delimiter=',')
            next(packages)
            for package in packages:
                packageID = int(package[0])
                address = package[1]
                city = package[2]
                state = package[3]
                zip = package[4]
                deadline = package[5]
                weight = package[6]
                status = package[7]
                item = Package(packageID, address, city, state, zip, deadline, weight, status)
                PackageHashTable.insert(packageID, item)
