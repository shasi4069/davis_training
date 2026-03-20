# Number Classification System

list = [50, 43, 55, -10, 3, 78, -54, 0, 12, -3, 99] # List of numbers to classify

for num in list: # Iterate through each number in the list

    # Check if the number is positive
    if num > 0: 
        print(num, "is a positive number.")

        # Check if the number is even or odd
        if(num % 2 == 0):
            print(num, "is an even number.")
        else:
            print(num, "is an odd number.")

    # Check if the number is negative
    elif num < 0:
        print(num, "is a negative number.")
    else:
        print(num, "is zero.")
