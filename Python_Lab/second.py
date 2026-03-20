def classify_number(num):
    if num > 0:
        print("Positive", end=", ")
    elif num < 0:
        print("Negative", end=", ")
    else:
        print("Zero", end=", ")

    # Nested if for even/odd
    if num != 0:
        if num % 2 == 0:
            print("Even")
        else:
            print("Odd")

numbers = [10, -5, 0, 7, -2]

for n in numbers:
    classify_number(n)
