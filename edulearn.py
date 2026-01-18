print("Welcome to EduLearn")
print("EduLearn is an online learning platform that helps students that study in grades strarting from grade 1 going all the way to grade 12.")
print("In EduLearn, you can have access to high quality study. You will be able to find past examination for different major examinations, past papers and answers for Mathematics Olympiads such as the American Mathematics Olympiad (AMO), and many more. You will be able to acces IB and Cambridge board curriculum and will be able to study them, for free!")
print("To begin, kindly enter your name")
name = str(input("Kindly enter your name: "))
print("Welcome to EduLearn", name)

print("Kindly enter your board curriculum")
print("1. Cambridge Board")
print("2. IB Board")
choice : input("Kindly enter your board curriculum.1/2 ") # type: ignore
if choice == ("1"):
    print("You have chosen the Cambridge Board Curriculum")
    print("Kindly enter the grade you would like to study")
    print("a. Grade 1")
    print("b. Grade 2")
    print("c. Grade 3")
    print("d. Grade 4")
    print("e. Grade 5")
    print("f. Grade 6")
    print("g. Grade 7")
    print("h. Grade 8")
    print("i. Grade 9")
    print("j. Grade 10")
    print("k. Grade 11")
    print("l. Grade 12")
    choice1 : input("Kindly enter the grade you would like to study on. a/b/c/d/e/f//g/h/u/j/k/l") # type: ignore
    if choice1 == ("a") or ("a."):
        print("You have chosen Grade 1")
        print("What would you like to do today")
        print("1. Practise Quizzes")
        print("2. Learn")
        print("3. Answer Questions")
        choice2 : input("Enter what you would like to do today. 1/2/3") # type: ignore
        if choice2 == ("1") or ("1."):
            print("You have chosen to do practise quizzes")
            print("What subject practise quiz would you like to do")
            print("a. Mathematics")
            print("b. English")
            print("c. Science")
            print("d. Geography")
            print("e. History")
            print("f. Music")
            print("g. Computing")
            print("h. Art and Design")
            print("i. French")
            print("j. Spanish")
            choice3 : input("Kindly enter what subject test you would like to take. a/b/c/d/e/f/g/h/i/j") # type: ignore
            if choice3 == ("a") or ("a."):
                print("You have chosen to take the Year 1 Mathematics Practise Quizz which will be about all the subjects that will take place throughout the academic year. Lets Begin!")
                print("Question Number 1")



