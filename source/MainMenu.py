import pygame, math

class Main_Menu:

    def __init__(self, width, height):
        '''Starts the main menu screen'''
        self.screen = pygame.display.set_mode((width,height))
        self.screen_size = self.screen.get_size()
        # self.width = self.screen_size.x
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.screen_color = (255,255,255)
        self.screen.fill(self.screen_color)
        pygame.display.set_caption("Stroop Game")
        self.titleFont = pygame.font.Font("fonts/Square.ttf", 70)
        self.font = pygame.font.Font("fonts/Square.ttf", 30)
        self.text1 = self.titleFont.render("Stroop Game", 1, pygame.Color("black"))
        self.screen.blit(self.text1, (20,20))
        pygame.display.update()