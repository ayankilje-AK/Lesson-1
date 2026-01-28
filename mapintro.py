# add two lists using map and lambda
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))


lists1 = [1, 3, 4, 5]
def sq(n):
    return n*n

result = list(map(sq, lists1))
print(result)