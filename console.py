#!/usr/bin/python3

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    The entry point for the command interpreter
    """
    prompt = '(hbnb) '

    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
    }

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file),
        and prints the id. Ex: $ create BaseModel
        """
        args = line.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        elif args[0] not in HBNBCommand.classes:
            print('** class doesn\'t exist **')
            return
        new_instance = HBNBCommand.classes[args[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234.
        """
        args = line.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        elif args[0] not in HBNBCommand.classes:
            print('** class doesn\'t exist **')
            return
        elif len(args) < 2:
            print('** instance id missing **')
            return
        key = args[0] + '.' + args[1]
        all_objects = storage.all()
        if key not in all_objects:
            print('** no instance found **')
        else:
            print(all_objects[key])

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234.
        """
        args = line.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        elif args[0] not in HBNBCommand.classes:
            print('** class doesn\'t exist **')
            return
        elif len(args) < 2:
            print('** instance id missing **')
            return
        key = args[0] + '.' + args[1]
        all_objects = storage.all()
        if key not in all_objects:
            print('** no instance found **')
        else:
            del all_objects[key]
            storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name. Ex: $ all BaseModel or $ all
        """
        args = line.split()
        result = []
        if len(args) != 0:
            if args[0] not in HBNBCommand.classes:
                print('** class doesn\'t exist **')
                return
            else:
                for key, value in storage.all().items():
                    if type(value).__name__ == args[0]:
                        result.append(value.__str__())
        else:
            for key, value in storage.all().items():
                result.append(value.__str__())
        print(result)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or updating attribute
        (save the change into the JSON file). Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        args = line.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        elif args[0] not in HBNBCommand.classes:
            print('** class doesn\'t exist **')
            return
        elif len(args) < 2:
            print('** instance id missing **')
            return
        key = args[0] + '.' + args[1]
        all_objects = storage.all()
        if key not in all_objects:
            print('** no instance found **')
            return
        elif len(args) < 3:
            print('** attribute name missing **')
            return
        elif len(args) < 4:
            print('** value missing **')
            return
        instance = all_objects[key]
        attr_name = args[2]
        attr_value = args[3]
        setattr(instance, attr_name, attr_value)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

