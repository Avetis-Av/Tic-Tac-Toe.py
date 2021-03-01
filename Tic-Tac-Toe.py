# This is my Tic-Tac-Toe project

#initializes the board for the game
board = [['  ', '  ', '  '],['  ', '  ', '  '],['  ', '  ', '  ']]

#prints the current board
def print_board(board):
    print('----------------')
    print('| ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2] + ' |')
    print('-----+----+-----')
    print('| ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2] + ' |')
    print('-----+----+-----')
    print('| ' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2] + ' |')
    print('----------------')

# prints instructions
def print_instructions():
    print('Each player gets a token of two characters(i.e. XX or AB).')
    print('To place your token in a spot, enter the row number, press "Enter" and then the coloumn number, starting with 1.') 
    print('Top left of the board is 1x1 and bottom right of the board is 3x3.')
    print('To proceed with the game, enter: Yes. Otherwise, enter: No.')

# checks if the board is full
def is_full(board):
    location = 0
    x = 0
    while (x < 3):
        y = 0
        while (y < 3):
            if (board[x][y] != '  '):
                location += 1
            y += 1
        x += 1
    
    return location == 9
 
# checks if the board has a winning combination
def game_win(board):
    win = False
    x = 0
    # iterates through the rows
    while x < 3:
        y = 0
        # iterates through the coloumns
        while y < 3:
            # x-value in the first row
            if x == 0:
                # y-value in the first coloumn
                if y == 0:
                    win = ((board[x][y] == board[x][y + 1] == board[x][y + 2] != '  ') or 
                        (board[x][y] == board[x + 1][y + 1] == board[x + 2][y + 2] != '  ') or 
                        (board[x][y] == board[x + 1][y] == board[x + 2][y] != '  '))
                    if win == True:
                        return win
                # y-value in the second coloumn
                elif y == 1:
                    win = (board[x][y] == board[x + 1][y] == board[x + 2][y] != '  ')
                    if win == True:
                        return win
                # y-value in the third coloumn
                else:
                    win = ((board[x][y] == board[x + 1][y - 1] == board[x + 2][y - 2] != '  ') or 
                        (board[x][y] == board[x + 1][y] == board[x + 2][y] != '  '))
                    if win == True:
                        return win
            # x-value in the second row
            elif x == 1:
                # y-value in the first coloumn
                if y == 0:
                    win = (board[x][y] == board[x][y + 1] == board[x][y + 2] != '  ')
                    if win == True:
                        return win
            # x-value in the third row
            else:
                # y-value in the first coloumn
                if y == 0:
                    win = (board[x][y] == board[x][y + 1] == board[x][y + 2] != '  ')
                    if win == True:
                        return win
            y += 1
        x += 1
    return win

# runs the 3x3 game of Tic-Tac-Toe
def game():
    # prints instructions for the game
    print_instructions()
    print('Proceed?')
    proceed = input()
    if (proceed == 'Yes'):
        p_1 = ' '
        p_2 = ' '
        while len(p_1) != 2:
            print('Player 1, please enter your two characters')
            p_1 = input()
            if len(p_1) != 2:
                print('Characters Not Valid!')
                continue

        while len(p_2) != 2:
            print('Player 2, please enter your two characters')
            p_2 = input()
            if len(p_2) != 2:
                print('Characters Not Valid!')
                continue

        turn = 0

        # requests tokens and positions while the board is not full
        while(is_full(board) == False):
            turn += 1
            if (turn % 2 == 1):
                print ('Player 1: please enter the row and then the coloumn of your token')
                x = int(input()) - 1 
                y = int(input()) - 1
                if board[x][y] != '  ':
                    print('You cannot place there! That space is occupied!!')
                    turn -= 1
                    continue
                board[x][y] = p_1
            else:
                print ('Player 2: please enter the row and then the coloumn of your token')
                x = int(input()) - 1 
                y = int(input()) - 1
                if board[x][y] != '  ':
                    print('You cannot place there! That space is occupied!!')
                    turn -= 1
                    continue
                board[x][y] = p_2
            print_board(board)

            # checks for possible win-conditions after 4 moves have been made 
            # 4 is the maximum number of moves in this game where no win is possible
            if turn >= 5:
                if game_win(board):
                    if turn % 2 == 1:
                        print ('Player 1 has won!!!')
                        return 0
                    else:
                        print ('Player 2 has won!!!')
                        return 0
        
        # checks for win conditions after the board has been filled
        if game_win(board):
            if turn % 2 == 1:
                print ('Player 1 has won!!!')
                return 0
            else:
                print ('Player 2 has won!!!')
                return 0
        else:
            print("It's a Tie!! The board is full.")


    else:
        print('See you next time!')

game()
    