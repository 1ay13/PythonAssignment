class Person:
  def __init__ (self, name, age, gender):
    self.name = name
    self.__age = age
    self.gender = gender

  def say_hello(self):
    print (f"Hello, {self.name} and your age is {self.__age}")

  def is_adult(self):
    if(self.__age > 18):
      return "true"
    else:
       return "false"

  def get_age(self):
        return self.__age

  def set_age(self, new_age):
      if new_age >= 0:
          self.__age = new_age
      else:
          print("Age cannot be negative.")

class Student(Person):
  def __init__ (self, student_id, course):
    self.student_id = student_id
    self.course = course

class Teacher(Student):
  def __init__ (self, teacher_id, subject):
    self.teacher_id = teacher_id
    self.subject = subject

  def say_hello(self):
        print(f"Hello, I am a teacher named {self.name}, teaching {self.subject}")


c1 = Person("Jay", 25, "male")
c1.say_hello()

t1 = Teacher("Teacher123", "Mathematics")
t1.name = "John"
t1.say_hello()

c1.is_adult()

c1.set_age(27)
c1.get_age()