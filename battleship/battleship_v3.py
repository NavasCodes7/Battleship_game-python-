import os
class player(object):
    def __init__(self,name):
        self.name = name
        self.board = [["O","O","O","O","O"],
                      ["O","O","O","O","O"],
                      ["O","O","O","O","O"],
                      ["O","O","O","O","O"],
                      ["O","O","O","O","O"]
                     ]
        print name
        self.printboard()
        self.ship_row = int(raw_input("position ship row "))
        self.ship_col = int(raw_input("position ship col "))
        
    def printboard(self):
        for row in self.board:
            print " ".join(row)
        

    def attack(self,other):
        raw_input("")
        os.system("cls")
        
        print self.name
        other.printboard()
        self.row = int(raw_input("which row should i blast commander "))
        self.col = int(raw_input("what about column "))
        if self.row == other.ship_row and self.col == other.ship_col:
            other.board[self.row][self.col] = "T"
            other.printboard()
            print "excellent commander "+self.name+" !! you just bombed shit outa ur enemy"
            return True
        else:
            if self.row not in range(5) or self.col not in range(5):
                print " COME'ON man.. thats not even an ocean"
                self.attack(other)
                
            elif other.board[self.row][self.col] == "X":
                print "U kidding me... U killed all those fishes ages ago"
                self.attack(other)
            
            else:
                other.board[self.row][self.col] = "X"
                other.printboard()
                print "oops.. wrong location commander " + self.name                 
            return False
        
        
p1name = raw_input("player 1 , ur commanding name? ")
p1 = player(p1name)
os.system("cls")
p2name = raw_input("player 2 , ur commanding name? ")
p2 = player(p2name)
os.system("cls")
print "LET THE WAR BEGIN"

    
while True:
   
   p1v = p1.attack(p2)
   if p1v:
       print p1.name + " WINS"
       break
   
   p2v = p2.attack(p1)
   if p2v:
       print p2.name + " WINS"
       break

    
