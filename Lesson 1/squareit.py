start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

square = []
even = []
odd = []

for num in range(start, end+1):
    sq = num*num
    square.append(sq)
    if sq%2 == 0:
        even.append(sq)
    else:
        odd.append(sq)

print(square)
print(even)
print(odd)