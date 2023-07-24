class Person:
    def __init__(self,name,age):
        self.age = age
        self.name = name

    def say_hello(self):
        print(f"HEllo my name is,{self.name},and i am ,{self.age},age" )






person1 = Person('Ivan',22)
print(person1)
person1.say_hello()