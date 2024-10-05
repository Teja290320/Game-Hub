import random

# Function for Number Guessing Game
def number_guessing_game():
    # Improved welcome message with a clear introduction
    def display_welcome_message():
        print("=" * 50)  # Decorative line
        print("🎉 WELCOME TO THE NUMBER GUESSING GAME! 🎉")
        print("=" * 50)
        print("In this game, I will pick a number, and you have to guess it!")
        print("Can you figure out what it is? Let's find out!")
        print("You will have a limited number of attempts based on the difficulty level you choose.")
        print("Good luck and have fun! 😊")
        print("=" * 50)

    # Display welcome message
    display_welcome_message()

    # Ask for player's name
    name = input("What's your name, brave player? ")

    # Set default values for the difficulty level
    max_number = 9
    max_attempts = 6

    # Let the player choose a difficulty level
    print("\nChoose a difficulty level:")
    print("1. Easy (Number between 0 and 9, 6 attempts)")
    print("2. Medium (Number between 0 and 20, 5 attempts)")
    print("3. Hard (Number between 0 and 50, 4 attempts)")

    while True:
        level = input("Enter the difficulty level (1/2/3): ")
        if level == "1":
            max_number = 9
            max_attempts = 6
            break
        elif level == "2":
            max_number = 20
            max_attempts = 5
            break
        elif level == "3":
            max_number = 50
            max_attempts = 4
            break
        else:
            print("Invalid choice! Please choose 1, 2, or 3.")

    # Generate a random number within the selected range
    secret_number = random.randint(0, max_number)

    print(f"\nI have chosen a number between 0 and {max_number}. Can you guess it?")

    # Loop through the allowed number of attempts (starting from 0)
    for attempt in range(max_attempts):
        try:
            guess = int(input(f"Attempt {attempt + 1}/{max_attempts} - Guess the number: "))  # Adjusted for display
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        if guess == secret_number:
            print(f"🎊 Congratulations {name}! You guessed the number in {attempt + 1} attempt(s)! 🎊")  # Adjusted for display
            break
        elif guess > secret_number:
            print("📉 Too high! Try again.")
        else:
            print("📈 Too low! Try again.")
    else:
        # If user runs out of attempts
        print(f"😢 Sorry {name}, you've used all {max_attempts} attempts. The correct number was {secret_number}.")

    # Ask if the player wants to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        number_guessing_game()
    else:
        print(f"\nThanks for playing, {name}! Goodbye! 👋")

# Function for Rock, Paper, Scissors
def rock_paper_scissors():
    def display_welcome_message():
        print("=" * 50)  # Decorative line
        print("🎉 WELCOME TO ROCK, PAPER, SCISSORS! 🎉")
        print("=" * 50)
        print("In this game, you will play against the computer.")
        print("Choose either rock, paper, or scissors.")
        print("Let's see if you can outsmart the computer!")
        print("Good luck! 😊")
        print("=" * 50)

    def play_rps():
        display_welcome_message()
        
        choices = ["rock", "paper", "scissors"]
        while True:
            computer_choice = random.choice(choices)

            player_choice = input("Choose rock, paper, or scissors: ").lower()
            if player_choice not in choices:
                print("❌ Invalid choice! Please choose rock, paper, or scissors.")
                continue  # Loop until valid input
            break  # Break out of loop if valid input

        print(f"Computer chose: {computer_choice}")
        
        if player_choice == computer_choice:
            print("🤝 It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
            (player_choice == "paper" and computer_choice == "rock") or \
            (player_choice == "scissors" and computer_choice == "paper"):
            print("🎉 You win!")
        else:
            print("😢 You lose!")

    play_rps()

# Function for Dice Roller
def dice_roller():
    def roll_dice():
        return random.randint(1, 6)

    def play_dice_roller():
        print("🎲🎲 Welcome to the Dice Roller Game! 🎲🎲")
        print("-" * 40)

        while True:
            roll = input("🔄 Would you like to roll the dice? (yes/no): ").lower()

            if roll == "yes":
                print("\nRolling the dice...")
                print("🎯 You rolled: 🎲", roll_dice())
                print("-" * 40)  # Divider for better readability
            elif roll == "no":
                print("\n👋 Thanks for playing! Goodbye!")
                print("-" * 40)
                break
            else:
                print("\n❗ Please type 'yes' or 'no'.")
                print("-" * 40)

    play_dice_roller()

# Function for Coin Toss
def coin_toss():
    def toss_coin():
        return random.choice(["heads", "tails"])

    def play_coin_toss():
        print("🪙🪙 Welcome to the Coin Toss Game! 🪙🪙")
        print("-" * 40)

        while True:
            guess = input("What's your guess? (heads/tails): ").lower()
            if guess not in ["heads", "tails"]:
                print("❌ Invalid choice! Please type 'heads' or 'tails'.")
                continue

            result = toss_coin()
            print(f"\nCoin is tossed... It's {result}!")

            if guess == result:
                print("🎉 You guessed it right!")
            else:
                print("😢 Better luck next time!")

            play_again = input("\nDo you want to toss the coin again? (yes/no): ").lower()
            if play_again != "yes":
                print("👋 Thanks for playing Coin Toss!")
                break

    play_coin_toss()

# Main menu function to select a game
def main_menu():
    while True:
        print("\n🎮 Welcome to the Game Hub! 🎮")
        print("Choose a game to play:")
        print("1. Number Guessing Game")
        print("2. Rock, Paper, Scissors")
        print("3. Dice Roller")
        print("4. Coin Toss")
        print("5. Exit")

        choice = input("Enter the number of the game you want to play (1/2/3/4/5): ")

        if choice == "1":
            number_guessing_game()
        elif choice == "2":
            rock_paper_scissors()
        elif choice == "3":
            dice_roller()
        elif choice == "4":
            coin_toss()
        elif choice == "5":
            print("👋 Goodbye! Thanks for playing!")
            break
        else:
            print("❌ Invalid choice! Please enter 1, 2, 3, 4, or 5.")

# Start the main menu
main_menu()
