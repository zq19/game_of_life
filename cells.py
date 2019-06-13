import pygame
import sys


class Cell():

    def __init__(self,screen_width,screen_height,edge):
        self.worldx = int(screen_width / edge)
        self.worldy = int(screen_height / edge)
        self.cell = [[0 for i in range(self.worldx)] for i in range(self.worldy)]
