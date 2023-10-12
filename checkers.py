if __name__ == "__main__":
    print("This is not intended to be run as main.")

import numpy
from numpy import random
from numpy import reshape

# first function
def build_board(size):
    board = random.choice(['Empty', 'Red', 'Black'], size = (size,size))
    return(board)

# second function
def get_count(board, color):
    return((board == color).sum())

# function to change shape of board
#def board_shape(shape):
    #shape2 = numpy.reshape(shape = (shape,shape))



