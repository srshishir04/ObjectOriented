class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.traveled_distance = 0

    def accelerate(self, speed):
        self.current_speed = min(self.max_speed, speed)

    def drive(self, hours):
        self.traveled_distance += self.current_speed * hours

class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume

if __name__ == "__main__":
    electric_car = ElectricCar("ABC-15", 180, 52.5)
    gasoline_car = GasolineCar("ACD-123", 165, 32.3)

    electric_car.accelerate(150)
    electric_car.drive(3)
    print(f"Electric Car Traveled Distance: {electric_car.traveled_distance} km")

    gasoline_car.accelerate(140)
    gasoline_car.drive(3)
    print(f"Gasoline Car Traveled Distance: {gasoline_car.traveled_distance} km")
