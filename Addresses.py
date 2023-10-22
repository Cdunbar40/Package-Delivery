import csv


# Class meant for accessing Addresses and the distances between them, stored in the form of a nested dictionary, where
# the outer key is the 'from' address, the inner key is the 'to' address, and the value of the inner dictionary is the
# distance between the two.
class Addresses:
    allAddresses = {}  # Outer dictionary

    # Method to populate the dictionary, accepts a CSV file. Only needs access to the class member allAddresses
    @classmethod
    def generateAdjMatrix(cls, filename):
        with open(filename, encoding='utf-8-sig') as inputAddresses:
            rawdistances = csv.reader(inputAddresses, delimiter=',')  # Initial input, CSV methods for navigation
            distances = list(rawdistances)                            # aren't great, so converting to a list of lists
                                                                      # to make things easier

            # For each row from the CSV, assigns the list for that row to address. O(N^2)
            for rowNumber, address in enumerate(distances):
                outerKey = address[0]       # The outer key for the nested dictionary is always col 0
                currentRow = rowNumber      # Copying the current row number to iterate below
                i = 2 + rowNumber           # Distance values for the current FROM address are always in col[2+currRow]

                # Iterates through the addresses in col 1 of the CSV and assigns the distance value associated with that
                # address.
                while currentRow < len(distances):
                    innerKey = distances[currentRow][1] # Assigns the 'to' address, always col 1 of the current row
                    distance = distances[currentRow][i] # Assigns the distance from outerKey to innerKey

                    # If the outer dictionary doesn't already have an entry for the 'From' address, then create it
                    if outerKey not in cls.allAddresses:
                        cls.allAddresses[outerKey] = {}

                    # Populate the nested dictionary. [FROM][TO] = DISTANCE
                    cls.allAddresses[outerKey][innerKey] = float(distance)

                    # Since the distances are bidirectional, you can swap the outer and inner keys to get
                    # entries for both directions
                    placeholder = outerKey
                    outerKey = innerKey
                    innerKey = placeholder

                    if outerKey not in cls.allAddresses:
                        cls.allAddresses[outerKey] = {}

                    cls.allAddresses[outerKey][innerKey] = float(distance)

                    #Swap back for next iteration
                    placeholder = outerKey
                    outerKey = innerKey
                    innerKey = placeholder

                    # Iterate current Row to the next row,
                    currentRow += 1