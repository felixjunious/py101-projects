import random

def number_guessing_game():
    answer = random.randint(1, 100)

    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100.")

    difficulty = input("Choose difficulty. Type 'easy' or 'hard': ").lower()
    attempts = 10 if difficulty == 'easy' else 5

    while attempts > 0:
        print(f"\nYou have {attempts} attempts remaining to guess the number.")
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if guess == answer:
            print(f"You got it! The answer is {answer}.")
            break
        elif guess > answer:
            print("Too high.")
        else:
            print("Too low.")

        attempts -= 1

        if attempts > 0:
            print("Guess again.")
        else:
            print(f"You've run out of guesses. The answer was {answer}.")

if __name__ == '__main__':
    number_guessing_game()