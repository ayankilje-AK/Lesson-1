''' Will make the board using dictionary in which keys will be location(top_left, mid_left, etc.) and initially its values will be empty space and after every move, we will change the valus according to the player's choice of move '''

the_board = {'7':' ', '8:':' ', '9':' ',
             '4':' ', '5':' ', '6':' ',
             '1':' ', '2':' ', '3':' '}

board_keys = []

for key in the_board:
    board_keys.append(key)
    '''Will have to print the updated board after every move in the game and will make a function in which we will define the print_board function, so that we can easily print the board every time by calling this function'''

def print_board(board):

    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():

    turn = "X"
    count = 0
    for i in range(10):
        print_board(the_board)
        print("It's your turn" + turn + "Move to which place")
        move = input("Enter your next move: ")
        if the_board[move] == ' ':
            the_board[move] = turn
            count += 1
        else:
            print("The place is already filled and move to another place")
            continue
        if count >= 5:
            if the_board['7'] == the_board['8'] == the_board['9'] != ' ':
                print_board(the_board)
                print("GAME OVER")
                print("*****" + turn + "Won")
                break
            elif the_board['4'] == the_board['5'] == the_board['6'] != ' ':
                print_board(the_board)
                print("GAME OVER")
                print("*****" + turn + "Won")
                break
            elif the_board['1'] == the_board['2'] == the_board['3'] != ' ':
                print_board(the_board)
                print("GAME OVER")
                print("*****" + turn + "Won")
                break
            elif the_board['1'] == the_board['4'] == the_board['7'] != ' ':
                print_board(the_board)
                print("GAME OVER")
                print("*****" + turn + "Won")
                break
            elif the_board['2'] == the_board['5'] == the_board['8'] != ' ':
                print_board(the_board)
                print("GAME OVER")
                print("*****" + turn + "Won")
                break
            elif the_board['3'] == the_board['6'] == the_board['9'] != ' ':
                print_board(the_board)
                print("GAME OVER")
                print("*****" + turn + "Won")
                break
            elif the_board['7'] == the_board['5'] == the_board['3'] != ' ':
                print_board(the_board)
                print("GAME OVER")
                print("*****" + turn + "Won")
                break
            elif the_board['1'] == the_board['5'] == the_board['9'] != ' ':
                print_board(the_board)
                print("GAME OVER")
                print("*****" + turn + "Won")
                break
        
        if count == 9:
            print("GAME OVER")
            print("The game has ended in a draw.")
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        
    restart = input("Would you like to play agein. y/n")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            the_board[key] = " "
        game()


if __name__ == "__main__":
    game()
