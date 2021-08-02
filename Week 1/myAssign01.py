# Import random and randint modules
import random
from random import randint

# Print Welcome Message
print("Welcome to the number guessing game!")

# Get Random Seed
seed_value = input("Enter random seed: ")

# Save the previous value
random.seed(seed_value)

# Set number of attempts
attempts = 0

# Generate Random numbers between 1 and 100
num = randint(1, 100)

# Add new lines
print("")

# Loop to iterate and compare user guesses and attempts
while (attempts != num):
    # Get User's Guess
    guess = int(input("Please enter a guess: "))

    # Increment the attempt count
    attempts += 1

    # Check user gues and print attempt status 
    if (guess > num):
        print("Lower\n")
    elif (guess < num):
        print("Higher\n")
    else:        
        print('Congratulations. You guessed it!\nIt took you %d guesses.\n' % attempts)
        try_again = input("Would you like to play again (yes/no)? ")
        lowerValue = try_again.lower()
        if (lowerValue == "yes"):
            attempts = 0
            num = randint(1, 100)
            # Add new line
            print("")
        else:
            print("Thank you. Goodbye.")
            break
