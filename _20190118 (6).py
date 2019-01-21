input_strings = ['1', '5', '28', '131', '3']
output_integers1 =[
    int(num) for num in input_strings
]
output_integers2 = [
    int(num) for num in input_strings if int(num) < 50
]

from collections import namedtuple

Book = namedtuple("Book", "author title genre")
books = [
    Book("Pratchett", "Nightwatch", "fantasy"),
    Book("Pratchett", "Thief Of Time", "fantasy"),
    Book("Le Guin", "The Dispossessed", "scifi"),
    Book("Le Guin", "A Wizard Of Earthsea", "fantasy"),
    Book("Turner", "The Thief", "fantasy"),
    Book("Phillips", "Preston Diamond", "western"),
    Book("Phillips", "Twice Upon A Time", "scifi"), 
]

fantasy_authors = {
    i.author for i in books if i.genre == "fantasy"
}



