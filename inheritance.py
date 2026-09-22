class Person:

    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name:", self.name)

class Student(Person):

    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def display_grade(self):
        print("Grade:", self.grade)

student = Student("Ruchitha", "A")

student.display_name()
student.display_grade()
