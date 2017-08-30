"""Probe class implementation file."""
import math
from point import Point
from action import Action

"""
    N
    |
W - * - E
    |
    S
"""
DIRECTIONS = {
    'E': 0,
    'N': 90,
    'W': 180,
    'S': 270
}


class Probe(object):
    """Proble class implementation."""

    angle = 0
    position = Point()

    def __init__(self, initial_position, initial_direction):
        """Initialize the probe with the conditions."""
        self.angle = Probe.parse_input_direction(initial_direction)
        self.position = initial_position
        super(Probe, self).__init__()

    @staticmethod
    def parse_input_direction(input_value):
        """Parse the input value using the DIRECTIONS values."""
        if input_value not in DIRECTIONS:
            raise ValueError('The initial_direction value is not a valid '
                             'direction')
        return DIRECTIONS.get(input_value)

    @property
    def direction(self):
        """Return the angle as a readable string."""
        final_angle = self.angle - (math.floor(self.angle/360)*360)
        for key, value in DIRECTIONS.items():
            if value == final_angle:
                return key
        return "Error while getting readable direction"

    def runAction(self, action):
        """Run an action and update the probe position and angle."""
        if not isinstance(action, Action):
            raise ValueError('action argument should be an instance of Action')
        self.angle = self.angle + action.angle
        point_diff = self.getMovementDelta(action.move)
        self.position.add(point_diff)

    def getMovementDelta(self, move_delta):
        """Get movement diff point to move."""
        x_angle = math.cos(math.radians(self.angle))
        y_angle = math.sin(math.radians(self.angle))
        return Point(
            move_delta * x_angle,
            move_delta * y_angle)

    def draw(self):
        """Return the probe draw for UI."""
        if self.direction == 'N':
            return ' ⇧ '
        if self.direction == 'W':
            return ' ⇦ '
        if self.direction == 'S':
            return ' ⇩ '
        if self.direction == 'E':
            return ' ⇨ '
        return ' * '
