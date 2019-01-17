random_keys = {}
random_keys["astring"] = "string"
random_keys[5] = "integer"
random_keys[25.2] = "float"
random_keys[("abc", 123)] = "tuple"

class AnObject:
    def __init__(self, avalue):
        self.avalue = avalue

my_object = AnObject(14)
random_keys[my_object] = "Object"
my_object.avalue = 12
print( random_keys[my_object] )


try:
    random_keys[[1,2,3]] = "Nope"
except:
    print("unable list")

for key, value in random_keys.items():
    print(f"{key} has value {value}")

