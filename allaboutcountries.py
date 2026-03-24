class India():
    def capital(self):
        print("The capital of India is, New Delhi")
    def language(self):
        print("India's ntional language is Hindi")
    def type(self):
        print("india is a developing country")

class USA():
    def capital(self):
        print("The capital of the United States of America is Washington D.C.")
    def language(self):
        print("America's national language is English")
    def type(self):
        print("America is a developed country")

obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()
    