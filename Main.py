# import unittest

# from Tests import TestCar


# if __name__ == "__main__":

#    # car = TestCar.TestCar("Maruthi 1000",2010,100,"Green")

#     unittest.main()

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

    
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()