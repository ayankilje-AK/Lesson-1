class Parrot:
    species = "Bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age
blue = Parrot("Blue", 16)
woo = Parrot("Red", 23)
print("Blue is a {}".format(blue.species))
print("Red is a {}".format(woo.species))
print("{} is a game {}".format(blue.name, blue.age))
print("{} is a game {}".format(woo.name, woo.age))