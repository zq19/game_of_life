

class Cell():

    def __init__(self,screen_width,screen_height,edge):
        self.worldy = int(screen_width / edge)
        self.worldx = int(screen_height / edge)
        self.cell = [[0 for i in range(self.worldy)] for i in range(self.worldx)]

    def live_or_dead(self):
        new_cell_list = [[0 for i in range(self.worldy)] for i in range(self.worldx)]
        len_y = len(self.cell[0])
        len_x = len(self.cell)
        for i in range(len_x):
            for j in range(len_y):

                sum = self.cell_surround_count( i, j)
                if sum < 2 or sum > 3:
                    new_cell_list[i][j] = 0
                elif sum == 3:
                    new_cell_list[i][j] = 1
                else:
                    new_cell_list[i][j] = self.cell[i][j]
        return new_cell_list

    def is_on_edge(self, i, j):
        if i < 0:
            i = len(self.cell) - 1
        if i > len(self.cell) - 1:
            i = 0
        if j < 0:
            j = len(self.cell[0]) - 1
        if j > len(self.cell[0]) - 1:
            j = 0
        return [i, j]

    def cell_surround_count(self, i, j):
        count = 0
        for k in [i - 1, i, i + 1]:
            for g in [j - 1, j, j + 1]:
                if k == i and g == j:
                    continue
                fresh = self.is_on_edge( k, g)

                count += self.cell[fresh[0]][fresh[1]]
        return count



