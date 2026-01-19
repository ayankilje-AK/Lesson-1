tuplex = ("tuple", False, 42, 22.5)
print(tuplex)

tuplex = (1, 12, 3, 65)
print(tuplex)

tuplex = tuplex + (9,)
print(tuplex)

tuplex = (50, 10, 60, 50)
print(tuplex.count(50))

tuplex = (10, 23, 76, 55, 94, 67, 89, 54, 2, 99)
slice = tuplex[3:5]
print(slice)
slice = tuplex[:6]
print(slice)