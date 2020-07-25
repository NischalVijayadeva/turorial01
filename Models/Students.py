import unittest 


class Student:
  def __init__(self, id, name, dept):
     self.id = id 
     self.name = name
     self.dept = dept

class Students:
  def __init__(self):
     self.students = list()

  def addStudent(self, name, dept):
     self.students.append(len(self.students)+1, name, dept)

  def removeStudentById(self, id):
     stud = getStudentById(id)
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

  
  
