# CREATE A DOG CLASS
class Dog:
    """A SIMPLE ATTEMPT TO MODEL A DOG"""

    def __init__(self, name, age):
        """INITIALIZE NAME AND AGE ATTRIBUTES"""
        self.name = name
        self.age = age

    def sit(self):
        """SIMULATE A DOG SITTING IN RESPONSE TO A COMMAND"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """SIMULATE ROLLING OVER IN RESPONSE TO A COMMAND"""
        print(f"{self.name} rolled over!")

# DEFINE A DOG
my_dog = Dog('Reggie', 1)

print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")
my_dog.sit()
my_dog.roll_over()

# DEFINE ANOTHER DOG
your_dog = Dog('Willie', 6)

print(f"My dog's name is {your_dog.name}")
print(f"My dog is {your_dog.age} years old")
your_dog.sit()
your_dog.roll_over()