#!/usr/bin/python3
"""
Module Console
"""
from __future__ import print_function, unicode_literals
import cmd
import shlex
import sys
import models
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """HBNB Class """

    prompt = '(hbnb) '
    classes = {
        'BaseModel': BaseModel, 'Amenity': Amenity, 'State': State,
        'Place': Place, 'Review': Review, 'User': User, 'City': City
    }

    def do_quit(self, argument):
        """Quit command"""
        return True

    def do_EOF(self, argument):
        """EOF command"""
        print()
        return True

    def emptyline(self):
        """Empty line command"""
        pass

    def do_create(self, argument):
        """Creates an instance of BaseModel"""
        if not argument:
            print("** class name missing **")
            return
        if argument not in self.classes:
            print("** class doesn't exist **")
            return

        cls = self.classes[argument]
        instance = cls()
        print(instance.id)
        models.storage.save()

    def do_show(self, argument):
        """Shows string representation based on the class name and id"""
        tokens = shlex.split(argument)
        if len(tokens) < 2:
            print("** class name or instance id missing **")
            return
        class_name, instance_id = tokens[0], tokens[1]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        key = "{}.{}".format(class_name, instance_id)
        instance = models.storage.all().get(key)
        if not instance:
            print("** no instance found **")
        else:
            print(instance)

    # other methods go here...

    def precmd(self, line):
        """Executed just before the command line is interpreted"""
        parts = line.split('.', 1)
        if len(parts) == 2:
            _class, rest = parts
            command, rest = rest.split('(', 1)
            _id, other_arguments = rest.split(')', 1)
            line = f"{command} {_class} {_id} {other_arguments}"
        return line


if __name__ == '__main__':
    """Infinite loop"""
    HBNBCommand().cmdloop()

