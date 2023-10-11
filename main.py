import checkers

# creating  function to ask user size of board and call build_board
def game():
    board_size = int(input("What is the size of the board? Enter a number 4-16: "))
    full_board = checkers.build_board(board_size)
    #new_shape = checkers.board_shape(board_size)
    print(full_board)




if __name__ == '__main__':
    game()

