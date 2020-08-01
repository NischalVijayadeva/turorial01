import unittest
from Classes import Car

class TestCar(unittest.TestCase):
    def __init__(self, model="Maruthi", year=2010, price=100, color="RED", *args,**kwargs):
        super(TestCar,self).__init__(*args,**kwargs)
        self.car = Car.Car(model,year,price,color)
        
    # def testcreateCar(self):
    #     self.car = Car.Car(self.model,self.year,self.price,self.color)
    #     self.assertNotEqual(self.car,None,"Car not created!!")

   
    def test_carStart(self):
        self.car.start()
        self.assertNotEqual(self.car.ignision,"Off","Car not started!!")

    def test_carMove(self):
        self.direction = "Reverse"
        self.car.move(self.direction)
        self.assertNotEqual(self.car.direction,None,"Car not moved!!")

    def test_carStop(self):
        self.car.stop()
        self.assertNotEqual(self.car.ignision,"ON","Car not stopped!!")


