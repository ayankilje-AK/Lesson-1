def calculate_percentage(obtained_marks, total_marks):
    """

    Calculates the percentage based on obtained marks and total marks.

    Args:
        obtained_marks (float or int) : The marks obtained by the student.
        total_marks (float or int) : The total possible marks for the assessment

    Returns: 
        float: The calculated percentage

    """

    #Formula for Percentage = (obtained_marks / total_marks)*100
    if total_marks <= 0:
        return "Error: Total Marks cannot be zero or negative"
    percentage = (obtained_marks / total_marks) * 100
    return percentage


# Section for user input
try:
    obtained = float(input("Enter the marks obtained: "))
    total = float(input("Enter the total possible marks: "))

    #Calculate and display the percentage
    result_percentage = calculate_percentage(obtained, total)

    if isinstance(result_percentage, str):
        print(result_percentage) #Print error message if total_mark is invalid.
    else:
        print(f"The percentage is: {result_percentage: .2f}%")#Format to two decimal places
        
except ValueError:
    print("Invalid Input. Please enter numerical values for marks.")