import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock, Paper, Scissors Game!")
        print("Choose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '4':
            print("Exiting the game. Final Scores:")
            print(f"User: {user_score} - Computer: {computer_score}")
            break

        if choice not in ['1', '2', '3']:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
            continue

        user_choice_map = {'1': 'rock', '2': 'paper', '3': 'scissors'}
        user_choice = user_choice_map[choice]
        computer_choice = get_computer_choice()

        print(f"\nYour choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == "user":
            print("You win!")
            user_score += 1
        elif result == "computer":
            print("Computer wins!")
            computer_score += 1
        else:
            print("It's a tie!")

        print(f"Current Scores - User: {user_score} - Computer: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! Final Scores:")
            print(f"User: {user_score} - Computer: {computer_score}")
            break

if __name__ == "__main__":
    play_game()
