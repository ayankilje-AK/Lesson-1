class dog:
    animal = "dog"
    def __init__(self, breed, age):
        self.breed = breed
        self.age = age
d1 = dog("German Shepherd", 3)
d2 = dog("Golden Retriever", 2)
print(d1.breed)
print(d1.age)
print(d1.animal)
print(d2.breed)
print(d2.age)
print(d2.animal)
        
