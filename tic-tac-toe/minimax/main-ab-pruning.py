#TIC-TAC-TOE using minimax algorithm 
#By Sagar-Kr-Thapa

#packages 
from board import Board
from math import *

import sys
sys.setrecursionlimit(5000)

count=0

DRAW_POINT=0
WIN_POINT=1
LOSE_POINT=-1

'''
This is the crux of our game. It iterates over all the available spots to select the best move.
'''
#In our algorithm depth has no importance, one can use it to provide values to deep nodes accordingly
def minimax( board,depth,alpha,beta,maximizingPlayer='X' ): 

    global count 
    count+=1

    #checking if the board is in win/draw state
    if( board.win_check(board.player_1) ):
        return WIN_POINT
    elif ( board.win_check(board.player_2) ):
        return LOSE_POINT
    elif ( board.draw_check() ):
        return DRAW_POINT


    #further iterating
    if( maximizingPlayer=='X' ):
        maxValue=-inf
        for row in range(3):
            for col in range(3):
                #Is the slot empty?
                if( board.state[row,col]==board.empty_square ):
                    #Filling the slot
                    board.state[row,col]=maximizingPlayer
                    value = minimax(board,depth+1,alpha,beta,'O')  
                    maxValue = max(maxValue, value)
                    #Restoring the slot
                    board.state[row,col]=board.empty_square
                    alpha=max(alpha,value)
                    if beta<=alpha:
                        break

        return maxValue

    else:
        minValue=inf
        for row in range(3):
            for col in range(3):
                #Is the slot empty?
                if( board.state[row,col]==board.empty_square ):

                    board.state[row,col]=maximizingPlayer
                    value = minimax(board, depth+1, alpha, beta, 'X')
                    minValue = min(minValue, value)
                    #Restoring the slot
                    board.state[row,col]=board.empty_square
                    beta=min(beta,value)
                    if beta<=alpha:
                        break
                    
        return minValue 



'''
The best move for the computer is determined by this function.
It iterates for all remaining positions finding out the best position optimal for the computer. 
This optimal position is determined by value which is initially positive infinity.
Since the computer is minimizing player, we initialize the value with positive infinity.
'''
def best_move(board):
    value=inf
    bestMove=[-1,-1]
    for row in range(3):
        for col in range(3):
            #Is the slot empty?
            if( board.state[row,col]==board.empty_square ):
                #Filling the slot
                board.state[row,col]='O'
                val=minimax(board,1,-inf,inf,'X')
                if( val<value ):
                    value = val
                    bestMove[0], bestMove[1] = row, col
                #Restoring the slot
                board.state[row,col]=board.empty_square
    return bestMove



'''
This is the game play function which allows user to input the (row,col) coordinates for their move.
'''
def game_play():

    #creating a board
    b=Board()
    print("Type 'exit' to quit!!!!")

    #printing initial state of the board
    b.print_board()

    while True:
        #asking for user input
        user_ip = input("> ")

        #handling exit
        if user_ip=='exit': break
        
        #handling empty input
        if user_ip=='': continue

        try:
            #parsing user input
            row, col = map(int, user_ip.split(','))

            if( b.state[row,col]!=b.empty_square ):
                print("Illegal Move!!!")
                continue

            #make move
            b.fill_cell(row,col,'X')

            #best move
            row,col=best_move(b)

            b.fill_cell(row,col,'O')

            b.print_board()

            print(count)

            if( b.win_check(b.player_1) ):
                print("YOU WON!!")
                break
            elif( b.win_check(b.player_2 )):
                print("YOU LOSE!!")
                break
            elif( b.draw_check() ):
                print("DRAW")
                break

        except Exception as e:
            print( "ERROR!!! ",e)
            print( "GAME INPUT: row,col" )


############################################################################
# ATTENTION ATTENTION ATTENTION                                            #
############################################################################

#Starting the game 
#You are player -> 'X'
#Computer is player -> 'O'

game_play()

