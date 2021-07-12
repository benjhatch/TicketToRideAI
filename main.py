from Game.Board import Board

def main():
   board = Board()
   print()
   board.getConnections()
   print()

# Using the special variable 
# __name__
if __name__=="__main__":
    main()