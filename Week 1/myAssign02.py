# Import random and randint modules
import random
from random import randint

# Print Welcome Message
print("Welcome to the number guessing game!")

# Get Random Seed
seed_value = input("Enter random seed: ")

# Save the previous value
random.seed(seed_value)

# Accept user input and call guess_number function
def call_guess_number():
    # Generate random numbers between 1 and 100
    random_number = randint(1, 100)
    
    # Add new lines
    print("")
    
    # Call guess_number function
    guess_number("Please enter a guess: ", random_number)
    
    
# guess_number function
def guess_number(guess, random_number):
    # Set number of attempts
    attempts = 0
    
    # Loop to iterate and compare user guesses and attempts
    while (attempts != random_number):
        # Get user guess
        guess_input = int(input(guess))
        
        # Increment the attempt count
        attempts += 1
        
        # Check user gues and print attempt status 
        if (guess_input > random_number):
            print("Lower\n")
        elif (guess_input < random_number):
            print("Higher\n")
        else:
            print('Congratulations. You guessed it!\nIt took you %d guesses.\n' % attempts)
            play_again(guess_input, random_number)

def play_again(number, random_number):
    if (number == random_number):
        if (input("Would you like to play again (yes/no)? ").lower() == "yes"):
            call_guess_number()
        else:
            print("Thank you. Goodbye.")
            exit()


call_guess_number()
    
    
    
