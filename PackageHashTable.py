# TASK A: Package Hash Table creates a HashTable implementation for storing package information by ID number, enabling quick
# lookup and retrieval. This information includes the delivery address, city, zipcode, and deadline, as well as the
# status of a package at a given time.
class PackageHashTable:
    # Hash table constructor, initialized as an empty list of lists, with default size 10. This allows for a chaining
    # implementation in the hash table. O(N)
    hashTable = []

    def __init__(self, size=10):
        PackageHashTable.hashTable = []
        for i in range(size):
            PackageHashTable.hashTable.append([])

    # Adds a package to the hashTable. O(N)
    @classmethod
    def insert(cls, key, item):
        bucketIndex = hash(key) % len(cls.hashTable)  # retrieves the appropriate bucket index based on ID
        bucket = cls.hashTable[bucketIndex]                 # retrieves the list at that index
        bucket.append(item)                             # adds the package info to that list.

    # TASK B: Retrieves package information given a valid package ID. Returns a Package object, which contains the address,
    # deadline, delivery city, delivery zip code, package weight, and status. O(N)
    @classmethod
    def lookup(cls, key):
        bucketIndex = hash(key) % len(cls.hashTable)  # retrieves the appropriate bucket index based on ID
        bucket = cls.hashTable[bucketIndex]                 # retrieves the list at that index
        for item in bucket:                                 # searches each package in the bucket for a matching ID
            if key == item.id:
                return item                                 # if found returns the package, otherwise returns None
        return None







