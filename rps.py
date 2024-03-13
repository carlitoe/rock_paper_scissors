import random


options = ["rock", "paper", "scissors"]

while True:
    my_choice = input("Rock, Paper, or Scissors?: ").lower()  # Convert user input to lowercase
    computer_choice = random.choice(options)
    if my_choice == "quit":
        break 

    print(f"Your choice: {my_choice.capitalize()}")  # Capitalize the user's choice for output
    print(f"Computer's choice: {computer_choice.capitalize()}")

    if my_choice == computer_choice:
        print("It's a tie! Please go again.")
    elif my_choice == "rock" and computer_choice == "scissors":
        print("Rock beats scissors. You win!")
        break
    elif my_choice == "paper" and computer_choice == "rock":
        print("Paper beats rock. You win!")
        break
    elif my_choice == "scissors" and computer_choice == "paper":
        print("Scissors beats paper. You win!")
        break
    else:
        print("You lose! Try again.")

