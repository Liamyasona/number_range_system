def number_inputs():
    # Make a list on each range to store the inputted numbers   
    ranges = [0, 0, 0, 0, 0] 


    # Loop to keep asking the user to input a number
    while True:
        try:
            # Ask user to input numbers ranging from 1 to 50
            number_input = int(input("Please input a number ranging from 1 to 50: "))

            # Conditions on what are considered valid for the user to input
            if 1 <= number_input <= 50:
                # If & elif statements to group the inputted valid numbers within 1 to 50
                if number_input >= 1 and number_input <= 10:
                    ranges[0] += 1 
                elif number_input >= 11 and number_input <= 20:
                    ranges[1] += 1 
                elif number_input >= 21 and number_input <= 30:
                    ranges[2] += 1 
                elif number_input >= 31 and number_input <= 40:
                    ranges[3] += 1 
                elif number_input >= 41 and number_input <= 50:
                    ranges[4] += 1 
            else:
                print("Invalid number! Displaying previous numbers.")
                break # When user inputs a invalid number, the loop breaks and prints the numbers
        
        # If user inputted a invalid integer
        except ValueError:
            print("Invalid integer! Please print a valid integer.")
    
    # If user input is invalid, the loop and the inputted numbers will be printed in their following ranges
    print("")
    print("Here are the inputted numbers on every range:")
    print(f"Numbers 1-10: {ranges[0]}")
    print(f"Numbers 11-20: {ranges[1]}")
    print(f"Numbers 21-30: {ranges[2]}")
    print(f"Numbers 31-40: {ranges[3]}")
    print(f"Numbers 41-50: {ranges[4]}")

# Execute the function
number_inputs()