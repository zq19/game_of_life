

class Setting():

    def __init__(self):
        # 游戏窗口设置
        self.screen_width = 1200
        self.screen_height = 700
        # 细胞的设置
        self.cell_edge = 10
        self.live_cell_color = 255
        self.dead_cell_color = 0
        # 3通道颜色分量
        self.red_number = 0.2
        self.green_number = 0.6
        self.blue_number = 0.2
        # 游戏帧率设置
        self.FPS = 60
