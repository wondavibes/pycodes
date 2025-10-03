import random

def guess_game():
    secret_number = random.randint(1, 10)
    guess_attempts = 0
    while True:
        guess = int(input("Guess the secret number between 1 and 10: "))
        guess_attempts += 1
        match guess:
            case _ if guess < secret_number:
                print("Too low!") 
            case _ if guess > secret_number:
                print("Too high!")
            case _:
                print(f"Congratulations! You got it right and it only took you {guess_attempts} times.")
                break

while True:
    guess_game()
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye.")
        break
           
































"""age = int(input("Enter your age: "))
has_id = input("Do you have a valid ID? (yes/no): ").strip().lower() == "yes"

if age >= 18 and has_id:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")"""
