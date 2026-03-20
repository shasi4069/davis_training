# Salary Bonus Calculator


i = 0 # Initialize counter

# Start loop
while(i < 5):
    salary = int(input("Enter the salary: "))   # Get salary input
    Years = int(input("Enter the years of experience: "))  # Get years of experience

    # Calculate bonus
    if(Years >= 10):
        Bonus = salary * 0.2
        print(f"Bonus: {Bonus}")
    elif(Years >= 5):
        Bonus = salary * 0.1
        print(f"Bonus: {Bonus}")
    else:
        Bonus = salary * 0.05
        print(f"Bonus: {Bonus}")
    i += 1 # Increment counter
