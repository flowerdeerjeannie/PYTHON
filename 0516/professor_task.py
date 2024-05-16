class Person:
     def __init__(self, pid, name, age):
          self.pid = pid
          self.name = name
          self.age = age
     def __str__(self):
        return f"Person ID: {self.pid}, Name: {self.name}, Age: {self.age}"

class Dept:
     def __init__(self, department):
          self.department = department

     def __str__(self):
        return self.department



class Student(Person):
     def __init__(self, pid, name, age, sid, syear, dept):
          super().__init__(pid, name, age)
          self.sid =sid
          self.syear = syear 
          self.dept = dept
     def __str__(self):
        return f"Student ID: {self.pid}, Name: {self.name}, Age: {self.age}, ID: {self.sid}, year:{self.syear}, dept:{self.dept}"



d1 = Dept('java')
p1 = Person(1, '가영', 20)
p2 = Person(2, '나영', 21)
p3 = Person(3, '다영', 22)
p4 = Person(4, '라영', 23)
p5 = Person(5, '마', 24)
s1 = Student(6, '바', 25, 201334121, 3, d1)
s2 = Student(7, '사', 26, 201234423, 1, d1)
s3 = Student(8, '아', 27, 2013323412, 2, d1)
s4 = Student(9, '자', 28, 2013234412, 4, d1)
s5 = Student(10, '차', 29, 202451249, 1, d1)


object_list = [s1, s2, s3, s4, s5, p1, p2, p3, p4, p5]

for obj in object_list:
     print(obj)


