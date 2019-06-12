def is_on_edge(cells,h, w):
    "判断细胞是否位于边界"
    return cells[min(h, len(cells) - 1)][min(w,len(cells[0]) - 1)]

def get_surround_cells_count(cells, h, w):
    "统计细胞周围8个细胞的生死状态"
    nearby = [is_on_edge(cells,h + dy, w + dx) for dx in [-1, 0, 1]
              for dy in [-1, 0, 1] if not (dx == 0 and dy == 0)]
    return len(list(filter(lambda x: x == 1, nearby)))


def cell_new_state(cells,h, w):
    "更新细胞状态"
    count = get_surround_cells_count(cells,h, w)
    return 1 if count == 3 else 0 if count < 2 or count > 3 else cells[h][w]


def update_cells(cells):
    "返回所有细胞更新后的状态"
    cells = [[cell_new_state(cells,h, w) for w in range(len(cells[0]))]
                  for h in range(len(cells))]
    return cells
