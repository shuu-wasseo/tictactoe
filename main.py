sys.path.insert(0, './functions')

from twoplayer import twoplayer
from tictacboard import tictacboard

# main selection screen
while 1:
  playnow = input("enter '2player' to enter a 2-player game. \n")
  if playnow == "2player":
    twoplayer()
