import random
class Car:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed
        self.position = 0
        self.speed = 0

    def accelerate(self):
        if self.speed < self.max_speed:
            self.speed += 10
    
    def brake(self):
        if self.speed > 15:
            self.speed -= 15
    
    def move(self):
        self.position += self.speed
    
    def get_info(self):
        return f"car name: {self.name}, speed: {self.speed}, position: {self.position}"
    
class SportCar(Car):
    def __init__(self, name):
        super().__init__(name, max_speed = 100)
        self.turbo_available = True
    
    def  accelerate(self):
        self.speed += 15

    def use_turbo(self):
        if self.turbo_available:
            self.position += 50
            self.turbo_available = False

class Truck(Car):
    def __init__(self, name):
        super().__init__(name, max_speed = 60)

    def accelerate(self):
        self.speed += 8

    def brake(self):
       self.speed -= 5

    def ram(self, other_car):
        other_car.speed -= 20

class Motorcycle(Car):
    def __init__(self, name):
        super().__init__(name, max_speed = 80)
    
    def accelerate(self):
        self.speed += 12
    
    def weave(self):
        ran = random.randint(0, 20)
        self.position += ran
        
           
