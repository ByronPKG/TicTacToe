#! /usr/bin/python3
#A tic tac toe game
#Plans: make a two human player version (input error checking, win conditions), then add option to play against computer, then look at graphics libs to make GUI
#todo: Singleplayer/VS Computer, GUI version (Thought about making validMoveRegex more flexible, but with GUI this is not necessary)
import re
validMoveRegex = re.compile(r'(TOP|MID|BOT)-(L|M|R)')

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

def moveInput(player1Turn=True): #default will assume player 1, to call for vs computer match
    while True:
        print("Player %d, make your move: ROW-COLUMN=(TOP, MID, BOT)-(L,M,R)" % (1 if player1Turn else 2))
        try:
            move = str(input()).upper()
            if validMoveRegex.search(move) is None:
                print("Invalid input. Try again.")
                continue
            return move
        except ValueError:
            print("Invalid input. Try again.")
            continue


def findWinner(board): #Return true if there is a winnter on the board
    rows = ['TOP','MID','BOT']
    columns = ['-L','-M','-R']
    for x in range(3):
        if (board[rows[x]+columns[0]] == board[rows[x]+columns[1]] == board[rows[x]+columns[2]] != ' '): #checks rows
            return True
        if (board[rows[0]+columns[x]] == board[rows[1]+columns[x]] == board[rows[2]+columns[x]] != ' '): #checks columns
            return True
    if ((board['TOP-L'] == board['MID-M'] == board['BOT-R'] != ' ') or
       (board['TOP-R'] == board['MID-M'] == board['BOT-L'] != ' ')): #checks diagnols
       return True
    return False

def singleplayer():
    print("Single-player: WIP")


def multiplayer():
    player1 = chooseSymbol()
    player2 = 'X' if player1 == 'O' else 'O'
    print("OK, Player 1 is '%s's and Player 2 is '%s's." % (player1, player2))

    turn = 0
    player1Turn = True
    theBoard = {'TOP-L': ' ', 'TOP-M': ' ', 'TOP-R': ' ',
                'MID-L': ' ', 'MID-M': ' ', 'MID-R': ' ',
                'BOT-L': ' ', 'BOT-M': ' ', 'BOT-R': ' '}
    printBoard(theBoard) #displaying the empty board

    while turn < 9: #Only 9 moves max
        move = moveInput(player1Turn)
        if theBoard[move] == ' ':
            theBoard[move] = player1 if player1Turn else player2
            turn += 1   #Move made and turn completed
        else:
            print("Invalid move. Try again.")
            continue #Re-prompt for a valid move

        printBoard(theBoard) #print out the new board at "end" of each turn

        if turn > 4: #a win can only occur starting turn 5
            if findWinner(theBoard):
                print("Congratulations, Player %d, you won!" % (1 if player1Turn else 2))
                return None
        player1Turn = not player1Turn

    print('Draw!')
    return None

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
#    exit(0)
