my_set = {1, 2, 3}
print(my_set)

# mixed data types
mixed_set = {1.0, "Hello", (1, 2, 3)}
print(mixed_set)

# duplicated items in set
duplicate_set = {1, 2, 3, 3, 4, 5, 5, 5}
print(duplicate_set)

# making a set from a list
listed_set = set([1, 2, 3, 2])
print(listed_set)

#removing a. number from a set
removal_set = set([0, 1, 2, 3, 4, 5])
print("The original set: \n",removal_set)
removal_set.pop()
print(removal_set)