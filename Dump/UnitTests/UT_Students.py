import unittest
from Models import Students as stud
#from .Models.Students import Students as stud

class UT_Students(unittest.TestCase):
  def __init__(self, *args, **kwargs):
    super(*args,**kwargs)
    self.students = stud.Students()

  def setUp(self):
    self.id = 1
    self.name = "Nischal"
    self.dept = "IT"

  def test_addStudent(self):
    id = self.students.addStudent(self.name, self.dept)
    stud = self.students.getStudentById(id)
    self.assertIn(stud, self.students.students, "Student {} does not exist".format(self.name))

  def test_getStudent(self):
    stud = self.students.getStudentById(self.id)
    self.assertIn(stud, self.students.students, "Student with ID: {} does not exist".format(self.id))
