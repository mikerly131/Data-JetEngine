from random import choice

class RandomWalk:
    """A class to generate random walks"""

    def __init__(self, num_points=5000):
        """Constructor? Initialize variables of walk"""

        self.num_points = num_points

        # All walks start at (0,0)
        self.x_index = [0]
        self.y_index = [0]

    def fill_walk(self):
        """Calculate all the points in the walk"""

        # Keep taking steps until the walk reaches the max steps
        while len(self.x_index) < self.num_points:

            # decide which direction to go and how far in that direction
            x_direction = choice([1, -1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position
            x = self.x_index[-1] + x_step
            y = self.y_index[-1] + y_step
            
            self.x_index.append(x)
            self.y_index.append(y)