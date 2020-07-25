import unittest 
from Models.Students import Students as stud

class UT_Students(unittest.TestCase):
   def __init__(self, *args, **kwargs):
     super(*args,**kwargs)
     self.students = stud.Students().students

   #def test_addStudent(self, name,dept):
    # self.students.addStudent(
