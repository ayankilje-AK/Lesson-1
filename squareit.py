start = int(input("Enter the start number: "))
end = int(input("Enter the ending number: "))

square_list = []
even = []
odd = []

for i in range(start, end + 1):
    square = i*i
    square_list.append(square)

    if square % 2 == 0:
        even.append(square)
    else:
        odd.append(square)


print(square_list)
print(even)
print(odd)