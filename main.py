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

# stores some of the strings
# ideally, should store all the strings (if even better system won't be implemented)
text = {
    'welcome': 'Welcome! This is a rock-paper-scissors game.',
    'rules': 'Rules are simple: paper beats rock; rock beats scissors, scissors beat paper. '
             'The winner is chosen after 5 rounds.',
    'controls': 'Enter the name of an object play a round.',
    'computer': 'Computer',
    'player': 'Player',
    'gwinner_draw': 'WHOA! It\'s a TOTAL draw!',
    'gwinner_player': 'Congratulations! You\'ve WON',
    'gwinner_computer': 'Uh-oh... It\'s not your lucky game. Try again!'
}

# stores valid computer and player choices
text_choice = ['rock', 'paper', 'scissors']


# prints out initial texts on application launch
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

    # spellcheck of cleaned input
    # checks if player_input is one of these: 'rock', 'paper', 'scissors'
    while player_input not in text_choice:
        print('Choose one of the following: rock, paper or scissors!')
        player_input = clean_input()

    # chooses the winner for the round based on input
    # returns score adjustment: 0 for draw; 1 for player win, -1 for computer win
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


# game logic: 5 rounds played,
# then winner is determined based on score
def game():
    score = 0
    for game_round in range(1, 6):
        score += one_round()
    if score > 0:
        print(text['gwinner_player'])
    elif score < 0:
        print(text['gwinner_computer'])
    else:
        print(text['gwinner_draw'])


if __name__ == '__main__':
    welcome()
    game()
