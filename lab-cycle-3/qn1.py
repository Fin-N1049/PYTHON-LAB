from itertools import count
from timeit import repeat
import pygame,sys
import numpy as np

pygame.init()

WIDTH=600
HEIGHT=800
LINE_WIDTH=25
WINDOW_COL=1
WINDOW_ROW=4
BOARD_ROWS = 3
BOARD_COLS = 3
CIRCLE_RADIUS = 50
CIRCLE_WIDTH = 10
CROSS_WIDTH = 15
SPACE = 55
RED = (255,0,0)
CIRCLE_COLOUR = (120,120,120)
LINE_COLOUR=(232,232,232)
BG_COLOUR=(200,200,200)

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill( BG_COLOUR )

board = np.zeros((BOARD_ROWS,BOARD_COLS))
window=np.zeros((WINDOW_ROW,WINDOW_COL))
global win

def draw_lines():
   #horizontal
    pygame.draw.line(screen, LINE_COLOUR, (20,200), (580,200),LINE_WIDTH )
    pygame.draw.line(screen, LINE_COLOUR, (20,400), (580,400),LINE_WIDTH )
   #vertical
    pygame.draw.line(screen, LINE_COLOUR, (200,15), (200,590),LINE_WIDTH )
    pygame.draw.line(screen, LINE_COLOUR, (400,15), (400,590),LINE_WIDTH )
   #borders
    pygame.draw.line(screen, LINE_COLOUR, (0,10), (600,10),25)
    pygame.draw.line(screen, LINE_COLOUR, (10,0), (10,600),25 )

    pygame.draw.line(screen, LINE_COLOUR, (590,10), (590,600),25)
    pygame.draw.line(screen, LINE_COLOUR, (0,600), (600,600),25)
    rec=pygame.draw.rect(screen, CIRCLE_COLOUR, pygame.Rect(50, 650, 200, 100))
    font = pygame.font.SysFont('Arial', 35)
    screen.blit(font.render('Restart', True, (0,0,0)), ((85,685) ))
    pygame.display.update()

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle( screen,CIRCLE_COLOUR,(int( col*200+100),#
                          int(row*200+110)),CIRCLE_RADIUS,CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line( screen,CIRCLE_COLOUR,(col*200+SPACE,#
                                   row*200+200-SPACE),(col*200+200-SPACE,#
                                   row*200+SPACE),CROSS_WIDTH)
                pygame.draw.line( screen,CIRCLE_COLOUR,(col*200+SPACE,#
                                row*200+SPACE),(col*200+200-SPACE,#
                                 row*200+200-SPACE),CROSS_WIDTH)


def mark_square(row,col,player):
    board[row][col] = player

def available_square(row,col):
    #print(board[row][col])
    if board[row][col] == 0:
        return True
    else:
        return False

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    #status()
    return True

def check_win(player):
    #vertical check
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col,player)
            return True

    #horizontal check
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row,player)
            return True

    #asc diagonla check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True

    #desc Diagonal check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True

    return False


def draw_vertical_winning_line(col,player):
    posX = col * 200 + 100
    
    if player == 1:
        colour = RED
        print("O WINS")
    elif player == 2:
        colour = RED
        print("X WINS")
    win=1
    pygame.draw.line(screen, CIRCLE_COLOUR,(posX,35),(posX,600-30),10)
    

def draw_horizontal_winning_line(row,player):
    posY = row * 200 + 100

    if player == 1:
        print("O WINS")
    elif player == 2:
        print("X WINS")
    win=1

    pygame.draw.line(screen,CIRCLE_COLOUR,(35,posY),(600-30,posY),10)



def draw_asc_diagonal(player):
    if player == 1:
        print("O WINS")
    elif player == 2:
        print("X WINS")
    pygame.draw.line(screen,CIRCLE_COLOUR,(35,600-35),(600-35,35),10)
    win=1

def draw_desc_diagonal(player):
    if player == 1:
       print("O WINS")
    elif player == 2:
       print("X WINS")
    pygame.draw.line(screen,CIRCLE_COLOUR,(35,35),(600-35,600-35),10)
    win=1

def status():
    if win == "X":
        print("X WINS")
    elif win == "O":
        print("O WINS")
    


def check_outside(row,col):
    if  (row>=50 and row<=250)and (col>=650 and col<=750):
        #print("Entered2")
        return True
    else:
        return False

def restart():
    screen.fill( BG_COLOUR)
    draw_lines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS): 
            board[row][col] = 0

draw_lines()



player = 1
win=0
game_over = False



mouseX = 0
mouseY = 0
count = 0
while True:
    for event in pygame.event.get():
    

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY //200)
            clicked_col = int(mouseX // 200)
            #print(clicked_row)
            #print(WINDOW_ROW)
            #print(clicked_row  != WINDOW_ROW-1)

           
            if clicked_row  != WINDOW_ROW-1:
                if available_square(clicked_row,clicked_col):
               
                    if player == 1:
                        mark_square( clicked_row,clicked_col,1)
                        if check_win(player):
                            game_over = True
                        player = 2
                    elif player ==2:
                        mark_square( clicked_row,clicked_col,2)
                        if check_win(player):
                            game_over = True
                        player = 1

                    draw_figures()
                    if game_over == True and count == 0:
                        status()
                 
                
            elif event.type == pygame.MOUSEBUTTONDOWN :
                #print("Entered")
                #print(mouseX," ",mouseY)
                if check_outside(mouseX,mouseY):
                    #print("Get restart")
                    restart()
                    game_over=False

       
        pygame.display.update()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False
        
        if event.type == pygame.QUIT:
            sys.exit()
        
    pygame.display.update()