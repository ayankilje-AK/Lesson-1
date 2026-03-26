class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return self.word+'('+self.meaning+')'
    
flash = []
print("Welcome to the flashcard application")
while (True):
    word = input("Enter the name you would like to add to the flashcard")
    meaning = input("Enter the meaning of the word you would like to add to the flashcards")
    flash.append(flashcard(word, meaning))
    option = int(input("Enter ) if you want to add another flashcard, otherwise enter 1"))
    if (option):
        break

print("Your flashcards")
for i in flash:
    print(">", i)