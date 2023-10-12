import checkers

# creating  function to ask user size of board and call build_board
def game():
    board_size = int(input("What is the size of the board? Enter a number 4-16: "))
    full_board = checkers.build_board(board_size)
    #new_shape = checkers.board_shape(board_size)
    print(full_board)

# Print how many of each square
    print("Here's how many red squares: ")
    red = (full_board == "Red")
    print(checkers.get_count(full_board, red))

    print("Here's how many black squares: ")
    black = (full_board == "Black")
    print(f"{checkers.get_count(full_board, black)}")

    print("Here's how many empty squares: ")
    empty = (full_board == "empty")
    print(f"{checkers.get_count(full_board, empty)}")

if __name__ == '__main__':
    game()

