import traceback

metaslash = 1


def printNames(*args):
    neal = 'neal'
    michele = 'michele'  # Corrected the variable name from 'michelle' to 'michele'
    eric = 5
    print("Local values:", neal, michele, eric)


class Nothing:
    def printValue(self, value):  # Added 'self' parameter to the method
        print(value)

    def __init__(self, value):  # Added __init__ method to initialize the 'value' attribute
        self.value = value

    def set(self, value):
        self.value = value


def tryToDoSomething(value):  # Removed 'self' parameter
    try:
        import string
        if not value:
            raise RuntimeError("Hey, there's no value")  # Fixed raising exception
        printNames('a', 'b', 'c')  # Corrected passing arguments to printNames function
    except:
        traceback.print_exc()


def setGlobal(value=None):
    global metaslash  # Added 'global' keyword to modify the global variable
    metaslash = value
    print('Old MetaSlash value is:', metaslash)
    useless = Nothing(5)  # Corrected the class instantiation
    print('a useless value is:', useless.value)  # Corrected attribute access


setGlobal(50)
