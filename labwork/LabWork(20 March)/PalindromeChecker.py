def check_palindrome(s):
    # Remove spaces and convert to lowercase
    cleaned = ''.join(s.split()).lower()
    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]

# Take input from user
user_input = input("Enter a string to check if it's a palindrome: ")
if check_palindrome(user_input):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
