first_artists = {
    "Sarah Brightman",
    "Guns N' Roses",
    "Opeth",
    "Vixy and Tony",
}

second_artists = {
    "Nickelback",
    "Guns N' Roses",
    "Savage Garden"
}

print("All: {}".format(
    first_artists.union(second_artists)
))

print("Both: {}".format(
    second_artists.intersection(first_artists)
))

print(
    "Either but not both: {}".format(
        first_artists.symmetric_difference(second_artists)
    )
)

a = {1,2,3,4,5}
b = {1,2,3}
print( a.issubset(b), b.issubset(a))
print(a.issuperset(b), b.issuperset(a))
print(a.difference(b), b.difference(a))




