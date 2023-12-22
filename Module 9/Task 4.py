import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.traveled_distance = 0

    def accelerate(self):
        self.current_speed = max(0, min(self.max_speed, self.current_speed + random.randint(-10, 15)))

    def drive(self):
        self.traveled_distance += self.current_speed

if __name__ == "__main__":
    num_cars = 10
    cars = [Car(f"ABC-{i}", random.randint(100, 200)) for i in range(1, num_cars + 1)]

    while all(car.traveled_distance < 10000 for car in cars):
        for car in cars:
            car.accelerate()
            car.drive()

    print("\nRace Results:")
    for car in cars:
        print(f"{car.registration_number:<15} {car.max_speed:<15} {car.current_speed:<15} {car.traveled_distance:<15}")
