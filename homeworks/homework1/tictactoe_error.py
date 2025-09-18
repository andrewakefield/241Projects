"""tictactoe game for 2 players
Andrew Wakefield"""

choices = [] # FIX: initialize choices as an empty array
for x in range (1, 10) : # FIX: change range max to 10 so 9 is included
    choices.append(x)

playerOneTurn = True # FIX: replace equality operator with the assignment operator
winner = False

# FIX: convert choices [i] to str before attempting concatenation
def printBoard() :
    print( '\n -----')
    print( '|' + str((choices[0])) + '|' + str(choices[1]) + '|' + str(choices[2]) + '|')
    print( ' -----')
    print( '|' + str(choices[3]) + '|' + str(choices[4]) + '|' + str(choices[5]) + '|')
    print( ' -----')
    print( '|' + str(choices[6]) + '|' + str(choices[7]) + '|' + str(choices[8]) + '|')
    print( ' -----\n')

while not winner : # FIX: winner should be notted as it is currently False
    printBoard() # FIX: lowercase PrintBoard() to printBoard() to match function name

    if playerOneTurn :
        print( "Player 1:")
    else :
        print( "Player 2:")

    try:
        choice = int(input(">> "))
    except:
        print("please enter a valid field")
        continue

    if choices[choice - 1] == 'X' or choices [choice - 1] == 'O': # FIX: replace assignment operator with equality operator and indice of choices to choice - 1
        print("illegal move, please try again")
        continue

    if playerOneTurn :
        choices[choice - 1] = "X" # FIX: add "" marks around letter so it is recognizes as a string
    else :
        choices[choice - 1] = "O" # FIX: add "" marks around letter so it is recognizes as a string

    playerOneTurn = not playerOneTurn

    for x in range (0, 3) :  # Place break point at this line!
        y = x * 3 # FIX: remove extra indentation
        if (choices[y] == choices[(y + 1)] and choices[y] == choices[(y + 2)]) :
            winner = True
            printBoard()
        if (choices[x] == choices[(x + 3)] and choices[x] == choices[(x + 6)]) :
            winner = True
            printBoard()

    if((choices[0] == choices[4] and choices[0] == choices[8]) or
       (choices[2] == choices[4] and choices[4] == choices[6])) :
        winner = True # FIX: capitalize 'true' to 'True'
        printBoard()

print ("Player " + str(int(playerOneTurn + 1)) + " wins!\n")