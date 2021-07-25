class Employee:
    """COLLECTS INFORMATION ABOUT AN EMPLOYEE"""

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, amount=5000):
        self.salary += amount