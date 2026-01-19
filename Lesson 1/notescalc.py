amount = int(input("Enter the amount of money that you have in total"))

note1 = amount // 100
note2 = (amount%100)//50
note3 = ((amount%100)%50)//10
note4 = (((amount%100)%50)%10)//5

print("Amount of notes that are worth $100", note1)
print("Amount of notes that are worth $50", note2)
print("Amount of notes that are worth $10", note3)
print("Amount of notes that are worth $5", note4)