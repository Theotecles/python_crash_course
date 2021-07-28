from random import randint

class Die:
    """A CLASS REPRESENTING A SINGLE DIE."""

    def __init__(delf, num_sides-6):
        """ASSUME A SIX-SIDED DIE."""
        self.num_sides = num_sides

    def roll(self):
        """RETURN A RANDOM VALUE BETWEEN 1 AND NUMBER OF SIDES."""
        return randint(1, self.num_sides)