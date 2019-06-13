import pygame


class Button():

    def __init__(self,location,screen):

        self.image = pygame.image.load(location)
        self.screen = screen
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        "按钮初始位置"
        self.rect.top = self.screen_rect.top
        self.rect.left = self.screen_rect.left

    def blitbutton(self,state):
        if state.active_flag == False:
            self.screen.blit(self.image,self.rect)
            pygame.mouse.set_visible(True)


