class Cell():

    def __init__(self, screen_width, screen_height, cell_edge):
        self.worldx = int(screen_width / cell_edge)
        self.worldy = int(screen_height / cell_edge)
        self.cellmat = [[0 for i in range(self.worldx)] for i in range(self.worldy)]

    def is_on_edge(self, h, w):
        "判断细胞是否位于边界"
        return self.cellmat[min(h, len(self.cellmat) - 1)][min(w, len(self.cellmat[0]) - 1)]

    def get_surround_cells_count(self, h, w):
        "统计细胞周围8个细胞的生死状态"
        nearby = [self.is_on_edge(self.cellmat, h + dy, w + dx) for dx in [-1, 0, 1]
                  for dy in [-1, 0, 1] if not (dx == 0 and dy == 0)]
        return len(list(filter(lambda x: x == 1, nearby)))

    def cell_new_state(self, h, w):
        "更新细胞状态"
        count = self.get_surround_cells_count(self.cellmat, h, w)
        return 1 if count == 3 else 0 if count < 2 or count > 3 else self.cellmat[h][w]

    def update_cells(self):
        "返回所有细胞更新后的状态"
        self.cellmat = [[self.cell_new_state(self.cellmat, h, w) for w in range(len(self.cellmat[0]))]
                 for h in range(self.cellmat)]
        return self.cellmat
