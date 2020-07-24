import unittest

class TestSuite1(unittest.TestCase):
    
    def __init__(self, a, b, *args, **kwargs):
        super(*args, **kwargs).__init__()
        self.a = a
        self.b = b 


    def test_substract(self):
       # a,b = 5,10
        res = self.a - self.b
        self.assertEqual(res,5,"not matched")


if __name__ == "__main__":
    suite1 = TestSuite1(10,5)

    tc = unittest.FunctionTestCase(suite1.test_substract)

    suite = unittest.TestSuite()
    suite.addTest(tc)

    runner = unittest.TextTestRunner()
    runner.run(suite)

   