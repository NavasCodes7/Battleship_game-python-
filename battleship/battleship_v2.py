from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

def playerTurn():
    print "Player Turn"
    guess_row = int(raw_input("Guess Row: "))
    guess_col = int(raw_input("Guess Col: "))
    
    if guess_row == ship_row and guess_col == ship_col:
        
        board[guess_row][guess_col] = "T"
        print_board(board)
        print "Congratulations! You sank the battleship!.. you won"
        return True
    else:
        if guess_row not in range(5) or \
          guess_col not in range(5):
            print "Oops, that's not even in the ocean."
            playerTurn()
            
        elif board[guess_row][guess_col] == "X":
          print( "You guessed that one already." )
          playerTurn()
        else:
          print "You missed"
          board[guess_row][guess_col] = "X"
        return False

def computerTurn():
    
    row = random_row(board)
    col = random_col(board)
    print row
    print col
    
    if row == ship_row and col == ship_col:
        board[row][col] = "T"
        print_board(board)
        print "oops computer sank battleship!.. you lost"
        return True
    else:
        if board[row][col] == "X":
          computerTurn()
        else:
          print "computer missed the battleship!"
          board[row][col] = "X"
        return False

while(True):
    
    
    hadwon = playerTurn()

    if hadwon:
        break
    print_board(board)

    
    raw_input("Computers Turn")
    compwon = computerTurn()
    if compwon:
        break
    print_board(board)

    

      
