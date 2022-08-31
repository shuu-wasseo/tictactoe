# 2-player mode
def twoplayer():
  win = False # status of whether game is over or not
  playerid = 0 # playerid % 2 -> identity of player
  playerletter = "o" # letter player uses
  tttboard = {
    "a1" : 0,
    "a2" : 1,
    "a3" : 2,
    "b1" : 3,
    "b2" : 4,
    "b3" : 5,
    "c1" : 6,
    "c2" : 7,
    "c3" : 8
  } # ttt values vs tictacboard values
  ttt = "         " # argument for tictacboard()
  
  # loop until someone wins
  while win == False:
    
    # print board
    print("------------------")
    print(tictacboard(ttt))
    print("------------------")
    
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
    ttt = ttt[:tttboard.get(playstr)] + playerletter + tttboard.get(playstr)+1:]
      
    # check for win
    threeinrow = ["012", "345", "678", "036", "147", "258", "048", "246"] # possible rows
    for x in threeinrow: #checks for every row combination
      if ttt[int(x[0])] != " " and ttt[int(x[0])] == ttt[int(x[1])] and ttt[int(x[1])] == ttt[int(x[2])]:
        print("\nwinner: " + ttt[int(x[0])])
        win = True
        break

    playerid += 1
    print("\n")
