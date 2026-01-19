rowSize = int(input("Enter the number of rows: "))
if rowSize %2 == 0:
    halfDiamrow = int(rowSize/2)

else:
    halfDiamrow = int(rowSize/2) + 1
space = halfDiamrow - 1

for i in range(1, halfDiamrow + 1):
    for j in range(1, space + 1):
        print(end= " ")
    space = space - 1
    num = 1
    for j in range(2*i - 1):
        print(end= str(num))

        num = num + 1
    print()
space = 1

for i in range(1, halfDiamrow):
    for j in range(1 , space+1):
        print(end=" ")
    space += 1
    num = 1
    for j in range(1, 2*(halfDiamrow - i)):
        print(end= str(num))

        num += 1
    print()

