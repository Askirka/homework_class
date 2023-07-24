class Car:
    def __init__(self,make,model,speed):
        self.make = make
        self.model = model
        self.speed = speed


    def accelerate(self,new_speed):
        new_speed = new_speed + self.speed
        print(new_speed)


    def brake(self,brake_limit):
        brake_limit = self.speed - brake_limit
        print(f"Скорость снижена до {brake_limit}")


    def get_speed(self):
        first_speed = self.speed
        print(f"первоначальная скорость {first_speed}")






car1 = Car('germany','v33',300)
print(car1.accelerate(1))

print(car1.brake(200))
print(car1.get_speed())