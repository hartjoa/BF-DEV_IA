class Vehicle:
    color = "White"

    def __init__(self, name: str, max_speed: float, mileage: float, capacity: int) -> None:
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

    def display_info(self) -> None:
        print(f"Color: {self.color} - Vehicle Name: {self.name} - Speed: {self.max_speed} - Mileage: {self.mileage}")

    def seating_capacity(self, capacity: int) -> None:
        print(f"The seating capacity of {self.name} is {capacity}")