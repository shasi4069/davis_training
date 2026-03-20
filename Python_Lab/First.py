def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"

# Process 5 students
for i in range(5):
    marks = int(input(f"Enter marks of student {i+1}: "))
    
    if 0 <= marks <= 100:
        grade = calculate_grade(marks)
        print("Grade:", grade)
    else:
        print("Invalid marks")
