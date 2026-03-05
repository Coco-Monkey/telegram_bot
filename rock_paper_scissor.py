import random, sys

def _welcome_message():
    print("*" * 20, '\n')
    print("Welcome to Rock, paper & scissors game \n" \
    "You will play against the system. You have these options: \n" \
    "[R] OCK \n" \
    "[P] APER \n" \
    "[S] CISSORS\n" \
    "[Q] UIT")
    print("*" * 20)
_welcome_message()

score = {'wins': 0, 'loses': 0, 'ties':0}

def global_score():
    scores = f"Wins: {score['wins']} loses: {score['loses']} ties: {score['ties']}"
    return scores



def chooses():
    options = ['ROCK', 'PAPER', 'SCISSORS']
    valid_inputs= ['R', 'P', 'S', 'Q']


    while True: 
        computer_choose = random.choice(options)

        print("Type your move:")
        player_input =input(">")
        player_input = player_input.upper() 

        #R OPTIONS
        if player_input == 'R' and computer_choose == 'ROCK':
            print("You choose Rock and computer also chooses Rock... TIE!")
            score['ties'] += 1
            print(global_score())

        elif player_input == 'R' and computer_choose == 'PAPER':
            print("You choose Rock and computer choose Paper... COMPUTER WINS:")
            score['loses'] += 1
            print(global_score())

        elif player_input == 'R' and computer_choose == 'SCISSORS':
            print("You choose Rock and computer choose Scissor... YOU WIN!")
            score['wins'] += 1
            print(global_score())


        #P OPTIONS
        elif player_input == 'P' and computer_choose == 'PAPER':
            print("You choose Paper and computer also choose Paper.... TIE!")
            score['ties'] += 1
            print(global_score())

        elif player_input == 'P' and computer_choose == 'ROCK':
            print("You choose Paper and computer chooses Rock... YOU WIN!")
            score['wins'] += 1
            print(global_score())

        elif player_input == 'P' and computer_choose == 'SCISSORS':
            print('You choose paper and computer chooses Scissors... COMPUTER WINS!')
            score['loses'] += 1
            print(global_score())


        #S OPTIONS
        elif player_input == 'S' and computer_choose == 'SCISSORS':
            print('You choose Scissors and computer also chooses Scissors... TIE!')
            score['ties'] += 1
            print(global_score())

        elif player_input == 'S' and computer_choose == 'PAPER':
            print("You choose Scissors and computer chooses Paper... YOU WIN!")
            score['wins'] += 1
            print(global_score())

        elif player_input == 'S' and computer_choose == 'ROCK':
            print('You choose Scissors and computer chooses Rock, COMPUTER WINS!')
            score['loses'] += 1
            print(global_score())


        elif player_input == 'Q':
            sys.exit()

        if player_input not in valid_inputs:
            print("Not an option, try again")
            continue


        if score['wins'] == 10 or score['loses'] == 10:
            print("Game has ended, final score is: " + global_score())
            sys.exit()
chooses()