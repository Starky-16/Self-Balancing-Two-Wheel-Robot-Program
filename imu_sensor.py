import random

class IMUSensor:
    def __init__(self):
        pass

    def get_angle(self):
        # Simulate tilt angle (replace with ROS topic subscription in real case)
        return random.uniform(-5, 5)
