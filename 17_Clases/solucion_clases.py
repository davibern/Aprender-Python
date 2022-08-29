class Vehiculo:
    
    wheels = 0
    doors = 0
    motor = ''
    cv = 0
    cc = 0
    
    def __init__(self, wheels, doors, motor, cv, cc):
        self.wheels = wheels
        self.doors = doors
        self.motor = motor
        self.cv = cv
        self.cc = cc
        print('Se ha instanciado correctamente.')
        
    def __str__(self):
        print(f'El vehículo tiene {self.wheels} ruedas, {self.doors} ruedas, su motor es de {self.motor}, tiene {self.cv} caballos y {self.cc} de cilindrada')

v = Vehiculo(4, 5, 'gasolina', 150, 1600)
v.__str__()