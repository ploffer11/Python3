import re

regex_example =[
    ("hello worl", "hello world"),
    ("ello world", "hello world"),
    ("^hello world$", "hello world"),
    ("^hello world$", "hello worl"),
    ("hel.o world", "hello world"),
    ("hel.o world", "helpo world"),
    ("hel.o world", "hel o world"),
    ("hel.o world", "helo world"),
    ("hel[lp]o world", "hello world"),
    ("hel[lp]o world", "helpo world"),
    ("hel[lp]o world", "helPo world"),
    ("hello [a-z] world", "hello   world"),
    ("hello [a-z] world", "hello b world"),
    ("hello [a-z] world", "hello B world"),
    ("hello [a-zA-Z] world", "hello B world"),
    ("hello [a-zA-Z0-9] world", "hello 2 world"),
    ("0\.[0-9][0-9]", "0.05"),
    ("0\.[0-9][0-9]", "005"),
    ("0\.[0-9][0-9]", "0,05"),
    ("\(abc\]", "(abc]"),
    ("\s\d\w", "\t5n"),
    ("\s\d\w", "5n"),
    ("hel*o", "hello"),
    ("hel*o", "heo"),
    ("hel*o", "helllllo"),
    ("hel*o", "heko"),
    ("[A-Z][a-z]* [a-z]*\.", "A string."),
    ("[A-Z][a-z]* [a-z]*\.", "No ."),
    ("[a-z]*.*", ""),
    ("\d+\.\d+", "0.4"),
    ("\d+\.\d+", "1.0002"),
    ("\d+\.\d+", "1."),
    ("\d?\d%", "1%"),
    ("\d?\d%", "99%"),
    ("\d?\d%", "999%"),
    ("abc{3}", "abccc"),
    ("(abc){3}", "abccc"),
    ("(abc){3}", "abcabcabc"),
    ("[A-Z][a-z]*( [a-z]+)*\.$", "Eat."),
    ("[A-Z][a-z]*( [a-z]+)*\.$", "Eat more good food."),
    ("[A-Z][a-z]*( [a-z]+)*\.$", "A good meal."),

]

# * 0개 이상
# + 1개 이상
# ? 0개 or 1개 

class Regex:
    def __init__(self, pattern, search_string):
        self.search_string, self.pattern = (
            search_string, pattern
        )

    def match(self):
        match = re.match(self.pattern, self.search_string)
        if match:
            template = "'{}' matches pattern '{}'"
        else:
            template = "'{}' doesn't match pattern '{}'"
        
        print (template.format(
            self.search_string, self.pattern
        ))

    def group(self):
        match = re.match(self.pattern, self.search_string)
        if match:
            domain = match.groups()
            print(domain)

for pattern, search_string in regex_example:
    regex = Regex(pattern, search_string)
    regex.match()


regex = Regex(
    "^[a-zA-Z.]+@([a-z.]*\.[a-z]+)$", "some.user@example.com"
)

regex.group()
