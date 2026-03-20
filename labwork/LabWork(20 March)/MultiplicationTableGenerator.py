# Function to generate multiplication table
def table(num):

    # Check for negative numbers
    if(num < 0):
        print("Negative numbers are not allowed.")
        return

    # Generate multiplication table
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

# Take input from user
num = int(input("Enter a number: "))
table(num)