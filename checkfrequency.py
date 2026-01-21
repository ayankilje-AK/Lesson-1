original_dict = {'Codingal': 2, 'is': 2, 'Best' : 2, 'For' : 2, 'Coding' : 1}
print("The original dictionary is" + str(original_dict))

k = 2
result = 0

for key in original_dict:
    if original_dict[key]==k:
        result += 1
print("The result is" +  str(result))