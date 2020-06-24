#A tic tac toe game
#Plans: make a two human player version (input error checking, win conditions), then add option to play against computer, then look at graphics libs to make GUI
#so far this is just the print board function

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'bot-L': ' ', 'bot-M': ' ', 'bot-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-R'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-R'] + '|' + board['mid-R'])
    print('-----')
    print(board['bot-L'] + '|' + board['bot-R'] + '|' + board['bot-R'])

printBoard(theBoard)
