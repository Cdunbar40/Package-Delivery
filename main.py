# TASK C: C950 DSA II, by Colin Dunbar, ID 010839086

import datetime
from Addresses import Addresses
from Package import Package
from PackageHashTable import PackageHashTable
from Recorder import Recorder
from Truck import Truck
import sys

# Sim start. All statements in main are O(1)
print('Welcome to the WGUPS Package Tracking System. Executing sim...\n')

# Importing CSVs and running the delivery sim
Addresses.generateAdjMatrix('WGUPS Distance Table.csv')
myPackages = PackageHashTable()
Package.loadPackages('packages.csv')

truck1 = Truck('truck1')
t2StartTime = datetime.timedelta(hours=9, minutes=5)
truck2 = Truck('truck2', t2StartTime)
Truck.runSimulation(truck1, truck2)
print(
    f'All trucks returned to hub and all packages delivered by {truck2.time}. Truck 1 total miles = {truck1.milesTraveled:.1f}. Truck 2 total miles = {truck2.milesTraveled:.1f}\n')

# Initializing a few variables to use for the UI
closeApp = False
packageSelection = 1
userTime = 0

# Keep the UI running until exited by the user
while not closeApp:
    try:
        timeSelection = input('If you would like to view the status of a package, please enter a time '
                              '(formatted as HH:MM:SS). Otherwise, enter 0 to close the application\n').split(':')

        # If the input is 0, end the program
        if (len(timeSelection) == 1) and (timeSelection[0] == '0'):
            sys.exit()

        # Otherwise try to parse the input into a datetime.timedelta object
        else:
            for i in range(len(timeSelection)):
                timeSelection[i] = int(timeSelection[i])
            # noinspection PyTypeChecker
            userTime = datetime.timedelta(hours=timeSelection[0], minutes=timeSelection[1], seconds=timeSelection[2])
            packageSelection = 1
    except TypeError:
        print('Please enter a valid command')
        packageSelection = 0
    except NameError:
        print('Please enter a valid command')
        packageSelection = 0
    except IndexError:
        print('Please enter a valid command')
        packageSelection = 0

    # Submenu for selecting what you want to see for the given time
    while packageSelection != 0 and packageSelection != 3:
        print(f'Checking package status at {userTime}')
        packageSelection = int(input('Select one of the following options:\n'
                                     '1: View all packages\n'
                                     '2: View a specific package\n'
                                     '3: Return to previous menu\n'  # Entering 3 is an exit condition for the inner while loop, and puts you back in the time input UI    
                                     '0: Close application\n\n'))

        if packageSelection == 0:
            sys.exit()
        elif packageSelection == 1:
            Recorder.getAllTimestamps(userTime)
        elif packageSelection == 2:
            packageSelection = int(input('Enter the package ID that you would like to view:\n'))
            if packageSelection < 1 or packageSelection > 40:
                print('Invalid package number, returning to previous menu\n')
            else:
                Recorder.getTimestamp(userTime, packageSelection)
        print('\n')

sys.exit()
