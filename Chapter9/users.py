# CREATE A USER CLASS
class User:
    """ATTEMPT TO MODEL A USER"""

    def __init__(self, first_name, last_name, city, country, age):
        """INITIALIZE DIFFERENT ATTRIBUTES FOR THE USER"""
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.country = country
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """WRITES A BRIEF DESCRIPTION ABOUT THE USER"""
        print(f"{self.first_name.title()} {self.last_name.title()} is {self.age} years old and lives in {self.city.title()}, {self.country.title()}")

    def greet_user(self):
        """WRITES A SIMPLE GREETING TO THE USER"""
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")

    def increment_login_attempts(self):
        """INCREASES TOTAL NUMBER OF LOGIN ATTEMPTS BY 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0