import unittest
from UnitTests import UT_Students as UT_Stud

if __name__ == "__main__":
    testStud = UT_Stud.UT_Students()
    
    # Setup test data for TC1
    testStud.id = 2
    testStud.name = "Test"
    testStud.dept = "Bank"

    tc1 = unittest.FunctionTestCase(testStud.test_addStudent)

    # Setup test data for TC2
    testStud.id = 1
    tc2 = unittest.FunctionTestCase(testStud.test_getStudent)

    ts = unittest.TestSuite()
    ts.addTest(tc1)
    ts.addTest(tc2)

    runner = unittest.TextTestRunner()
    runner.run(ts)