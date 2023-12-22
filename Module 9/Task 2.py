class Car:
    def __init__(self, registration_number, maximum_speed,current_speed=0,travelled_distance=0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, change):
        new_speed=self.current_speed+change
        if new_speed > self.maximum_speed:
            self.current_speed=self.maximum_speed
        elif new_speed < 0:
            self.current_speed=0
        else:
            self.current_speed=new_speed

new_car=Car("ABC-123", 142)
new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)

print(f"Current Speed after acceleration: {new_car.current_speed} km/h")

new_car.accelerate(-200)

print(f"Final Speed after emergency brake:", new_car.current_speed, "km/h")