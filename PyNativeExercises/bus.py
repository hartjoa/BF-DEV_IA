from vehicle import Vehicle

class Bus(Vehicle):
    def seating_capacity(self, capacity = 50):
        super().seating_capacity(capacity)
    
    def fare(self):
        return 1.1 * super().fare()