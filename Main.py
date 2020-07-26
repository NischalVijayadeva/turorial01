import unittest

from Tests import TestCar


if __name__ == "__main__":

    car = TestCar.TestCar("Maruthi 800",2010,100,"Green")

    unittest.main()

    # ftc2 = unittest.FunctionTestCase(car.testcarStart)

    # car.direction = "forward"

    # ftc3 = unittest.FunctionTestCase(car.testcarMove)
    # ftc4 = unittest.FunctionTestCase(car.testcarStop)
    
    # ts = unittest.TestSuite()
    # ts.addTest(ftc2)
    # ts.addTest(ftc3)
    # ts.addTest(ftc4)

    # runner = unittest.TextTestRunner()
    # runner.run(ts)

    
