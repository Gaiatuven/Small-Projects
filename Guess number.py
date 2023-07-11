import random

max_tries = random.randint(1, 10)
low_number, high_number = 1, 70
secret_number = random.randint(low_number, high_number)

print("----- Welcome to Guess the Number! ------")
print(f"---- Guess the number between {low_number} and {high_number} ----")
print("Fun Fact: Each time the game is played, \nthe maximum tries will differ from the previous \n\t\t\t\tgame.")

print(secret_number)
print()

while True:
    user_guess = int(input("Enter your guess: "))
    if user_guess == secret_number:
        print(f"Congrats! You guessed the number {secret_number}, was successfully guessed")
        break
    elif user_guess < secret_number:
        print("Your guess is too low")
        max_tries -= 1
    else:
        print("Your guess is too high")
        max_tries -= 1

    if max_tries == 0:
        print(f"You ran out of tries, the number was {secret_number}")
        break
print("Thanks for playing along")