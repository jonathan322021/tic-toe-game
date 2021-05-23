import random,time 
import pyinputplus
import datetime
import threading
#Goal of this project is to create a game that is one player can play with the computer.
class Game:
    """
    This class contain, information from the player, table
    """
    
    def __init__(self,game,simbol,player,position,table):
        self.simbol=simbol
        self.position=position
        self.player=player
        self.table=table
        self.game=game
    
    def print_Table(self):
        """
        Print the table to the screen
        """
        print("welcome to tic toe")
        print(self.table['top-left']+"     |       "+self.table["top-middle"]+"      |    "+self.table['top-right'])
        print("-----------------------")
        print(self.table['middle-left']+"     +       "+self.table["center"]+"     +    "+self.table["middle-right"])
        print("-----------------------")
        print(self.table['button-left']+"     |        "+self.table["button-middle"]+"     |   "+self.table["button-right"])

    def printing_Val(self,val):
        """
        this function will find, respect to sign , who is the winner either pc or player
        """
        if self.simbol==val:
            print(self.player+" won!!")
        else:
            print("PC wont")
        return "finish"

    def checkingwinner(self):
      """
      this function check for the winner, when the game is won,part need to be improved.
      """
       
      if (self.table['top-left']==self.table["top-middle"])&(self.table["top-middle"]==self.table["top-middle"]):
            return self.table['top-left']
            
      if (self.table['middle-left']==self.table["center"])&(self.table["center"]==self.table["right-middle"]):
            return self.table['middle-left']
            
      if (self.table['button-left']==self.table["button-middle"])&(self.table["button-middle"]==self.table["right-middle"]):
            return self.table['button-left']
            
      if (self.table['top-left']==self.table["center"])&(self.table["center"]==self.table["button-right"]):
            return self.table['top-left']
            
      if  (self.table['top-right']==self.table["center"])&(self.table["center"]==self.table["button-left"]):
            return self.table['top-left']
            
def playing_with_Pc(gameInfo):
    """
    This function will assign to the pc the sign that pc will use.
    """
    if gameInfo.simbol=="X" :
        pc_simbol="O"
    else:
        pc_simbol="X"
    return pc_simbol

def pc_choosing_position(position_list):
        """
        This will produce a random.move ment from pc, and also will check if this place to move is empty or not
        """
        max_ind=len(position_list)
        while True:
            pc_choose=random.randint(0,max_ind-1)
            if position_list[pc_choose]!="":
                return position_list[pc_choose]

def start_Game():
    """
    Function will start the game, print the positions on the table.
    """
    table={'top-left':"","top-middle":"","top-right":"",
           'middle-left':"","center":"","middle-right":"",
           'button-left':"","button-middle":"","button-right":"",
           }

    position_1=['top-left', 'top-middle', 'top-right',"middle-left","center"," middle-right","button-left","button-middle" ,"button-right"]
    user_input=pyinputplus.inputYesNo("Start a new game:",blank=False)
    counter=0
    if user_input.upper()=="YES":
    #Creating a object game.
       name=pyinputplus.inputStr("Please enter name ",blank=False)
       namegame=pyinputplus.inputStr("Please enter game-name ",blank=False)
       simbol=pyinputplus.inputMenu(['X', 'O'], lettered=True, numbered=False)
       position_user=pyinputplus.inputMenu(position_1, lettered=True, numbered=False)
       position_1.remove(position_user)
       game=Game(namegame,simbol,name,position_user,table)
       game.table[position_user]=game.simbol
       game.table[pc_choosing_position(position_1)]=playing_with_Pc(game)
       game.print_Table()
       
    #After the first input until the game has fishihed
    while True :
        value_forpc=pc_choosing_position(position_1)
        position_user=pyinputplus.inputMenu(position_1, lettered=True, numbered=False)
        position_1.remove(position_user)
        game.table[position_user]=game.simbol
        time.sleep(1)
        game.table[value_forpc]=playing_with_Pc(game)
        position_1.remove(value_forpc)
        game.print_Table()
        if counter >= 3:
            print(game.checkingwinner())
        counter=+1
            
print("Welcome to tic-toe-game")
print("")
print("top-left        |       top-middle        |      top-right")
print("-----------------------------------------------------------------")
print("middle-left     +       center            +      middle-right")
print("-----------------------------------------------------------------")
print("button-left     |        button-middle    |      button-right")
print("")
start_Game()

      


    
 
   
    

 
    
        
            
        
            
            
       
        
        


            
            
        
        












        
    
