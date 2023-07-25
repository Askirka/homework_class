class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print("Гав-гав!")

    def get_human_age(self):

        human_years = self.age * 7
        return human_years

# Пример использования класса Dog
dog1 = Dog("Бобик", "Дворняжка", 3)
dog1.bark()
print(f"Имя собаки: {dog1.name}")
print(f"Порода собаки: {dog1.breed}")
print(f"Возраст собаки: {dog1.age} года")
print(f"Возраст собаки в 'человеческих' годах: {dog1.get_human_age()} лет")
