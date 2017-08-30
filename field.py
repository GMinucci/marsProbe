"""Field implementation file."""
import os
import time
from point import Point
from probe import Probe


class Field(object):
    """Map field to the probe."""

    width = 0
    height = 0
    probes = []

    def __init__(self, width, height):
        """Overwrite default __init__ function."""
        self.width = width + 1
        self.height = height + 1
        super(Field, self).__init__()

    def _contains(self, point):
        """Check if field contains point."""
        if not isinstance(point, Point):
            raise ValueError('Argument point should be an Point instance')
        return 0 <= point.x <= self.width and 0 <= point.y <= self.height

    def validateProbePosition(self, position):
        """Validate if position is inside the field.

        If the final position is not inside the field return last possible
        position inside the field.
        return: (True, point)
                (False, point)
        """
        if self._contains(position):
            return (True, position)

        last_x = max(0, min(self.width, position.x))
        last_y = max(0, min(self.height, position.y))
        return (False, Point(x=last_x, y=last_y))

    def insertProbe(self, probe, drawing=True):
        """Add probe into the field."""
        if not isinstance(probe, Probe):
            raise ValueError('action argument should be an instance of Probe')
        self.probes.append(probe)
        self.drawField()

    def runActionOnProbe(self, action, is_last=True, probe_id=0, drawing=True):
        """Move the probe at id or the last added probe."""
        if not is_last:
            raise NotImplementedError('Function not implemented yet')
        if len(self.probes) <= 0:
            return
        probe = self.probes[-1]
        probe.runAction(action)
        (is_inside, in_position) = self.validateProbePosition(probe.position)
        if not is_inside:
            probe.position = in_position
        if drawing:
            self.drawField()
        return probe.position, probe.direction

    def point_representation(self, point):
        """Return the point representation of the desired point for the UI."""
        for probe in self.probes:
            if point.x <= probe.position.x < point.x + 1 and \
               point.y <= probe.position.y < point.y + 1:
                return probe.draw()
        return ' * '

    def drawField(self):
        """Return the the UI field draw."""
        time.sleep(1)
        os.system('clear')
        final_draw = ""
        for y in reversed(range(self.height)):
            line_draw = ""
            for x in range(self.width):
                self.point_representation(Point(x, y))
                line_draw += self.point_representation(Point(x, y))
            line_draw += '\n'
            final_draw += line_draw
        print(final_draw)
