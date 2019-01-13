class EvenOnly(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("Only integers can be added")
        if integer % 2:
            raise ValueError("Only even numbers can be added")
        super().append(integer)

def no_return():
    print("Raise an exception")
    raise Exception("This is always raised")
    print("this line don't run")
    return "GO TO HELL"

def call_exceptor():
    print("call_exceptor starts")
    no_return()
    print("this line don't run")
    
def funny_division(divider):
    try:
        if divider == 13:
            raise ValueError("Do not use 13. 13 is unlucky number!")
        return 100 / divider 
    except ZeroDivisionError:
        return "Enter a number other than zero"
    except TypeError:
        return "Enter a numerical value"
    except ValueError:
        print ("No, No, not 13!")
        raise 




#for value in (10, 5.0, 0, "fuck you, function", 13):
#    print ( funny_division(value) )

try:
    raise ValueError("This is an argument")
except ValueError as e:
    print("The exception arguments were", e.args)
