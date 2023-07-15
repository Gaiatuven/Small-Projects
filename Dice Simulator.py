import random


def roll_dice(amount):
    highest_roll = 0
    """
    Rolls a number of dice
    :param amount: The number of dice to roll
    :return: A list of the dice rolls
    """
    rolls = []
    for i in range(amount):
        random_roll = random.randint(1, 6)
        rolls.append(random_roll)
        if random_roll > highest_roll:
            highest_roll = random_roll
    return rolls


def main():
    total_amount = 0
    while True:
        try:
            user_input = input("How many dice rolls would you like: ").lower()

            if user_input == "quit":
                print("Goodbye!")
                print(f"You rolled {total_amount}!")
                break

            print(*roll_dice(int(user_input)), sep=", ")
            total_amount += int(user_input)
        except ValueError:
            print("Please enter a number!")


if __name__ == '__main__':
    main()
