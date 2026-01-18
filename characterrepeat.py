string = str(input("Enter your own string: "))
character = input("Please  enter a character from the sting you entered")

i = 0
count = 0

while(i < len(string)):

    if(string[i] == character):
        count = count + 1
    i = i + 1

print("The total number of times", character, "has occured in", string, "is", count,"times")