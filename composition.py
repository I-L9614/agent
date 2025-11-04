# class Engine:
#     def info(self):
#         print("Engine: 2.0L Turbo")

# class Owner:
#     def info(self):
#         print("Owner:Moshe")

# class Car(Engine,Owner):
#     pass
class Car:
    def __init__(self, Engine, Owner):
        self.Engine = Engine
        self.Owner = Owner

class Engine:
    def info(self):
        print("Engine: 2.0L Turbo")

class Owner:
    def info(self):
        print("Owner:Moshe")


my_car = Car(Engine(), Owner())
my_car.Engine.info()
my_car.Owner.info()
