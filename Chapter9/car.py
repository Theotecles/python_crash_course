# CREATE A CAR CLASS
"""A SET OF CLASSES USED TO REPRESENT GAS AND ELECTRIC CARS"""
class Car:
    """A SIMPLE ATTEMPT TO REPRESENT A CAR."""

    def __init__(self, make, model, year):
        """INITIALIZE ATTRIBUTES TO DESCRIBE A CAR."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """RETURN A NEATLY FORMATTED DESCRIPTIVE NAME."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """PRINT A STATEMENT SHOWING THE CAR'S MILEAGE"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
         """
         SET THE ODOMETER READING TO THE GIVEN VALUE.
         REJECT THE CHANGE IF IT ATTEMPTS TO ROLL THE ODOMETER BACK.
         """
         if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
         else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """ADD THE GIVEN AMOUNT TO THE ODOMETER READING"""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")