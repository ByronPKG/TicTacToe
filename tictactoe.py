#! /usr/bin/python3
#A tic tac toe game
#Plans: make a two human player version (input error checking, win conditions), then add option to play against computer, then look at graphics libs to make GUI
#todo: check for win conditions/early draw, a better method for switching players each turn, regex for move input checking


#    theBoard = {'TOP-L': ' ', 'TOP-M': ' ', 'TOP-R': ' ',
#                'MID-L': ' ', 'MID-M': ' ', 'MID-R': ' ',
#                'BOT-L': ' ', 'BOT-M': ' ', 'BOT-R': ' '}

def printBoard(board):
    print(board['TOP-L'] + '|' + board['TOP-M'] + '|' + board['TOP-R'])
    print('-----')
    print(board['MID-L'] + '|' + board['MID-M'] + '|' + board['MID-R'])
    print('-----')
    print(board['BOT-L'] + '|' + board['BOT-M'] + '|' + board['BOT-R'])

def chooseSymbol(): #returns symbol chosen for player1, player2 handled by calling function
    while True:
        print("Player 1, would you like to be 'X' or 'O'?")
        player1 = str(input()).upper()
        if player1 == 'X' or player1 == 'O':
            return player1

def isValidMove(board, move): #Returns bool if the move is valid, there space is open
    if board[move] == ' ':
        return True
    else:
        return False


def singleplayer():
    print("Single-player: WIP")


def multiplayer():
    player1 = chooseSymbol()
    player2 = 'X' if player1 == 'O' else 'O'
    print("OK, Player 1 is '%s's and Player 2 is '%s's." % (player1, player2))

    turn = 0
    theBoard = {'TOP-L': ' ', 'TOP-M': ' ', 'TOP-R': ' ',
                'MID-L': ' ', 'MID-M': ' ', 'MID-R': ' ',
                'BOT-L': ' ', 'BOT-M': ' ', 'BOT-R': ' '}
    printBoard(theBoard) #displaying the empty board

    while turn < 9: #forces all moves to be made, make a function that checks for an early draw
        print("Player %d, make your move: ROW-COLUMN=(TOP, MID, BOT)-(L,M,R)" % (turn%2+1))
        move = str(input()).upper() #need to implement input checking function, look up regex for it
        if isValidMove(theBoard, move):
            theBoard[move] = player2 if turn%2 else player1
            turn += 1   #Move made and turn completed
        else:
            print("Invalid move.")
            continue #Re-prompt for a valid move

        printBoard(theBoard) #print out the new board at "end" of each turn
#       if turn > 5
#           winner = findWinner(theBoard)   #a win can only occur after turn 5
#           if winner is not ' ':
#

def main():
    print('TIME TO PLAY TIC TAC TOE.')
    while True:
        try:
            print('Pick your game mode: (1)Single-player, (2)Two-player, (0) Quit')
            mode = int(input())
            if mode == 0:
                break
            elif mode == 1:
                singleplayer()
            elif mode == 2:
                multiplayer()
            else:
                print("Sorry, I didn't recognize your input: %d. Please try again." % (mode))
        except ValueError:
            print('Please enter your selection as a number.')   #If input can't cast to int
            continue

    print('Goodbye! Thank you for playing!')

if __name__ == '__main__':
    main()
    exit(0)
