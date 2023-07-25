class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def is_honors_student(self):
        return self.get_average_grade() > 4.5

student1 = Student("Иван", 20)
student1.add_grade(4.5)
student1.add_grade(5.0)
student1.add_grade(4.8)

print(f"Имя студента: {student1.name}")
print(f"Возраст студента: {student1.age}")
print(f"Средний балл студента: {student1.get_average_grade()}")
print(f"Студент является отличником: {student1.is_honors_student()}")
