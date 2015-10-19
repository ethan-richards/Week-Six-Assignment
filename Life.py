__author__ = "Ethan Richards" 
# CIS 125
#Life
# Life.py
#Simulates a game.
import random
def main():
    
    world = []
    h = 80
    w = 22

    populate(world,h,w)
    display(world,h,w)
    
    userIn = input("Press a key, Q stops the program: ")
    while userIn != "Q":
        
        display(world,h,w)
        
        generation(world,h,w)
        
        userIn = input("Press a key, Q stops the program: ")
    print("Goodbye!")
   #this function will populate the world 
def populate(world,h,w):
   
    pass
 #this function will display the world           
def display(world,h,w):
  
    pass
  #this function will create a new world for each generation and decide whether cells live or die  
def generation(world,h,w):
    pass

main()