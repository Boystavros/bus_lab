class Bus:
    def __init__(self, route, destination):
        self.route = route
        self.destination = destination
        self.passengers = []

    
    def drive(self):
        return "Brum Brum"
    
    def count_passengers(self):
        return len(self.passengers)

    def pick_up(self, passenger):
        self.passengers.append(passenger)

    def drop_off(self, passenger):
        self.passengers.remove(passenger)
    
    def empty(self):
        del self.passengers



