import random
import time

def RPS():
    # Welcome message and instructions for the user
    print('Welcome to Rock-Paper-Scissors!')
    print('Choose the number of num_rounds:')
    print("Enter '1' for single round, '3' for best out of 3, '-1' for endless, or any other positive number for custom num_rounds.")
    
    # User input for the number of num_rounds
    num_rounds = int(input("num_num_rounds: "))
    
    # Initialize scores for the computer and the user
    comp_score, user_score = 0, 0
    # Variable to keep track of total num_rounds played
    total_rounds_played = 0
    # Variable to track if end game prompt has been shown
    end_game_prompted = False
    
    # Main game loop
    while True:
        # Displaying countdown for computer's choice
        for item in ['ROCK', 'PAPER', 'SCISSOR', 'SHOOT...']: 
            print(item,end=' '); 
            time.sleep(0.46)
        
        # Computer randomly chooses Rock, Paper, or Scissors
        comp_choice = random.choice(['✊','🤚','✌'])
        print('\n',comp_choice)
        
        # Asking the user who won the round
        win = input("Who won? (comp 'c', user 'u', tie 't'): ").strip().lower()
        
        # Input validation
        while win not in ['c', 'u', 't']:
            print("Invalid input! Please enter 'c' for computer, 'u' for user, or 't' for tie.")
            win = input("Who won? (comp 'c', user 'u', tie 't'): ").strip().lower()
        
        # Updating scores based on user input
        if win == 'c':
            comp_score += 1
        elif win == 'u':
            user_score += 1
        
        # Increment total num_rounds played
        total_rounds_played += 1

        # ask user if they want to end the game when the specified number of num_rounds are completed
        if num_rounds != -1 and total_rounds_played == num_rounds and not end_game_prompted:
            end_game = input("\nAll num_rounds are completed. Do you want to end the game? (y/n): ").strip().lower()
            if end_game == 'y':
                break
            else:
                # Ask user to input more num_rounds if they want to continue
                additional_rounds = int(input("Enter additional num_rounds: "))
                num_rounds += additional_rounds
                # Set the flag to True to prevent further prompting
                end_game_prompted = True

        # End the game after every 10 num_rounds in endless mode
        elif num_rounds == -1 and total_rounds_played == 10:
            end_game = input("\nDo you wish to continue playing?(y/n): ").strip().lower()
            if end_game == 'y':
                total_rounds_played = 0
            else:
                break
        
        # End the game if the user has added additional num_rounds and these additional num_rounds have been completed
        if num_rounds != -1  and end_game_prompted and total_rounds_played == num_rounds:
            break

    # Printing final scores
    print("\nFinal Scores:")
    print("-"*13)
    print("Computer:", comp_score)
    print("User:", user_score)
    
    # Determining and printing the winner of the game
    if comp_score == user_score:
        print("It's a tie!")
    elif comp_score > user_score:
        print("Computer wins the game!")
    else:
        print("You won the game!")

# Calling the main function to start the game
RPS()
