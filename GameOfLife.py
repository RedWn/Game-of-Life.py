import random
import pygame as pyg

alive = set()

Window = 1000
nblock = 100
block = 10

nebs = [ [ 0 for y in range( nblock ) ] for x in range( nblock ) ]

change = True

def printGrid():
    """
    Creates and Updates the grid in the window
    """
    SCREEN.fill((31,32,35))
    for i in range(0,Window,block):
        for j in range(0,Window,block):
            rect = pyg.Rect(i,j,block,block)
            if (i/block,j/block) in alive:
                pyg.draw.rect(SCREEN, (200,200,200), rect, 0)
            pyg.draw.rect(SCREEN, (200,200,200), rect, 1)


def neb():
    """
    Fills the nebs matrix with the number of alive neighbors for each cell
    """
    ans = 0
    for x in range(1,nblock-1):
        for y in range(1,nblock-1):
            for i in range(-1,2):
                for j in range(-1,2):
                    if i == 0 and j == 0:
                        continue
                    if (x+i,y+j) in alive:
                        ans += 1
            nebs[x][y] = ans
            ans = 0

def GameOfLife():
    """
    The main function. this function decides who dies and who lives
    """
    notDone = False #for rare cases where the game reach a balanced or dead state with no further action
    neb()
    for i in range(1,nblock-1):
        for j in range(1,nblock-1):
            if (i,j) in alive:
                if nebs[i][j] >= 2 and nebs[i][j] <= 3:
                    continue
                alive.remove((i,j))
                notDone = True
            else:
                if nebs[i][j] == 3:
                    alive.add((i,j))
                    notDone = True
    return notDone

def init():
    """
    Initializer for PyGame and to create a random seed for the game
    """
    # for PyGame
    global SCREEN, CLOCK
    pyg.init()
    SCREEN = pyg.display.set_mode((Window,Window))
    CLOCK = pyg.time.Clock()
    SCREEN.fill((31,32,35))
    #for the seed
    for i in range (0, int((nblock*nblock)/3)):
        x = random.randrange(1,nblock-1)
        y = random.randrange(1,nblock-1)
        alive.add((x,y))

if __name__ == '__main__':
    init()
    # Main loop for the game
    while True:
        pyg.event.get() #Pygame crashes without this line
        pyg.display.update()
        if change:
            printGrid()
            change = False
        else:
            break
        change = GameOfLife()
