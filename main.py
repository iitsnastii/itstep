class Student:
    print("Hi")

first_student = Student()

class Student:
    print("Hi")
    def __init__(self):
        self.height = 160
        print("I am alive!")
first_student = Student()

class Student:
    def __init__(self):
        self.height = 160
        print(self)
first_student = Student()


class Student:
    amount_of_students = 0
    def __init__(self, height= 160):
        self.height = height
        Student.amount_of_students += 1
    def grow(self, height= 1):
            self.height += height
nick = Student()
kate = Student(height= 170)
nick.grow(height= 15)
print(kate.height)
print(nick.height)

