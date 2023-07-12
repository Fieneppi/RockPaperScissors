import random
from enum import Enum


class Winner(Enum):
    player = 1
    computer = -1
    draw = 0


TEXT_WINNERS = {
    Winner.draw: 'DRAW',
    Winner.computer: 'Computer won',
    Winner.player: 'Player won'
}


class UiText(Enum):
    welcome = 0
    rules = 1
    controls = 2
    computer = 3
    player = 4
    warning_input = 5
    game_winner_draw = 6
    game_winner_computer = 7
    game_winner_player = 8
    input_request = 9


TEXT_UI = {
    UiText.welcome: 'Welcome! This is a rock-paper-scissors game.',
    UiText.rules: 'Rules are simple: paper beats rock; rock beats scissors, scissors beat paper. '
                  'The winner is chosen after 5 rounds.',
    UiText.controls: 'Enter the name of an object play a round.',
    UiText.computer: 'Computer',
    UiText.player: 'Player',
    UiText.warning_input: 'Choose one of the following: rock, paper or scissors!',
    UiText.game_winner_draw: 'WHOA! It\'s a TOTAL draw!',
    UiText.game_winner_player: 'Congratulations! You\'ve WON',
    UiText.game_winner_computer: 'Uh-oh... It\'s not your lucky game. Try again!',
    UiText.input_request: 'Type in your choice for this round: ',
}


# stores valid computer and player choices
text_choice = ['rock', 'paper', 'scissors']


# prints out initial texts on application launch
def welcome():
    print(TEXT_UI[UiText.welcome])
    print(TEXT_UI[UiText.rules])
    print(TEXT_UI[UiText.controls])


# rolls computer turn
def computer_choice():
    computer_roll = random.choice(text_choice)
    return computer_roll


# clears player input from some shit and lower cases it
def clean_input():
    player_input = input(TEXT_UI[UiText.input_request])
    player_input.strip(' ,.')
    return player_input.casefold()


# shows status message at the end of the round
# and returns value for score
def round_end(player, computer, winner):
    print(f'{player} VS {computer}. {TEXT_WINNERS[winner]}!')
    return winner.value


def one_round():
    player_input = clean_input()
    computer_input = computer_choice()

    # spellcheck of cleaned input
    # checks if player_input is one of these: 'rock', 'paper', 'scissors'
    while player_input not in text_choice:
        print(TEXT_UI[UiText.warning_input])
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
        print(TEXT_UI[UiText.game_winner_player])
    elif score < 0:
        print(TEXT_UI[UiText.game_winner_computer])
    else:
        print(TEXT_UI[UiText.game_winner_draw])


if __name__ == '__main__':
    welcome()
    game()
