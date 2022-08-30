from functions import tictacboard, twoplayer

# main selection screen
while 1:
  playnow = input("enter '2player' to enter a 2-player game. \n")
  if playnow == "2player":
    twoplayer()
