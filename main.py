
# Tic Tac Toe game (YT).

"""
LOGIC OUTLINE

GAME PARAMETERS
3x3 game board grid matrix, 9 boxes total
2 players, each player assigned a mark X or O
X goes first
Each player takes turns putting their marks into empty squares
First player to get 3 marks in a row vertically, horizontally, or diagonally wins
When all 9 squares are marked, the game is over, win or tie

LOGIC
Prompt player, do they want X or O?
Display board to user
Prompt player 1, pick a square to mark, make a move
Validate board, check if there is a winner or whether board is filled
Prompt player 2 to pick a square to mark, make a move
Repeat same validation logic as Player 1
Game loop until we have a winner or tie, then game over

REUSABLE FUNCTIONS
Which logic is getting repeated multiple times?
-Make a move
-Check for a winner or tie
-Game loop:
    1. User make a move
    2. Is there a winner?
    3. Is the board filled?

"""
# Player 1 makes a move
# Display the board
# Check for the winner
# Check if the board is filled

# Player 2 makes a move
# Display the board
# Check for the winner
# Check if the board is filled

# Go back and clean up/comment out all unwanted code, i.e. inserted check print statements, refactor, and optimize.

# Can add invalid input intake and message
# Can add edit mark feature

# Import libraries? - Not necessary for this implementation.
# import numpy as np - Not necessary.

"""
# Test code

# Represent X and O
x = 1
o = 0

# Players
player1 = p1
player2 = p2

# Prompt player X or O?
p1 = input('Player 1, choose X or O: ')
p2 = input('Player 2, choose X or O: ')

# Default assignment
if p1 == x:
    p2 = o
if p1 == o:
    p2 = x

# Initialize empty grid
g = np.empty((3,3))

# Display grid to Player 1
def draw():
    board = ''

    for i in range(-1,6):

        if i%2==0:
            board += '|      ' * 4
            board += '\n|      |      |      |'

        else:
            board += ' _____ ' * 3

        board += '\n'
    print (board)

draw()
"""
# Grid 2D list access via coordinates
#    0   1   2
# 0 [ ] [ ] [ ]
# 1 [ ] [ ] [ ]
# 2 [ ] [ ] [ ]

# Test counter variable
"""
totalMoves = 0
"""

player1Mark = input("Please choose X or O")
if player1Mark == "X":
    player2Mark = "O"
else:
    player2Mark = "X"

"""
print(player1Mark, player2Mark)
"""

board = []
for row in range(3):
    board.append([""] * 3)

"""
for row in range(3):
    print(board[row])
"""

def isValid(row, col):
    if not (row >= 0 and row < 3 and col >= 0 and col < 3):
        return False

    return board[row][col] == ""

def playerMakeMove(mark):
    isValidMove = False

    while not isValidMove:
        inputRow = int(input(f"{mark}: Please pick a row"))
        inputColumn = int(input(f"{mark}: Please pick a column"))

        isValidMove = isValid(inputRow, inputColumn)
        if not isValidMove:
            print("Please enter a valid input")

    """
    totalMoves += 1
    """

    board[inputRow][inputColumn] = mark

# Refactored into ticTacToe()
"""
playerMakeMove(player1Mark)

for row in range(3):
    print(board[row])
    
playerMakeMove(player2Mark)

for row in range(3):
    print(board[row])
"""

def checkHorizontal():
    for row in range(3):
        mark = board[row][0]
        if mark == "":
            continue

        matches = 1
        for col in range(1, 3):
            if mark == board[row][col]:
                matches += 1

        if matches == 3:
            return True

    return False

def checkVertical():
    for col in range(3):
        mark = board[0][col]
        if mark == "":
            continue

        matches = 1
        for row in range(1, 3):
            if mark == board[row][col]:
                matches += 1

        if matches == 3:
            return True

    return False

def diagonal(row, col, increment):
    mark = board[row][col]
    if mark == "":
        return False

    matches = 1
    for _ in range(2):
        row += increment
        col += increment
        if mark == board[row][col]:
            matches += 1

    return matches == 3

def checkDiagonal():
    return diagonal(0, 0, 1) or diagonal(0, 2, -1)

def checkWinner():
    return checkHorizontal() or checkVertical() or checkDiagonal()

for row in range(3):
    print(board[row])

"""
print(checkWinner())
"""

def checkBoardFilled():
    for row in range(3):
        for col in range(3):
            if board[row][col] == "":
                return False
    return True

"""
def checkBoardFilled():
    return totalMoves == 9
"""

# Now have all the logic for the game.

# Now need to create game loop.
# Use code logic skeleton to ensure all required steps are accounted for.
# And refactor as necessary to simplify code.


# Wrap in function so can exit the function when the game ends.
# With loops only, break. But within functions, return.
def ticTacToe():
    while True:
        for mark in [player1Mark, player2Mark]:
            playerMakeMove(mark)

            for row in range(3):
                print(board[row])

            if checkWinner():
                print(mark, "wins!")
                return

            if checkBoardFilled():
                print("Game over")
                return

ticTacToe()
