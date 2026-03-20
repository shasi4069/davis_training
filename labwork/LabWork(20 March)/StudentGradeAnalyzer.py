i = 0  # Initialize counter
while(i < 5): # Loop to get grades for 5 students
    grade = int(input("Enter the grade: "))
    if grade >= 90:
        print("Grade: A")
    elif grade >= 75:
        print("Grade: B")
    elif grade >= 50:
        print("Grade: C")
    else:
        print("Grade: F")
    i += 1  # Increment counter