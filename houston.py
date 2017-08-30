"""Houston control station file."""
import os
from control_station import ControlStation


def main():
    """Main script function."""
    command_list = []
    command = 'X'
    while(command.upper() != ''):
        command = input("Insert the command: (Empty enter to finish) \n")
        if command.upper() != '':
            command_list.insert(len(command_list), command)

    station = ControlStation()
    for command in command_list:
        station.parse_command_line(command)
    print("End of commands!")
    print("Bye.")


if __name__ == "__main__":
    os.system('clear')
    main()
