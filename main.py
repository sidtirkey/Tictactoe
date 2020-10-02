

game_is_still_on = True
winner= None
current_player= 'X'

board =["_", "_","_",
        "_","_","_",
        "_","_","_"]

board1 =["1", "2","3",
        "4","5","6",
        "7","8","9"]
print( board1[0] + "|" + board1[1] + "|" + board1[2] )
print( board1[3] + "|" + board1[4] + "|" + board1[5] )
print( board1[6] + "|" + board1[7] + "|" + board1[8] )
print("\n ______________________________________________   \n")


def display_board():
  print( board[0] + "|" + board[1] + "|" + board[2] )
  print( board[3] + "|" + board[4] + "|" + board[5] )
  print( board[6] + "|" + board[7] + "|" + board[8] )

def play_game():
  display_board()

  while game_is_still_on:
    print("\n It's  "+ current_player + "  turn")
    turn_handle(current_player)
    
    check_game()
    swap_player()

  if winner=="X" or winner=="O":
    print ("winner is:" + winner)
  elif winner==None:
     print("It's a tie!!") 


def check_game():
  check_if_win()
  check_if_tie()


  
def check_if_win():
  row_check()
  coloumn_check()
  diagonal_check()


def row_check():
  global game_is_still_on
  global winner
  row_1= board[0] == board[1] == board[2] != '_'
  row_2= board[3] == board[4] == board[5] != '_'
  row_3= board[6] == board[7] == board[8] != '_'
  if row_1 or row_2 or row_3:
    game_is_still_on= False
    

  if row_1:
    winner= board[0]
    return board[0]
   
  elif row_2:
    winner= board[3]
    return board[3]
    
  elif row_3:
    winner= board[6]
    return board[6]
      

def coloumn_check():
  global game_is_still_on
  global winner
  coloumn_1= board[0] == board[3] == board[6] != '_'
  coloumn_2= board[1] == board[4] == board[7] != '_'
  coloumn_3= board[2] == board[5] == board[8] != '_'
  if coloumn_1 or coloumn_2 or coloumn_3:
    game_is_still_on= False

  if coloumn_1:
    winner= board[0]
    return board[0]
  elif coloumn_2:
    winner=board[1]
    return board[1]
  elif coloumn_3:
    winner=board[2]
    return board[2]

def diagonal_check():
  global game_is_still_on
  global winner
  diagonal_1= board[0] == board[4] == board[8] != '_'
  diagonal_2= board[2] == board[4] == board[6] != '_'
  
  if diagonal_1 or diagonal_2:
    game_is_still_on= False

  if diagonal_1:
    winner= board[0]
    return board[0]
  elif diagonal_2:
    winner=board[2]
    return board[2]
  




def turn_handle(current_player):
  position = input("\n Enter a position from 1-9 (position 1 refers to left top corner and increases rightwards) or see the above figur with numbers wherer numbers indicate the postion in matrix: ")
  valid= True
  position_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

  while valid:

    while position not in position_list:
      print("\n Invalid input!! \n")
      position = input("\n Enter a position from 1-9 (position 1 refers to left top corner and increases rightwards) or see the above figure with numbers where numbers indicate the postion in matrix: ")
    position = int(position) - 1
    if board[position] == '_':
      valid= False
    else:
      print('\n Position already taken!! \n')



  board[position]= current_player
  display_board()


def swap_player():
  global current_player
  if current_player == 'X':
    current_player = 'O'
  else:
    current_player = 'X'


def check_if_tie():
  global game_is_still_on
  if '_' not in board:
    game_is_still_on= False


play_game()

