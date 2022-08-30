# prints a tic-tac-toe board, board takes a string argument filled with characters "o", "x" and " "
def tictacboard(oxb):
  board = f"""   1     2     3
      |     |     
a  {oxb[0]}  |  {oxb[1]}  |  {oxb[2]}  
 _____|_____|_____
      |     |     
b  {oxb[3]}  |  {oxb[4]}  |  {oxb[5]}  
 _____|_____|_____
      |     |     
c  {oxb[6]}  |  {oxb[7]}  |  {oxb[8]}  
      |     |     """
  return board
