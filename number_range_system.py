# Define the ranges
def number_inputs():
    # Make a list on each range to store the inputted numbers   
    ranges = [0 for i in range(5)]

# Loop to keep asking the user to input a number
    while True:
        try:
            # Ask user to input numbers ranging from 1 to 50
            number_input = int(input("Please input a number ranging from 1 to 50: "))

            # Conditions on what are considered valid for the user to input
            if 1 <= number_input <= 50:
                
            else:
                print("Invalid number! Displaying previous numbers.")
                break # When user inputs a invalid number, the loop breaks and prints the numbers
        
        # If user inputted a invalid integer
        except ValueError:
            print("Invalid integer! Please print a valid integer.")


# Ask the user to input again
# If user input is invalid, print the inputted numbers in their following ranges