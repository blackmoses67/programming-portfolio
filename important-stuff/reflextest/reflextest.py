#
# Reflex Test on a 3x3 board
#

import pygame
import math
import game_mouse
import random
import datetime

BACKGROUND_COLOR        = (200, 200, 200)
BUTTON_OUTLINE_COLOR    = (  0,   0,   0)
BUTTON_FILL_COLOR       = (255, 51, 153)
BUG_COLOR               = (86,195,86)

class GameBoard(game_mouse.Game):
    def __init__(self, width, height):
        game_mouse.Game.__init__(self, "Reflex tester", width, height, 10)
        
        self.board = [0,0,0,0,0,0,0,0,0]
        self.timeclock = 0
        self.timer = 0
        self.random_wait = random.randint(20,50)
        self.bug = False
        self.bugpos = random.randrange(9)
        self.spot = pygame.Rect(10,10,0,0)
        return
        
    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
        x = mouse_position[0]
        y = mouse_position[1]
        
        self.timeclock += 1
        self.timer += 1
        if self.bug and self.timeclock%50 == 0:
            self.bug = False
        elif self.timeclock%self.random_wait == 0:
            self.bug = True
            self.timer = 0
            self.bugpos = random.randrange(9)
            self.random_wait = random.randint(50,150)
            
        if 1 in newbuttons:
            self.spot = processClick(self.board, x, y, self.bug, self.bugpos,
                                     self.width, self.height, self.timer)
        
    def paint(self, surface):
        drawWindow(surface, self.width, self.height, self.board)
        if self.bug:
            drawBug(surface, self.width, self.height, self.bugpos, self.board)
        return
        
def processClick(board, click_x, click_y, bug, bugpos, width, height,timer):
    print "ProcessClick", click_x, click_y, bug, bugpos, width, height
    
    if bug:
        spot = pygame.Rect((bugpos%3)*(width/3)+(width/6)-20,
                           (bugpos/3)*(height/3)+(height/6)-20, 40, 40)
        if spot.collidepoint(click_x, click_y):
            print "You smashed the bug!!!, it took,", timer, "cycles"
    else:
        spot = pygame.Rect(10,10,0,0)
    return spot
    
    

def drawBug(surface, width, height, square, board):
    pygame.draw.circle(surface, BUG_COLOR, [(square%3)*(width/3)+(width/6),
                                            (square/3)*(height/3)+(height/6)],
                                            20,0)
    return
    
def drawTest(surface, spot):
    pass

def drawWindow(surface, width, height, board):
    clearBackground(surface, width, height)
    
    for x in range(3):
        for y in range(3):
            outline = pygame.Rect(x*(width/3), y*(height/3), (width/3), (height/3))
            pygame.draw.rect(surface, BUTTON_FILL_COLOR, outline, 0)
            pygame.draw.rect(surface, BUTTON_OUTLINE_COLOR, outline, 1)
    return


def clearBackground(surface, width, height):
    rect = pygame.Rect(0, 0, width, height)
    surface.fill(BACKGROUND_COLOR, rect)
    return

def main():
    game = GameBoard(600, 600)
    game.main_loop()
    
if __name__ == "__main__":
    main()



    