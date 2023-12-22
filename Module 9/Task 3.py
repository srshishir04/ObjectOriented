class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        new_speed = self.current_speed + change
        if new_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed
    def drive(self,hours):
        distance=self.current_speed*hours
        self.travelled_distance +=distance


new_car=Car("ABC-123", 142)

new_car.accelerate(60)

new_car.drive(1.5)

print(f"Travelled Distance after driving for 1.5 hours:", new_car.travelled_distance, "km")