class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.current_floor = bottom_floor
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

    def go_to_floor(self, floor):
        self.current_floor = floor
        print(f"Elevator is now at floor {self.current_floor}")

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        if elevator_number < len(self.elevators):
            self.elevators[elevator_number].go_to_floor(destination_floor)

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.elevators[0].bottom_floor)

if __name__ == "__main__":
    building = Building(1, 10, 3)
    building.run_elevator(0, 5)
    building.fire_alarm()
