list = [4, 5, 1, 2, 9, 7, 10, 8]
print(list)

count = 0

for i in list:
    count += i
average = count / len(list)
print(count, average)

list.sort()
print(list[0])
print(list[-1])
