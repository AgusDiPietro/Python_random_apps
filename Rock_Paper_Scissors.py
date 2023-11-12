import random

print('Welcome to the game');

rounds = int(input(' How many rounds would you like to play?: '));

#Variables
moves = ['rock', 'paper', 'scisors'];
p_score = 0
c_score = 0

#Main game loop
for game_round in range(rounds):
    #Print the game screen and get user input
    print(' Round ' + str(game_round + 1))
    print(' Player: ' + str(p_score) + ' Computer: ' + str(c_score))

    #Get the computers move
    c_index = random.randint(0,2)
    c_choise = moves[c_index]

    #Get the players move
    p_choice = input('Time to pick one...rock, papers or scissors: ').lower().strip()

    #If the player makes a valid move
    if p_choice in moves:
        print(' Computer: ' + c_choise)
        print(' Player: ' + p_choice)


    

