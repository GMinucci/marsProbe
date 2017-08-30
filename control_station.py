"""Control station file."""
from action import Action
from field import Field
from probe import Probe
from point import Point


class ControlStation(object):
    """Control station file to control the probes and the field."""

    allowed_actions = [
        Action(input_key="R", angle=-90),
        Action(input_key="L", angle=90),
        Action(input_key="M", move=1)
    ]
    field = None

    def validate_field(self):
        """Verify if field is configured properly."""
        if not self.field:
            raise ValueError('Should configure the field before any command')

    def parse_input_key(self, input_key):
        """Parse input_key into action."""
        self.validate_field()
        action = [action for action in self.allowed_actions
                  if action.input_key == input_key.upper()]
        if len(action) != 1:
            raise ValueError('The input_key is not allowed')
        return action[0]

    def parse_command_line(self, command_line):
        """Parse the input command_line."""
        ns_command_line = command_line.replace(' ', '').upper()
        com_list = list(ns_command_line)
        parsed_com_list = []
        for com in com_list:
            try:
                parsed_com_list.append(int(com))
            except ValueError:
                parsed_com_list.append(com)
        if any(isinstance(x, int) for x in parsed_com_list):
            if len(parsed_com_list) == 2:
                self.field = Field(parsed_com_list[0], parsed_com_list[1])
            elif len(parsed_com_list) == 3:
                self.validate_field()
                probe = Probe(
                    Point(parsed_com_list[0], parsed_com_list[1]),
                    initial_direction=parsed_com_list[2])
                self.field.insertProbe(probe)
            else:
                raise ValueError('Invalid input command')
        else:
            self.validate_field()
            for command in parsed_com_list:
                action = self.parse_input_key(command)
                final_position, direction = self.field.runActionOnProbe(action)
            print(final_position.readable, direction)
