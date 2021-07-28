from random import choice

class RandomWalk:
    """A CLASS TO GENERATE RANDOM WALKS."""

    def __init__(self, num_points=5000):
        """INITIALIZE ATTRIBUTES OF A WALK."""
        self.num_points = num_points

        # ALL WALKS START AT (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """
        GETS THE DIRECTION FOR EACH NEW POINT IN THE RANDOM WALK
        """
        # DECIDE WHICH DIRECTION TO GO AND HOW FAR TO GO IN THAT DIRECTION
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        step = direction * distance

        return step

    def fill_walk(self):
        """CALCULATE ALL THE POINTS IN THE WALK."""

        # KEEP TAKING STEPS UNTIL THE WALK REACHES THE DESIRED LENGTH
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()
            # REJECT MOVES THAT GO NOWHERE
            if x_step == 0 and y_step == 0:
                continue

            # CALCULATE THE NEW POSITION
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
