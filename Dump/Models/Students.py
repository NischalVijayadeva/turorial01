import unittest 
import Models

class Student:
  def __init__(self, id, name, dept):
     self.id = id 
     self.name = name
     self.dept = dept

class Students:
  def __init__(self):
     self.students = list()

  def addStudent(self, name, dept):
     id = len(self.students)+1
     self.students.append(Student(id, name, dept))
     return id

  def removeStudentById(self, id):
     stud = self.getStudentById(id)
     self.students.remove(stud)

  def getStudentById(self, id):
      for s in self.students:
        if (s.id == id):
           return s


if __name__=="__main__":
   students = Students()
   students.addStudent("Nischal","IT")
   students.addStudent("TestUser","BA")

   print(len(students.students))

  
  
