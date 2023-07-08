# should probably greet user and explain rules
# should accept input from the user (think about input!)
# should generate random?? response
# should match input and response
# should generate output string
# match is 5 rolls
# winner is the one with most wins out of 5
# there can be draws

import random
from enum import Enum


class Winner(Enum):
    player = 1
    computer = -1
    draw = 0

text_winners = {
    Winner.draw: 'DRAW',
    Winner.computer: 'Computer won',
    Winner.player: 'Player won'
}

text = {
    'welcome': 'Welcome! This is a rock-paper-scissors game.',
    'rules': 'Rules are simple: paper beats rock; rock beats scissors, scissors beat paper. The winner is chosen after 5 rounds.',
    'controls': 'Enter the name of an object play a round.',
    'computer': 'Computer',
    'player': 'Player'
}

text_choice = ['rock', 'paper', 'scissors']

def welcome():
    print(text['welcome'])
    print(text['controls'])
    print(text['rules'])


# rolls computer turn
def computer_choice():
    return random.choice(text_choice)


# clears player input from some shit and lower cases it
def clean_input():
    player_input = input('Type in your choice for this round: ')
    player_input.strip(' ,.')
    return player_input.casefold()


# shows status message at the end of the round
# and returns value for score
def round_end(player, computer, winner):
    print(f'{player} VS {computer}. {text_winners[winner]}!')
    return winner.value


def one_round():
    player_input = clean_input()
    computer_input = computer_choice()
    while player_input not in text_choice:
        # tell player they suck at typing
        player_input = clean_input()
    if player_input == computer_input:
        print(f'{player_input} VS {computer_input}. DRAW!')
        return 0
    elif player_input == 'rock':
        if computer_input == 'paper':
            return round_end(player_input, computer_input, Winner.computer)
        else:
            return round_end(player_input, computer_input, Winner.player)
    elif player_input == 'paper':
        if computer_input == 'scissors':
            return round_end(player_input, computer_input, Winner.computer)
        else:
            return round_end(player_input, computer_input, Winner.player)
    elif player_input == 'scissors':
        if computer_input == 'rock':
            return round_end(player_input, computer_input, Winner.computer)
        else:
            return round_end(player_input, computer_input, Winner.player)
    else:



def game():
    score = 0
    for game_round in range(1, 6):
        score += one_round()
    if score > 0:
        print('Congratulations! You\'ve WON')
    elif score < 0:
        print('Uh-oh... It\'s not your lucky game. Try again!')
    else:
        print('WHOA! It\'s a TOTAL draw!')


if __name__ == '__main__':
    welcome()
    game()
