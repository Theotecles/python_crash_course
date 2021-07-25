from car import Car

class Battery:
    """A SIMPLE ATTEMPT TO MODEL A BATTERY FOR AN ELECTRIC CAR."""

    def __init__(self, battery_size=75):
        """INITIALIZE THE BATTERY'S ATTRIBUTES."""
        self.battery_size = battery_size

    def describe_battery(self):
        """PRINT A STATEMENT DESCRIBING THE BATTERY SIZE."""
        print(f"This car has a {self.battery_size}-kwh battery.")

    def upgrade_battery(self, new_size):
        print(f"Current battery size is {self.battery_size}. Upgrading...")
        self.battery_size = new_size
        print(f"Battery size is now {self.battery_size}!")

    def get_range(self):
        """PRINT A STATEMENT ABOUT THE RANGE THIS BATTERY PROVIDES."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """REPRESENT ASPECTS OF A CAR, SPECIFIC TO ELECTRIC VEHICLES."""

    def __init__(self, make, model, year):
        """
        INITIALIZE ATTRIBUTES OF THE PARENT CLASS.
        THEN INITIALIZE ATTRIBUTES SPECIFIC TO AN ELECTRIC CAR.
        """
        super().__init__(make, model, year)
        self.battery = Battery()