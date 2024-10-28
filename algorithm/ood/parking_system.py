"""leet code 1603, easy"""


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        # Number of empty slots for each type of car
        self.empty = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.empty[carType - 1] > 0:
            self.empty[carType - 1] -= 1
            return True
        return False
