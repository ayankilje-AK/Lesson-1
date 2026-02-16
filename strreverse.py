class strreverse:
    def __init__(self, word):
        self.word = word
    def reverse_words(self):
        a = self.word.split()
        rev_word = a[::-1]
        result = " ".join(rev_word)
        return result

word = input("Please enter a sentence: ")
obj1 = strreverse(word)
print(obj1.reverse_words())