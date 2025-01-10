class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.b=big
        self.m=medium
        self.s=small

    def addCar(self, carType: int) -> bool:
        if carType==1:
            if self.b>0:
                self.b-=1
                return True
            else:
                return False
        elif carType==2:
            if self.m>0:
                self.m-=1
                return True
            else:
                return False
        elif carType==3:
            if self.s>0:
                self.s-=1
                return True
            else:
                return False            

obj = ParkingSystem(1, 1, 0)
print(obj.addCar(1))
print(obj.addCar(2))
print(obj.addCar(3))
print(obj.addCar(1))