#TIC-TAC-TOE using MCTS
#By: Sagar-Kr-Thapa

#packages
from board import Board
from mcts import mcts
from copy import deepcopy as dc


def game_play():

    #creating board instance with no prior configuration
    b=Board()
    print("Type 'exit' to quit!!!")

    #printing initial state of the board 
    b.print_board()

    #creating MCTS instance
    game = mcts()

    # b = b.take_action((0,0))

    # b = game.iterate(b)

    # b.print_board()

    while True:
        user_ip = input("> ")

        #break if typed exit
        if user_ip == 'exit': break

        #continue if no null string is provided
        if user_ip == '': continue

        # try: 
            #parsing input
        row, col = map(int,user_ip.split(','))           

        #checking if the move is legal
        if( b.state[row,col]!=b.empty_square ):
            print(" Illegal Move ")
            continue
        
        #make move
        b = b.take_action((row,col))

        #Finding the best move
        try:
            b = game.iterate(b)
        except:
            pass

        b.print_board()

        if( b.win_check() ):
            print("PLAYER %s WON!!"%b.player_2)
            break
        elif( b.draw_check() ):
            print("DRAW")
            break


############################################################################
# ATTENTION ATTENTION ATTENTION                                            #
############################################################################

#Starting the game 
#You are player -> 'X'
#Computer is player -> 'O'

game_play()



