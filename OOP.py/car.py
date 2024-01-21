class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    # METHODS
    def drive(self):
        print("The " + self.model+ "  is moving")

    def stop(self):
        print("This  " + self.model+ "  has stopped")