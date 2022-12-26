from copy import deepcopy as dc

#Board class 
class Board():

    def __init__(self, state=None):

        self.player_1='X'
        self.player_2='O'

        self.empty_square='.'
        #player positions        
        self.state={}

        if state is not None:
            for row in range(3):
                for column in range(3):
                    self.state[row,column]=dc(state[row][column])
        else:
            self.initialize()

    def initialize(self):
        for row in range(3):
            for column in range(3):
                self.state[row,column] = self.empty_square

    def print_board(self):
        for row in range(3):
            for column in range(3):
                print(self.state[row,column], end='\t')
            print()

    def win_check(self, player):
        #row check
        for column in range(3):
            count=0
            for row in range(3):
                if( self.state[row,column]==player ):
                    count+=1
            if( count==3 ):
                return True

        #column check
        for row in range(3):
            count=0
            for column in range(3):
                if( self.state[row,column]==player ):
                    count+=1
            if( count==3 ):
                return True
        
        #diagonal 1 check
        count=0
        for row in range(3):
            column=row 
            if( self.state[row,column]==player ):
                count+=1
        if( count==3 ):
            return True

        #diagonal 2 check
        count=0
        for row in range(3):
            column=2-row
            if( self.state[row,column]==player ):
                count+=1
        if( count==3 ):
            return True

        #Else return false
        return False


    def draw_check(self):
        for row in range(3):
            for col in range(3):
                if( self.state[row,col]==self.empty_square ):
                    return False
        return True 

    def fill_cell(self, row, col, player):
        self.state[row,col] = player 
