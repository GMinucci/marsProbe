"""Point class implementation file."""


class Point(object):
    """Simple point class to handle x and y position."""

    x = 0.0
    y = 0.0

    def __init__(self, x=0, y=0):
        """Overwrite default __init__ method."""
        self.x = x
        self.y = y
        super(Point, self).__init__()

    @property
    def readable(self):
        """Return the point as a readable string."""
        return "(x: %.1f, y:%.1f)" % (self.x, self.y)

    def add(self, point):
        """Sum point with the current point."""
        if not isinstance(point, Point):
            raise ValueError('Argument point should be an Point instance')
        self.x = self.x + point.x
        self.y = self.y + point.y
