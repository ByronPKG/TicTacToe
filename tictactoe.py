#! /usr/bin/python3
#A tic tac toe game
#Plans: make a two human player version (input error checking, win conditions), then add option to play against computer, then look at graphics libs to make GUI
#so far this is just the print board function

#Make a board struct-like? struct in python?
#theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'bot-L': ' ', 'bot-M': ' ', 'bot-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-R'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-R'] + '|' + board['mid-R'])
    print('-----')
    print(board['bot-L'] + '|' + board['bot-R'] + '|' + board['bot-R'])

def chooseSymbol(): #returns symbol chosen for player1, player2 handled by calling function
    while True:
        print("Player 1, would you like to be 'X' or 'O'?")
        player1 = str(input()).upper()
        if player1 == 'X' or player1 == 'O':
            return player1

def singleplayer():
    print("Single-player: WIP")

def multiplayer():
    player1 = chooseSymbol()
    player2 = 'X' if player1 == 'O' else 'O'
    print("OK, Player 1 is '%s's and Player 2 is '%s's." % (player1, player2))

    turn = 0
    theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'bot-L': ' ', 'bot-M': ' ', 'bot-R': ' '}
    printBoard(theBoard)

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
