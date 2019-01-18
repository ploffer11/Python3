class Options:
    default_options = {
        "port": 21,
        "host": "localhost",
        "username": None,
        "password": None,
        "debug": False,
    }

    def __init__(self, **kwargs):
        self.options = dict(Options.default_options)
        self.options.update(kwargs)

    def __getitem__(self, key):
        if not key in self.options:
            raise KeyError("Don't have it!")
        return self.options[key]


options = Options(username="dusty", password="drowssap", debug=True)
options['debug']
options['port']
options['username']
options['?']

def show_args(arg1, arg2, arg3="THREE"):
    print(arg1, arg2, arg3)

some_args = range(3)
more_args = {
    "arg1": "ONE",
    "arg2": "TWO",
}

print("Unpacking a sequence", end=" ")
show_args(*some_args)

print("Unpacking a dict:", end=" ")
show_args(**more_args)

x = {'a': 1, 'b': 2}
y = {'b': 11, 'c': 3}
z = {**x, **y}
z

def my_function():
    print("The Function Was Called")

my_function.description = "A silly function"

def second_function():
    print("The second was called")

second_function.description = "A sillier function"

def another_function(function):
    print(f"""
The description: {function.description}
The name: {function.__name__}
The class: {function.__class__}
Now I'll call the function passed in"""
    )
    function()

another_function(my_function)
another_function(second_function)