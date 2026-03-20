# Take number of rows
rows = int(input("Enter number of rows: "))

# Outer loop for rows
for i in range(1, rows + 1):
    
    # Check if row is even or odd
    if i % 2 == 0:
        symbol = "*"
    else:
        symbol = "#"
    
    # Inner loop to print symbols
    for j in range(i):
        print(symbol, end=" ")
    
    # Move to next line
    print()