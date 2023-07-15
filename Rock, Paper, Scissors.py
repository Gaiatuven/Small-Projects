import random
import sys


class RPS:
    def __init__(self):
        print("Welcome to Rock, Paper, Scissors game!")

        self.moves: dict = {'rock': '🤜', 'paper': 'emoji.emoji.paper', 'scissors': 'emoji.emoji.scissors'}
        self.valid_moves = list(self.moves.keys())

    def play_game(self):
        user_move = input("Rock, paper, Scissors game: ").lower()

        if user_move == 'exit':
            print('Thanks for playing')
            sys.exit()

        if user_move not in self.valid_moves:
            print('Invalid move ....')
            return self.play_game()

        cpu_move = random.choice(self.valid_moves)

        self.display_moves(user_move, cpu_move)
        self.check_move(user_move, cpu_move)

    def display_moves(self, user_move, cpu_move):
        print('--------------------------------')
        print(f'You: {self.moves[user_move]}')
        print()
        print(f'Computer: {self.moves[cpu_move]}')

    def check_move(self, user_move, cpu_move):
        if user_move == cpu_move:
            print('We have a Tie ....')
        elif user_move == 'rock' and cpu_move == 'scissors':
            print('You win !!')
        elif user_move == 'scissors' and cpu_move == 'paper':
            print('You win !!')
        elif user_move == 'paper' and cpu_move == 'rock':
            print('You win !!')
        else:
            print('You lose.')


if __name__ == '__main__':
    rps = RPS()
    while True:
        rps.play_game()