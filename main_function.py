import pygame
import sys
from pygame.locals import *
from settings import Setting
import functions as lf
from cells import Cell
from buttons import Button
from game_state import GameState

setting = Setting()

state = GameState()
pygame.init()
screen = pygame.display.set_mode((setting.screen_width,setting.screen_height),0,32)
button = Button('./images/play.png',screen)
pygame.display.set_caption("GameofLife")
"下面的数字之后会变为参数"

cell1 = Cell(setting.screen_width,setting.screen_height,setting.cell_edge)
#"""
"这个是用来指定初始图形的"

#"""
while True:
    "更新cells状态"
    cell1.cell = lf.update_cells(cell1.cell)
    button.blitbutton(state)
    lf.check_events(setting.cell_edge, button, state,cell1,screen)
    if state.active_flag:
        screen.fill((0,0,0))
        lf.change_color(screen,cell1)
    pygame.display.flip()
    lf.check_exit()