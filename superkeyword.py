class Bird:

    def _init__(self):
        print("Bird is ready!")

    def whoisthis(self):
        print("Bird")
    
    def swim(self):
        print("Swim faster")

class Penguin(Bird):

    def __init__(self):
        super().__init__()
        print("The Super Penguin is Ready")

    def whoisthis(self):
        print("Penguin")

    def run(self):
        print("Run Faster!")


obj = Penguin()
obj.whoisthis()
obj.swim()
obj.run()    