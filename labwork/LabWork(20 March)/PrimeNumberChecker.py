# Function to check if a number is prime
def is_prime(n):
    # Prime numbers are greater than 1
    if n <= 1:
        return False
    
    # Use a for loop to check divisibility
    for i in range(2, n):
        # If n is divisible by any number between 2 and n-1
        if n % i == 0:
            return False  # Not a prime number
    
    # If no divisors were found
    return True


# Take input from user
num = int(input("Enter a number: "))

# Use if-else to display result
if is_prime(num):
    print("It is a prime number")
else:
    print("It is not a prime number")