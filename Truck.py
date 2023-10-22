import datetime
import queue
from Addresses import Addresses
from PackageHashTable import PackageHashTable
from Recorder import Recorder


# The truck class contains all methods and data structures needed to load packages and select the route to take based
# off of the packages held.
class Truck:
    speed = float(18)  # All trucks run at the same speed, so just made this a static var
    p9AddressUpdated = False  # Used to track if the address for package 9 has been updated yet (per special
                              # requirements)

    # Constructor
    def __init__(self, name, time=datetime.timedelta(hours=8, minutes=0), currAddress='4001 South 700 East 84107'):
        self.name = name
        self.time = time
        self.currAddress = currAddress
        self.cargo = []
        self.route = queue.Queue(16)  # Limits queue size, though it's a bit redundant due to the addCargo method and
        # due to manually loading packages.
        self.milesTraveled = 0

    # Adds packages to the truck. Attempting to add packages when there are already 16 results in an error. O(1)
    def addCargo(self, package):
        if len(self.cargo) == 16:
            print('Cannot add package: Truck is already full')
        else:
            self.cargo.append(package)
            package.status = 'En Route'  # Once a package is on the truck, it is officially En Route.
            # print(f'Package {package.id} has been loaded onto {self.name}')

    # Simulates a trucks route based on the packages in cargo. Uses a greedy nearest neighbor algorithm to determine
    # which package is the next one to be delivered. O(N^2)
    def simulateRoute(self):
        # Initializes the distance to the next stop to infinity. This ensures that, if a
        # package has yet to be delivered, it will be tagged as the next shorted route.
        nextStopDist = float('inf')

        checkTime = datetime.timedelta(hours=10, minutes=20)
        # Route is a queue used to hold packages as they are being
        # delivered. It could also have been a list or array, but a
        # queue made more sense in my head. While there are still
        # packages left to deliver....
        while self.route.qsize() < len(self.cargo):
            for package in self.cargo:
                # If a package is already marked as delivered, skip it
                if package.status.startswith('Delivered'):
                    continue

                # Get the delivery address and the distance
                delAddress = package.address + ' ' + package.zip
                distance = Addresses.allAddresses[self.currAddress][delAddress]

                # If the distance of the package is less than the distance to deliver the current next package, then
                # make this package the next one to be delivered.
                # print(f'Package {package.id} distance is {distance}')
                if distance < nextStopDist:
                    nextPackage = package
                    nextStopDist = distance

            # Once all packages left in cargo have been evaluated, add the next package to the queue, "travel" to that
            # address, update the mileage and time, mark the package as delivered and give it a timestamp, then reset
            # the next stop distance to inf for the next loop through cargo.
            self.route.put(nextPackage)
            self.currAddress = nextPackage.address + " " + nextPackage.zip
            self.milesTraveled += nextStopDist
            duration = 1 / (self.speed / 60.0) * nextStopDist
            self.time = self.time + datetime.timedelta(hours=0, minutes=duration)
            nextPackage.status = f'Delivered at {self.time}'
            Recorder.recordData(self.time)
            nextStopDist = float('inf')
            if self.time >= checkTime and self.p9AddressUpdated == False:
                p9 = PackageHashTable.lookup(9)
                p9.address = '410 S State St'
                p9.city = 'Salt Lake City'
                p9.state = 'UT'
                p9.zip = '84111'
                self.p9AddressUpdated = True

        # Once out of the while loop, all packages have been delivered. Below calculates time/distance for returning
        # to the hub.
        self.route.queue.clear()
        self.cargo.clear()
        distance = Addresses.allAddresses[self.currAddress]['4001 South 700 East 84107']
        self.milesTraveled += distance
        self.currAddress = '4001 South 700 East 84107'
        duration = 1 / (self.speed / 60.0) * distance
        self.time = self.time + datetime.timedelta(hours=0, minutes=duration)

    # Used to manually load the truck and execute the route without cluttering main. O(1)
    @staticmethod
    def runSimulation(truck1, truck2):
        #Making sure to record package status before and after delivery
        preShipTime = datetime.timedelta(hours=7)
        Recorder.recordData(preShipTime)
        truck1.addCargo(PackageHashTable.lookup(14))
        truck1.addCargo(PackageHashTable.lookup(15))
        truck1.addCargo(PackageHashTable.lookup(16))
        truck1.addCargo(PackageHashTable.lookup(34))
        truck1.addCargo(PackageHashTable.lookup(19))
        truck1.addCargo(PackageHashTable.lookup(13))
        truck1.addCargo(PackageHashTable.lookup(39))
        truck1.addCargo(PackageHashTable.lookup(29))
        truck1.addCargo(PackageHashTable.lookup(7))
        truck1.addCargo(PackageHashTable.lookup(1))
        truck1.addCargo(PackageHashTable.lookup(8))
        truck1.addCargo(PackageHashTable.lookup(30))
        truck1.addCargo(PackageHashTable.lookup(20))
        truck1.addCargo(PackageHashTable.lookup(21))
        truck1.addCargo(PackageHashTable.lookup(4))
        truck1.addCargo(PackageHashTable.lookup(40))
        Recorder.recordData(truck1.time)
        truck1.simulateRoute()  # Route simulated once the truck is full.


        preShipTime = datetime.timedelta(hours=9, minutes=4, seconds=59)
        Recorder.recordData(preShipTime)
        truck2.addCargo(PackageHashTable.lookup(6))
        truck2.addCargo(PackageHashTable.lookup(32))
        truck2.addCargo(PackageHashTable.lookup(25))
        truck2.addCargo(PackageHashTable.lookup(38))
        truck2.addCargo(PackageHashTable.lookup(18))
        truck2.addCargo(PackageHashTable.lookup(36))
        truck2.addCargo(PackageHashTable.lookup(3))
        truck2.addCargo(PackageHashTable.lookup(28))
        truck2.addCargo(PackageHashTable.lookup(26))
        truck2.addCargo(PackageHashTable.lookup(37))
        truck2.addCargo(PackageHashTable.lookup(5))
        truck2.addCargo(PackageHashTable.lookup(31))
        truck2.addCargo(PackageHashTable.lookup(27))
        truck2.addCargo(PackageHashTable.lookup(35))
        truck2.addCargo(PackageHashTable.lookup(2))
        truck2.addCargo(PackageHashTable.lookup(33))
        Recorder.recordData(truck2.time)
        truck2.simulateRoute()

        # Refilling truck 2 with the rest of the packages.
        truck2.addCargo(PackageHashTable.lookup(24))
        truck2.addCargo(PackageHashTable.lookup(23))
        truck2.addCargo(PackageHashTable.lookup(10))
        truck2.addCargo(PackageHashTable.lookup(22))
        truck2.addCargo(PackageHashTable.lookup(11))
        truck2.addCargo(PackageHashTable.lookup(9))
        truck2.addCargo(PackageHashTable.lookup(17))
        truck2.addCargo(PackageHashTable.lookup(12))
        Recorder.recordData(truck2.time)
        truck2.simulateRoute()

        # Sorting the time values so that Recorder.getTimestamps works as intended
        Recorder.timestamps.sort()
