"""Action main class."""


class Action(object):
    """Action base class."""

    angle = 0
    move = 0
    input_key = None

    def __init__(self, input_key, angle=0, move=0):
        """Overwrite default __init__."""
        self.angle = angle
        self.move = move
        self.input_key = input_key
        super(Action, self).__init__()
