def default_argument(x, y, z, a="Hi", b=False):
    print(x, y, z, a, b)


default_argument(1, 2, 3)
default_argument(1, 2, 3, "Hello", True)
default_argument(1, 2, 3, "Hello")
default_argument(1, 2, 3, b=True)
default_argument(1, 2, 3, b=True, a="Hello")
default_argument(y=2, x=1, z=3, b=True, a="Hello")

def kw_only(x, y="defaultkw", *, a, b="only"):
    print(x, y, a, b)

kw_only(1) # error
kw_only(1, a=3)
kw_only(1, a=3, 5) # error
kw_only(1, a=3, b=5)


number = 5
def funky_function(number=number):
    print(number)

funky_function()
funky_function(8)
number=6
funky_function()


def hello(b=[][:]):
    b.append('a')
    print(b)

hello()
hello()


def get_pages(*links):
    for link in links:
        print(link)

get_pages()
get_pages("http://www.archlinus.org")
get_pages("http://www.archlinus.org", "http://ccphillips.net/")