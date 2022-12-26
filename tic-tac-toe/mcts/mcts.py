import math 
import random
from copy import deepcopy as dc


x_wins = 0
o_wins = 0
draws = 0


class treeNode():
    
    def __init__(self, state, parent=None):
        self.state = state
        self.is_terminal = state.is_terminal()
        self.is_fully_expanded = self.is_terminal
        self.parent = parent
        self.n = 0
        self.w = 0
        self.children = {}

    def __str__(self):
        s=[]
        s.append("Total Reward: %s"%(self.w))
        s.append("Total Visits: %d"%(self.n))
        return "%s: {%s}"%(self.__class__.__name__,', '.join(s))


class mcts():

    def __init__(self, exploration_constant=2, simulations=5000 ):
        self.iteration_limit = simulations
        self.exploration_constant = exploration_constant

    
    def rollout_policy(self, node):

        # actions = node.state.getPossibleActions() 
        board = dc(node.state)

        actions=[]
        for row in range(3):
            for col in range(3):
                if( board.state[row,col]==board.empty_square ):
                    actions.append((row,col))

        while not board.win_check():
            try:
                action = random.choice(actions)
                board = board.take_action(action)
                actions.remove(action)
            except:
                return 0
        

        if board.player_2 == 'X': return 1
        else: return -1


    def iterate(self, initial_state):
        global x_wins
        global o_wins
        global draws
        self.root = treeNode(initial_state,None)

        for i in range(self.iteration_limit):
            node = self.selection(self.root)
            self.simulation(node)

        # best_child = self.select_child(self.root, 0)
        best_child = self.get_best_child(self.root, 0)

        # for children in self.root.children.values():
        #     print("+++++++++++++++++++++++++++")
        #     children.state.print_board()
        #     print(children.w, children.n)
        #     print("+++++++++++++++++++++++++++")

        print( x_wins, o_wins, draws)
        return dc(best_child.state)
        

    def selection(self, node):
        while not node.state.is_terminal():
            if node.is_fully_expanded:
                # node = self.select_child(node, self.exploration_constant)
                node = self.get_best_child(node, self.exploration_constant)
            else:
                return self.expansion(node)
        return node


    def expansion(self, node):
        # board = dc(node.state)
        # actions = board.get_possible_actions()
        actions=node.state.generate_states()

        for action in actions:
            if str(action.state) not in node.children:
                new_node = treeNode(action, node)

                node.children[str(action.state)] = new_node

                if len(actions)==len(node.children):
                    node.is_fully_expanded = True

                return new_node


    def simulation(self, initial_node):
        global x_wins
        global o_wins
        global draws
        reward = self.rollout_policy(initial_node)
        if( reward==1 ):x_wins+=1
        elif( reward==-1 ):o_wins+=1
        else: draws+=1
        self.backpropagation( initial_node, reward )



    def backpropagation(self, node, reward):
        winner = None
        if( reward>0 ): winner = 'X'
        elif( reward<0 ): winner = 'O'

        while node is not None:
            node.n += 1
            # if winner==node.state.player_2: node.w += 1
            node.w += reward
            node = node.parent


    def select_child(self, node, exploration_value ):
        max_value = -math.inf
        best_nodes = []
        
        for child in node.children.values():
            UCB = (child.w/child.n) + exploration_value * math.sqrt( 2*math.log(node.n)/child.n )
            
            if( UCB>max_value ):
                max_value = UCB
                best_nodes = [child]
            elif UCB==max_value:
                best_nodes.append(child)

        return random.choice(best_nodes)


    def get_best_child(self, node, exploration_value):
        best_value = -math.inf
        best_nodes = []

        current_player = 1 if node.state.player_1=='X' else -1

        for child in node.children.values():
            # if child.state.player_2 == 'X': current_player = 1
            # else: current_player = -1
            node_value = (current_player * child.w)/child.n + exploration_value * math.sqrt( math.log(node.n)/child.n )
            if node_value > best_value:
                best_value = node_value
                best_nodes = [child]
            # elif node_value == best_value:
                # best_nodes.append(child)

        return random.choice(best_nodes)