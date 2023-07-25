class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Привет, меня зовут {self.name} и мне {self.age} лет.")

    def can_vote(self):
        return self.age >= 18


person1 = Person("Анна", 25)
person1.say_hello()
print(f"Может ли голосовать: {person1.can_vote()}")

person2 = Person("Петр", 16)
person2.say_hello()
print(f"Может ли голосовать: {person2.can_vote()}")
