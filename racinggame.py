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

class Race:
    def __init__(self, track_lengh = 1000):
        self.track_lengh = track_lengh
        self.cars = []
        self.finished = False
    
    def add_car(self, car):
        self.cars.append(car)
    
    def show_position(self):
        for car in self.cars:
            print(f"car: {car.name} position: {car.position}")
    
    def race_turn(self):
        for car in self.cars:
            num = random.randint(0,3)
            for i in range(num):
                car.accelerate()
            car.move()
    
    def check_winner(self):
        for car in self.cars:
            if car.position >= self.track_lengh:
                return car.name
        return None

    def start_race(self):
        turn = 1
        while self.check_winner() is None:
            print(f'turn: {turn}')
            self.race_turn()
            self.show_position()
            turn += 1
        print(f"Winner: {self.check_winner()}")
 

def main():
    print("Welcom")
    race = Race()
    regulr_kilear = Car('regulr_kilear', 70)
    the_wind_cutter = SportCar('the_wind_cutter ')
    the_havy_weight = Truck('the_havy_weight')
    the_little_assassin = Motorcycle('the_little_assassin')
    race.add_car(regulr_kilear)
    race.add_car(the_wind_cutter)
    race.add_car(the_havy_weight)
    race.add_car(the_little_assassin)
    race.show_position()
    race.start_race()
    
main()

