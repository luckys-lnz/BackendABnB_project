#!/usr/bin/python3

"""
    contains the entry point of the command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
        An entry point to the command interpreter
        which Validates the storage engine
    """
    prompt = '(hbnb) '

    def emptyline(self):
        """" Do nothing when empty line is executed"""
        pass

    def do_quit(self, line):
        """ Quit Command to exit the program """
        return True

    def do_EOF(self, line):
        """ Exit the program at the End Of File """
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

