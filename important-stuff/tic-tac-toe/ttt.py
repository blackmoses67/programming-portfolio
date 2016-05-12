# Tic Tac Toe

import pygame
import math
import game_mouse
import random
import datetime

BACKGROUND_COLOR        = (200, 200, 200, 200)
BUTTON_OUTLINE_COLOR    = (  0,   0,   0)
BUTTON_FILL_COLOR       = (255, 51, 153)
BUG_COLOR               = (86,195,86)
X_COLOR                 = (0,0,0)
O_COLOR                 = (200, 200, 200)
FONT_COLOR              = (255, 255, 0)

pygame.font.init()
myfont = pygame.font.SysFont("Arial", 100)

class GameBoard(game_mouse.Game):
    def __init__(self, width, height):
        game_mouse.Game.__init__(self, "Reflex tester", width, height, 10)
        self.label = myfont.render("", 1, (255,255,0))
        self.board = [0,0,0,0,0,0,0,0,0]
        self.turn = "x"
        self.pos = None
        self.end = False
        self.spot = pygame.Rect(10,10,0,0)
        return
        
    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
        x = mouse_position[0]
        y = mouse_position[1]
        
        self.end, message = game_end(self.board)
        if self.end:
            print message
            self.label = myfont.render(message, 1, FONT_COLOR, BACKGROUND_COLOR)
        
        if 1 in newbuttons:
            if self.end:
                self.label = myfont.render("", 1, (255,255,0))
                self.board = [0,0,0,0,0,0,0,0,0]
                self.turn = "s"
                self.pos = None 
            
            if not self.turn == 's':
                self.spot, self.pos = processClick(self.board, x, y, self.turn, 
                                     self.width, self.height)
            else:
                self.turn = "x"
        
        
    def paint(self, surface):
        if self.end:
            clearBackground(surface, self.width, self.height)
        else:
            drawWindow(surface, self.width, self.height, self.board)
            if self.turn == 's':
                pass#self.turn = 'x'
            elif self.pos != None and self.board[self.pos] == 0:
                drawXO(surface, self.width, self.height, self.turn,
                       self.pos, self.board)
                if self.turn == "x":
                    self.turn = "o"
                else:
                    self.turn = "x"
                self.pos = None
            for i in range(len(self.board)):
                drawXO(surface, self.width, self.height, self.board[i], i, self.board) 
        surface.blit(self.label, (self.width/2-150, self.height/2-50))
        return

def game_end(board):
    
    return False, "Not over yet"
      
def processClick(board, click_x, click_y, turn, width, height):
    pos = click_y/(height/3)*3 + click_x/(width/3)
    spot = pygame.Rect((pos%3)*(width/3)+(width/6)-50,
                       (pos/3)*(height/3)+(height/6)-50, 100, 100)
                       
    return spot, pos
    
def drawXO(surface, width, height, turn, square, board):
    spot = pygame.Rect((square%3)*(width/3)+(width/6)-50,
                       (square/3)*(height/3)+(height/6)-50, 100, 100)
    center_point = [(square%3)*(width/3)+(width/6),
                    (square/3)*(height/3)+(height/6)]
    cp = center_point
    if turn == "x":
        pygame.draw.rect(surface, X_COLOR, spot, 0)
        top_tri = [(cp[0]-25,cp[1]-50),(cp[0]+25,cp[1]-50),(cp[0],cp[1]-25)]
        left_tri = [(cp[0]-50,cp[1]-25),(cp[0]-25,cp[1]),(cp[0]-50,cp[1]+25)]
        bottom_tri = [(cp[0]-25,cp[1]+50),(cp[0]+25,cp[1]+50),(cp[0],cp[1]+25)]
        right_tri = [(cp[0]+50,cp[1]-25),(cp[0]+25,cp[1]),(cp[0]+50,cp[1]+25)]
        print top_tri
        pygame.draw.polygon(surface, BUTTON_FILL_COLOR, top_tri, 0)
        pygame.draw.polygon(surface, BUTTON_FILL_COLOR, left_tri, 0)
        pygame.draw.polygon(surface, BUTTON_FILL_COLOR, right_tri, 0)
        pygame.draw.polygon(surface, BUTTON_FILL_COLOR, bottom_tri, 0)
        board[square] = "x"
        
    if turn == "o":
        pygame.draw.circle(surface, O_COLOR, cp, 50, 0)
        pygame.draw.circle(surface, BUTTON_FILL_COLOR, cp, 25, 0)
        board[square] = "o"
        

def drawWindow(surface, width, height, board):
    clearBackground(surface, width, height)
    
    for x in range(3):
        for y in range(3):
            outline = pygame.Rect(x*(width/3), y*(height/3), (width/3), (height/3))
            pygame.draw.rect(surface, BUTTON_FILL_COLOR, outline, 0)
            pygame.draw.rect(surface, BUTTON_OUTLINE_COLOR, outline, 1)
    return


def clearBackground(surface, width, height):
    rect = pygame.Surface((width,height), pygame.locals.SRCALPHA)
    rect.fill(BACKGROUND_COLOR)
    surface.blit(rect, (width, height))
    return

def main():
    game = GameBoard(600, 600)
    game.main_loop()
    
if __name__ == "__main__":
    main()
 