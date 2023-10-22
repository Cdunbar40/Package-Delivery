# Contains a list for storing package information throughout the day, and methods for recording and retrieving that
# data.
import datetime
from PackageHashTable import PackageHashTable

class Recorder:
    # A dictionary of dictionaries. The outer key is a time, and the inner key is a package number. The value stored is
    # a string that lists the status of the selected package at the selected time.
    packageData = {}

    # A list of valid keys for the packageData dictionary. Allows the user to input times that do not perfectly match
    # an event timestamp, returning the most recent time to the input that will work as a valid key.
    timestamps = []

    # Stores the string value for all packages (which includes the status) using the given time as the key, for later
    # retrieval. O(N)
    @classmethod
    def recordData(cls, time):
        outerKey = time
        cls.packageData[outerKey] = {}
        cls.timestamps.append(time)
        for i in range(1, 41):
            innerKey = i
            package = PackageHashTable.lookup(i)
            cls.packageData[outerKey][innerKey] = str(package)

    # Retrieves the stored string for the given package at the given time and prints it. O(N)
    @classmethod
    def getTimestamp(cls, time, packageID):
        outerKey = datetime.timedelta(hours=0)

        if time < datetime.timedelta(hours=8):
            outerKey = cls.timestamps[0]
            timestamp = cls.packageData[outerKey][packageID]
            print(timestamp)
            return

        for i in range(len(cls.timestamps)):

            # If i is not the last element and time falls between i and i+1, OR
            # If i is the last element and time is greater than or equal to i,
            # set the value of outer key to i. This allows the user to enter
            # any time, and timestamps will return the most recent valid key to
            # the entered time.
            if (i < len(cls.timestamps) - 1 and (cls.timestamps[i] <= time < cls.timestamps[i + 1])) or (
                    cls.timestamps[i] <= time and i == len(cls.timestamps) - 1):
                outerKey = cls.timestamps[i]
                break

        timestamp = cls.packageData[outerKey][packageID]
        print(timestamp)

    # Retrieves and prints the status of all packages at the given time. O(N)
    @classmethod
    def getAllTimestamps(cls, time):
        outerKey = datetime.timedelta(hours=0)

        if time < datetime.timedelta(hours=8):
            outerKey = cls.timestamps[0]
        else:
            for i in range(len(cls.timestamps)):
                if (i < len(cls.timestamps) - 1 and (cls.timestamps[i] <= time < cls.timestamps[i + 1])) or (
                        cls.timestamps[i] <= time and i == len(cls.timestamps) - 1):
                    outerKey = cls.timestamps[i]
                    break
        for i in range(1, 41):
            timestamp = cls.packageData[outerKey][i]
            print(timestamp)
