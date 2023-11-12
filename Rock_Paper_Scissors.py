import random

print('Welcome to the game');

rounds = int(input(' How many rounds would you like to play?: '));

#Variables
moves = ['rock', 'paper', 'scissors'];
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

        #Computer chooses rock
        if p_choice == 'rock' and c_choise == 'rock':
            winner = 'tie'
            phrase = ' It is a tie, again!'
        elif p_choice == 'paper' and c_choise =='rock':
            winner = 'Player'
            phrase = 'Paper covers rock!'
        elif p_choice == 'scissors' and c_choise =='rock':
            winner = 'Computer'
            phrase = 'Rock smashes scissors!'

        #Computer chooses paper
        elif p_choice == 'rock' and c_choise == 'paper':
            winner = 'Computer'
            phrase = 'Paper covers rock!'
        elif p_choice == 'paper' and c_choise =='paper':
            winner = 'tie'
            phrase = ' It is a tie, again!'
        elif p_choice == 'scissors' and c_choise =='paper':
            winner = 'Player'
            phrase = 'Scissors cut paper'    
        
        #Computer choose scissors
        elif p_choice == 'rock' and c_choise == 'scissors':
            winner = 'Player'
            phrase = 'Rock smashes scissors!'
        elif p_choice == 'paper' and c_choise =='scissors':
            winner = 'Computer'
            phrase = ' Scissors cut paper'
        elif p_choice == 'scissors' and c_choise =='scissors':
            winner = 'tie'
            phrase = ' It is a tie, again!'

        else:
            print("Round winner not calculated")
            winner = 'tie'
            phrase = 'It is a tie, how boring!'

     #Display round results
    print("\t " + phrase)
    if winner == 'Player':
     print("\tYou win round " + str(game_round + 1) + '.')
     p_score +=1
    elif winner == 'Computer':
     print("\tComputer wins round " + str(game_round + 1) + '.')
     c_score +=1
    else:
     print('This round is a tie')

    #Player did not make a valid move
else:
     print("That is not a valid game option")
     print("Computer gets the point!")
     c_score += 1

#Game ended print results
print('Final Game results')
print(' For ' + str(rounds) +' rounds ' + 'The Player score is: ' + str(p_score) + ' And the Computer score is: ' + str(c_score))
if p_score < c_score:
    print('The winner of the game is the Computer')
elif c_score < p_score:
    print('The winner of the game is the Player')
else:
    print('There is no winner, have a rematch!')