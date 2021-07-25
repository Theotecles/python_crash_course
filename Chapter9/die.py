import random

"""CREATE A DIE CLASS THAT WILL ALLOW US TO SIMULATE DICE ROLLS"""
class Die:
    """ATTEMPT TO MODEL A DIE"""

    def __init__(self, sides=6):
        """INITIALIZE ATTRIBUTES FOR DIE"""
        self.sides = sides

    def roll_die(self):
        print(f"The die has {self.sides} sides")
        print("Rolling...")
        print(random.randint(1, self.sides))

six_sided = Die()
six_sided.roll_die()
six_sided.roll_die()
six_sided.roll_die()
six_sided.roll_die()
six_sided.roll_die()
six_sided.roll_die()
six_sided.roll_die()
six_sided.roll_die()
six_sided.roll_die()
six_sided.roll_die()

ten_sided = Die(sides=10)
ten_sided.roll_die()
ten_sided.roll_die()
ten_sided.roll_die()
ten_sided.roll_die()
ten_sided.roll_die()
ten_sided.roll_die()
ten_sided.roll_die()
ten_sided.roll_die()
ten_sided.roll_die()
ten_sided.roll_die()

twenty_sided = Die(sides=20)
twenty_sided.roll_die()
twenty_sided.roll_die()
twenty_sided.roll_die()
twenty_sided.roll_die()
twenty_sided.roll_die()
twenty_sided.roll_die()
twenty_sided.roll_die()
twenty_sided.roll_die()
twenty_sided.roll_die()
twenty_sided.roll_die()