import unittest
from Classes import Car

class TestCar(unittest.TestCase):
    def __init__(self, model, year, price, color, *args,**kwargs):
        super(*args,**kwargs).__init__()
        self.car = Car.Car(model,year,price,color)
        self.direction = None
        
    # def testcreateCar(self):
    #     self.car = Car.Car(self.model,self.year,self.price,self.color)
    #     self.assertNotEqual(self.car,None,"Car not created!!")

    def test_carStart(self):
        self.car.start()
        self.assertNotEqual(self.car.ignision,"Off","Car not started!!")

    def test_carMove(self):
        self.car.move(self.direction)
        self.assertNotEqual(self.car.direction,None,"Car not moved!!")

    def test_carStop(self):
        self.car.stop()
        self.assertNotEqual(self.car.direction,"ON","Car not stopped!!")


