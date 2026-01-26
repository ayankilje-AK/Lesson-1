import array as arr

#create an array
array_num = arr.array("i", [1, 3, 5, 3, 7, 9, 3])
print("Original Array: ", (array_num))

print("Amount of times number 3 is repeated: ", (array_num.count(3)))

array_num.reverse()
print("The reversed form of the array: \n", (array_num))