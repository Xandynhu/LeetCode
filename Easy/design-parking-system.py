# Solution author: Alexadre de Rosso Crestani
# Problem picked from Leet Code website: https://leetcode.com/

# Design a parking system for a parking lot.
# The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for each size.

# Implement the ParkingSystem class:

# ParkingSystem(int big, int medium, int small) -> Initializes object of the ParkingSystem class.
# The number of slots for each parking space are given as part of the constructor.

# bool addCar(int carType) -> Checks whether there is a parking space of carType for the car that wants to get into the parking lot.
# carType can be of three kinds: big, medium, or small, which are represented by 1, 2, and 3 respectively.
# A car can only park in a parking space of its carType. If there is no space available, return false, else park the car in that size space and return true.

# exemple 1:
# Input     ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
#           [[1, 1, 0], [1], [2], [3], [1]]
# Output    [null, true, true, false, false]

# Explanation
#           ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);
#           parkingSystem.addCar(1); // return true because there is 1 available slot for a big car
#           parkingSystem.addCar(2); // return true because there is 1 available slot for a medium car
#           parkingSystem.addCar(3); // return false because there is no available slot for a small car
#           parkingSystem.addCar(1); // return false because there is no available slot for a big car. It is already occupied.

class ParkingSystem:

    # initialize the Parking Lot with the amount of 1(big), 2(medium) and 3(small) spots
    def __init__(self, big: int, medium: int, small: int) -> None:
        self.park_dict = {1: big, 2: medium, 3: small}

    # defines a function addCar to, if it is possible, add a car in the parking lot
    def addCar(self, carType: int) -> bool:
        
        # if we have more than 0 spots available of that type of car size
        # element at dict[key] is bigger than 0
        if self.park_dict[carType] > 0:

            # subtracts 1 and return true, because we can parking the car
            self.park_dict[carType] -= 1
            return True
        
        # else, false
        return False





# Tests:
parking = ParkingSystem(0, 0, 1)
print(parking.park_dict)
print(parking.addCar(3))
print(parking.addCar(3))