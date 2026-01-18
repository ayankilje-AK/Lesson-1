sub1 = int(input("Enter your score for the first subject test out of 100"))
sub2 = int(input("Enter your score for your second subject out of 100"))
sub3 = int(input("Enter your score for your third subject out of 100"))
sub4 = int(input("Enter your score for your fouth subject out of 100"))
sub5 = int(input("Enter your score for your fourth subject out of 100"))

sum = (sub1 + sub2 + sub3 + sub4 + sub5)
print("The sum of all your scores is :  ", sum)

percentage = (sum/500)*100
print("The percentages of all your scores for every subject combined is = ", percentage)