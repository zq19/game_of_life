import pygame
import sys


def change_color(screen,cell,setting):
    """根据新生成的细胞表信息更新生死细胞的颜色"""
    for i in range(len(cell.cell)):
        k = i
        k = (k+0.5) * setting.cell_edge
        for j in range(len(cell.cell[0])):
            g = j
            g = (g+0.5) * setting.cell_edge
            lid = cell.cell[i][j]*setting.live_cell_color
            pygame.draw.circle(screen, [lid*setting.red_number,
                lid*setting.green_number, lid*setting.blue_number],
                    (int(g), int(k)), setting.cell_edge//2)


def check_events(setting,button,state,cell1,screen):
    """监测鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            state.mouse_flag = True
            state.user_flag = True
        if event.type == pygame.MOUSEBUTTONUP:
            state.mouse_flag = False
            state.user_flag = False
        # 鼠标按下时，更改细胞的生死状态
        if state.mouse_flag:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            i = int(mouse_y/setting.cell_edge)
            j = int(mouse_x/setting.cell_edge)
            if state.user_flag:
                cell1.cell[i][j] = abs(cell1.cell[i][j] - 1)
                lid = cell1.cell[i][j]*setting.live_cell_color
                # 显示细胞状态
                pygame.draw.circle(screen, [lid*setting.red_number,
                    lid*setting.green_number, lid*setting.blue_number],
                    (int((j+0.5) * setting.cell_edge), int((i+0.5) * setting.cell_edge)),setting.cell_edge//2)
            check_paly_button(button, mouse_x, mouse_y, state)


def check_paly_button(button,mouse_x,mouse_y,state):
    "检查是否按下了play按钮"
    check_botton = button.rect.collidepoint(mouse_x,mouse_y)
    if check_botton and not state.active_flag:
        pygame.mouse.set_visible(True)
        state.active_flag = True
        pygame.mixer.music.load(".\images\water.mp3")
        pygame.mixer.music.play(100,0)


