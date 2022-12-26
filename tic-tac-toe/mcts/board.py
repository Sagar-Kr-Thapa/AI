from copy import deepcopy as dc

#Board class 
class Board():

    def __init__(self, board=None):
        self.player_1='X'
        self.player_2='O'

        self.empty_square='.'
        #player positions        
        self.state={}

        if board is not None:
            self.__dict__ = dc(board.__dict__)
        else:
            self.initialize()

    def initialize(self):
        for row in range(3):
            for column in range(3):
                self.state[row,column] = self.empty_square
        pass

    def print_board(self):
        for row in range(3):
            for column in range(3):
                print(self.state[row,column], end='\t')
            print()
        pass


    def is_terminal(self):
        for row in range(3):
            for col in range(3):
                if( self.state[row,col]==self.empty_square ):
                    return False
        return True

    def win_check(self, player=None):
        if( player==None ): player=self.player_2
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
    
    def generate_states(self):
        actions=[]

        for row in range(3):
            for col in range(3):
                if( self.state[row,col]==self.empty_square ):
                    actions.append(self.make_move(row,col))
        

        return actions

    
    def make_move(self, row, col):
        board = Board(self)
        board.state[row,col] = self.player_1
        board.player_1, board.player_2 = board.player_2, board.player_1

        return board


    def get_possible_actions(self):
        actions=[]
        for row in range(3):
            for col in range(3):
                if( self.state[row,col]==self.empty_square ):
                    actions.append((row,col))

        return actions


    def take_action(self, action):
        row, col = action
        self.state[row,col] = self.player_1

        b=Board(self)
        (b.player_1, b.player_2) = (b.player_2, b.player_1)

        return b
