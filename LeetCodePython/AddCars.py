class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        # if big > 0:
        #     self.bigCars = [0] * big
        # if medium > 0:
        #     self.mediumCars = [0] * medium
        # if small > 0:
        #     self.smallCars = [0] * small
        self.bigCars = big
        self.mediumCars = medium
        self.smallCars = small

    def addCar(self, carType: int) -> bool:
        ## 1 = big, 2 = medium, 3 = small
        if carType == 1:
            self.bigCars -= 1

            if self.bigCars < 0:
                return False
        elif carType == 2:
            self.mediumCars -=  1

            if self.mediumCars < 0:
                return False
        elif carType == 3:
            self.smallCars -= 1

            if self.smallCars < 0:
                return False
        
        return True
        



# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)