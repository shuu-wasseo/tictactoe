oneplayer()
# credits to https://www.wikihow.com/Win-at-Tic-Tac-Toe for tictactoe strats.
  
win = False # status of whether game is over or not
playerletter = "o" # letter player uses
ttt = "         " # argument for tictacboard()
threeinrow = ["012", "345", "678", "036", "147", "258", "048", "246"] # possible rows
corners = ["a1", "a3", "c1", "c3"] # corner tiles
edges = ["a2", "b1", "b3", "c2"] # edge tiles
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
round = 1
humanstarts = input("would you like to start first? (Y/n)")
if humanstarts.lower() == "Y":
  starter = "human"
  playerid = 0 # playerid % 2 -> identity of player
else:
  starter = "computer"
  playerid = 1 # playerid % 2 -> identity of player

# stratvars
conqcorners = False # if human plays b2 on first move 
nob2 = False # if human plays anything besides b2 on first move
secondedge = False # if human plays first but plays edge

# extra functions

# fill corner
def fillcorner():
  for x in corners:
    if ttt[tttboard.get(x)] == " ":
      return x

# block enemy
def block():
  for y in threeinrow:
    x = y.split()
    for w in x:
      w = int(w)
    if ttt[x[0]] + ttt[x[1]] + ttt[x[2]] == "oo ":
      return x[2]
    elif ttt[x[0]] + ttt[x[1]] + ttt[x[2]] == "o o":
      return x[1]
    elif ttt[x[0]] + ttt[x[1]] + ttt[x[2]] == " oo":
      return x[0]
    else:
      return ""

# form three
def make3():
  for y in threeinrow:
    x = y.split()
    for w in x:
      w = int(w)
    if ttt[x[0]] + ttt[x[1]] + ttt[x[2]] == "xx ":
      return x[2]
    elif ttt[x[0]] + ttt[x[1]] + ttt[x[2]] == "x x":
      return x[1]
    elif ttt[x[0]] + ttt[x[1]] + ttt[x[2]] == " xx":
      return x[0]
    else:
      return ""

# automatically move based on block and make3
def automove():
  if make3() != "":
    return make3()
  elif block() != "":
    return block()
  else:
    return randint(0,9)

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
  
  # print instructions + input (human) or calculate best move (computer)
  if playerid == 0:
    while 1:
      playstr = input("enter the column and then row of the cell you want to play in: (e.g. a1 for top left box) ")
      if playstr[0] in "abc" and playstr[1] in "123":
        break
  else:
    playstr = ""
    
    if starter = "computer":
      
      # start in corner on first move
      if round == 1:
        playstr = fillcorner()
        
      # conqcorners (round 3)
      elif round == 3 and ttt[4] == "o":
        conqcorners = True
        # if opposite corner is blank, fill it
        for x in range(4):
          if ttt[tttboard.get(corners[x])] == "x" and ttt[10-tttboard.get(corners[x])] == " ":
            playstr = corners[(x+2) % 4]
        # if opposite corner is not blank, fill another corner
        playstr = fillcorner()

      # conqcorners (round 5)
      elif round == 5 and conqcorners:
        playstr = fillcorner()

      # nob2 (round 3)
      elif round == 3 and o in ttt and ttt[4] != o:
        nob2 = True
        # put x in other corner such that row between two xs is "x x"
        for x in range(4):     
          if ttt[tttboard.get(corners[x])] == "x" and ttt[10-tttboard.get(corners[x])] == " ":
            playstr = corners[(x+2) % 4]

      # nob2 (round 5)
      elif round == 5 and nob2:
        # if human doesn't block potential three, form three and win
        if ttt[0] + ttt[4] + ttt[8] == "x x" or ttt[2] + ttt[4] + ttt[6] == "x x":
          playstr = 4
        # if human blocks potential three, put x in other corner such that three xs form a triangle with only one side blocked by o
        else:
          playstr = fillcorner()
          
      # nob2 (round 7)
      elif round == 7 and nob2:
        # human will probably try and block one of the potential threes
        # but regardless form three with other potential three and win
        playstr = automove()

      #if none of the above, automove
      else:
        playstr = automove()

    else: # if starter is human
      if round == 2:
        # if human plays center, play corner
        if ttt[4] == "o":
          playstr = fillcorner()
        # if human plays corner, play center
        elif "o" in ttt[1:8:2]:
          playstr = 4
        # secondedge (round 2)
        elif "o" in ttt[0:9:2]:
          #if human plays edge, play center
          secondedge = True
          playstr = 4
      # secondedge (round 4)
      elif round == 4 and secondedge and (ttt[1] + ttt[7] == "oo" or ttt[3] + ttt[5] == "oo"):
        #if human plays opposite edge, play corner
        fillcorner()
      
      # secondedge (round 6)
      elif round == 6 and secondedge:
        # play another corner
        fillcorner()
      
      else:
        playstr = automove()
            
  # add into ttt
  ttt = ttt[:tttboard.get(playstr)] + playerletter + tttboard.get(playstr)+1:]
    
  # check for win
  for x in threeinrow: #checks for every row combination
    if ttt[int(x[0])] != " " and ttt[int(x[0])] == ttt[int(x[1])] and ttt[int(x[1])] == ttt[int(x[2])]:
      print("\nwinner: " + ttt[int(x[0])])
      win = True
      break
  
  playerid += 1
  round += 1
  print("\n")
