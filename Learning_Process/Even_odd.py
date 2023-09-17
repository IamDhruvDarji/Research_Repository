# Get user input for a number
# Prompt the user to enter a number and convert it to an integer
number = int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:  # Use the modulo operator to check if the remainder is 0 when dividing by 2
    # If the remainder is 0, it's even; print the result
    print(f"{number} is an even number.")
else:
    # If the remainder is not 0, it's odd; print the result
    print(f"{number} is an odd number.")
