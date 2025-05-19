class Engine:
    def start(self):
        print("Engine had started")
class Car:
    def __init__(self,engine):
        self.engine = engine

    def startCar(self):
     print("Car is started..")
     self.engine.start()
engi = Engine()
car = Car(engi)
car.startCar()            
