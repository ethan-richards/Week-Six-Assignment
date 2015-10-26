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
    userIn = ""
    randomPopulate(world,h,w)
    display(world,h,w)
    
    userIn = input("Press a key, Q stops the program: ")
    while userIn != "Q":
        
        display(world,h,w)
        
        world = generation(world,h,w)
        
        userIn = input("Press a key, Q stops the program: ")
    print("Goodbye!")
    
def randomPopulate(world,h,w):
    for x in range(h):
        row = []
        for y in range(w):
            row.append(random.randint(0,1))
        world.append(row)
        
def populate(world,h,w):
    for x in range(h):
        row = []
        for y in range(w):
            row.append(0)
        world.append(row)  
            
def display(world,h,w):
    worldString = "" 
    for x in range(h):
        rowString =""
        for y in range(w):
            if world[x][y] == 0:
                rowString += " "
            else:
                rowString += "*"
             
        worldString += rowString + "\n"
    print(worldString)
        
    
    
def generation(world,h,w):
    newWorld = []
    populate(newWorld,h,w)
        
    for x in range(1,h-1):
        for y in range(1,w-1):
            n = 0
            n = world[x-1][y-1] +  \
                world[x-1][y] +  \
                world[x-1][y+1] +  \
                world[x][y-1] +  \
                world[x][y+1] +  \
                world[x+1][y-1] +  \
                world[x+1][y] +  \
                world[x+1][y+1]
            if world[x][y] == 0:
                if n == 3:
                    newWorld[x][y] = 1
                else:
                    newWorld[x][y] = 0
            
            else:
                if n == 3 or n ==2 :
                    newWorld[x][y] = 1
                else:
                    newWorld[x][y] = 0
    return newWorld
    
    
    

main()