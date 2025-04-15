import random

# Function to start the game
def guess_the_number():
    print("Welcome to the Guess the Number game!")
    
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    # Set the number of attempts
    attempts = 0
    
    # Start the game loop
    while True:
        try:
            # Ask the user for their guess
            user_guess = int(input("Guess a number between 1 and 100: "))
            
            # Increment the number of attempts
            attempts += 1
            
            # Check if the guess is correct
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break  # Exit the loop if the guess is correct
        except ValueError:
            print("Please enter a valid number.")
            
# Start the game
guess_the_number()
