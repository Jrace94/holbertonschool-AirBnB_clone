#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
<<<<<<< HEAD


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
=======

class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.
    Attributes:
    prompt (str): The command prompt.
>>>>>>> fc1994a8daf8dfda5c334b2a7ebd0094926de31e
    """

    prompt = "(hbnb) "
    __classes = {
<<<<<<< HEAD
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }
=======
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
            }
>>>>>>> fc1994a8daf8dfda5c334b2a7ebd0094926de31e

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
<<<<<<< HEAD
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
=======

        argdict = {
                "all": self.do_all,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "count": self.do_count,
                "update": self.do_update
                }
>>>>>>> fc1994a8daf8dfda5c334b2a7ebd0094926de31e
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
<<<<<<< HEAD
        print("*** Unknown syntax: {}".format(arg))
        return False
=======
                print("*** Unknown syntax: {}".format(arg))
                return False
>>>>>>> fc1994a8daf8dfda5c334b2a7ebd0094926de31e

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
