import pygame
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
cell1 = Cell(setting.screen_width,setting.screen_height,setting.cell_edge)
FPSClock=pygame.time.Clock()


while True:

    "更新cells状态"

    button.blitbutton(state)
    lf.check_events(setting, button, state,cell1,screen)
    # 游戏开始后，更新所有细胞状态
    if state.active_flag:
        screen.fill((setting.dead_cell_color,setting.dead_cell_color,setting.dead_cell_color))
        cell1.cell = cell1.live_or_dead()
        lf.change_color(screen,cell1,setting)
    pygame.display.flip()
    FPSClock.tick(setting.FPS)
