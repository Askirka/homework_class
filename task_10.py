class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_salary(self):
        return self.salary

    def get_tax(self):
        return 0.2 * self.salary


employee1 = Employee("Ivan Ivanov", "Manager", 50000)
employee2 = Employee("PEtr PEtrov", "INgineer", 60000)

print(f"{employee1.name} занимает должность {employee1.position}")
print(f"Зарплата: {employee1.get_salary()} руб.")
print(f"Налог: {employee1.get_tax()} руб.\n")

print(f"{employee2.name} занимает должность {employee2.position}")
print(f"Зарплата: {employee2.get_salary()} руб.")
print(f"Налог: {employee2.get_tax()} руб.")
