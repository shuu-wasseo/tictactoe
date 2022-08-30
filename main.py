# prints a tic-tac-toe board, board takes a string argument filled with characters "o", "x" and " "
def tictacboard(oxb):
  board = f"""
  a     b     c
      |     |     
1  {oxb[0]}  |  {oxb[1]}  |  {oxb[2]}  
 _____|_____|_____
      |     |     
2  {oxb[3]}  |  {oxb[4]}  |  {oxb[5]}  
 _____|_____|_____
      |     |     
3  {oxb[6]}  |  {oxb[7]}  |  {oxb[8]}  
      |     |     
"""
  return board

# 2-player mode
def twoplayer():
  win = False # status of whether game is over or not
  playerid = 0 # playerid % 2 -> identity of player
  playerletter = "o" # letter player uses
  ttt = "         " # argument for tictacboard()
  
  # loop until someone wins
  while win == False:
    
    # print board
    print(tictacboard(ttt))
    
    # player identity
    if playerid % 2 == 0:
      print("player: o")
      playerletter = "o"
    else:
      print("player: x")
      playerletter = "x"
    
    # print instructions + input
    while 1:
      playstr = input("enter the column and then row of the cell you want to play in: (e.g. a1 for top left box) ")
      if playstr[0] in "abc" and playstr[1] in "123":
        break
    
    # add into ttt
    if playstr[0] == "a":
      ttt[int(playstr[1])] == playerletter
    elif playstr[0] == "b":
      ttt[3 + int(playstr[1])] == playerletter
    elif playstr[0] == "c":
      ttt[6 + int(playstr[1])] == playerletter
      
    # check for win
    threeinrow = ["012", "345", "678", "036", "147", "258", "048", "246"] # possible rows
    for x in threeinrow: #checks for every row combination
      if ttt[int(x[0])] == ttt[int(x[1])] and ttt[int(x[1])] == ttt[int(x[2])]:
        print("winner: " + ttt[int(x[0])])
        win == True
