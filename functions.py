import pygame
import sys

def is_on_edge(cells,h, w):
    "判断细胞是否位于边界"
    return cells[min(h, len(cells) - 1)][min(w,len(cells[0]) - 1)]

def get_surround_cells_count(cells, h, w):
    "统计细胞周围8个细胞的生死状态"
    nearby = [is_on_edge(cells,h + dy, w + dx) for dx in [-1, 0, 1]
              for dy in [-1, 0, 1] if not (dx == 0 and dy == 0)]
    return len(list(filter(lambda x: x == 255, nearby)))


def cell_new_state(cells,h, w):
    "更新细胞状态"
    count = get_surround_cells_count(cells,h, w)
    return 255 if count == 3 else 0 if count < 2 or count > 3 else cells[h][w]


def update_cells(cells):
    "返回所有细胞更新后的状态"
    cells = [[cell_new_state(cells,h, w) for w in range(len(cells[0]))]
                  for h in range(len(cells))]
    return cells

def change_color(screen,cell):
    for i in range(len(cell.cell)):
        k = i
        k = k * 10
        for j in range(len(cell.cell)):
            g = j
            g = g * 10
            lid = cell.cell[i][j]
            pygame.draw.rect(screen, [lid, lid, lid], (k, g, 10, 10), 0)

def check_exit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()



def check_events(cell_edge,button,state,cell1,screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            i = int(mouse_x/cell_edge)
            j = int(mouse_y/cell_edge)
            if not state.active_flag:
                state.user_flag = True
            cell1.cell[i][j] = abs(cell1.cell[i][j]-255)
            if  state.user_flag:
                cell1.cell[28][28] = 255
                cell1.cell[28][29] = 255
                cell1.cell[28][30] = 255
                cell1.cell[29][29] = 255
                cell1.cell[30][30] = 255
            lid = cell1.cell[i][j]
            pygame.draw.rect(screen, [lid, lid, lid], (i * 10, j * 10, 10, 10), 0)


            check_paly_button(button,mouse_x,mouse_y,state,cell1)

def check_paly_button(button,mouse_x,mouse_y,state,cell1):
    "检查是否按下了play按钮"
    check_botton = button.rect.collidepoint(mouse_x,mouse_y)
    if check_botton and not state.active_flag:
        pygame.mouse.set_visible(False)
        state.active_flag = True

        pygame.mixer.music.load(".\images\water.mp3")
        pygame.mixer.music.play(100,0)

def check_mouse(cell1,cell_edge,screen,state):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if  not state.active_flag:
                state.user_flag = True
                i = int(mouse_x/cell_edge)
                j = int(mouse_y/cell_edge)
                cell1.cell[i][j] = abs(cell1.cell[i][j]-255)
                lid = cell1.cell[i][j]
                pygame.draw.rect(screen, [lid, lid, lid], (i * 10, j * 10, 10, 10), 0)
