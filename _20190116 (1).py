class Document:
    def __init__(self):
        self.characters, self.cursor, self.filename = (
            [], Cursor(self), ""
        )
    
    def insert(self, character):
        if not hasattr(character, 'character'):
            character = Character(character)
        self.characters.insert(
            self.cursor.position, character)
        self.cursor.forward()
    
    def delete(self):
        del self.characters[self.cursor.position]
    
    def save(self):
        with open(self.filename, "w") as f:
            f.write("".join(self.characters))

    @property
    def string(self):
        return "".join((str(c) for c in self.characters))
    
    
class Cursor:
    def __init__(self, document):
        self.document, self.position = (
            document, 0
        )

    def forward(self):
        self.position += 1

    def back(self):
        self.position -= 1

    def home(self):
        while self.document.characters[
                self.position - 1].character != "\n":
            self.position -= 1
            if self.position == 0:
                break 
    
    def end(self):
        cond1, cond2 = (
            self.position < len(self.document.characters),
            self.document.characters[self.position].character != "\n" 
        )
        while cond1 and cond2: 
            self.position += 1

class Character:
    def __init__(
        self, character, bold=False, italic=False, underline=False
        ):
        assert len(character) == 1
        self.character, self.bold, self.italic, self.underline = (
            character, bold, italic, underline
        )
    
    def __str__(self):
        bold, italic, underline = (
            "*" if self.bold else "", 
            "/" if self.italic else "",
            "_" if self.underline else ""
        )
        return bold + italic + underline + self.character

doc = Document()
doc.insert("h")
doc.insert("e")
doc.insert(Character("l", bold = True))
doc.insert(Character("l", bold = True))
doc.insert("o")
doc.insert("\n")
doc.insert(Character("w", italic = True))
doc.insert(Character("o", italic = True))
doc.insert(Character("r", underline = True))
doc.insert("l")
doc.insert("d")
print(doc.string)
doc.cursor.home()
doc.delete()
doc.insert("W")
print(doc.string)
doc.characters[0].underline = True
print(doc.string)