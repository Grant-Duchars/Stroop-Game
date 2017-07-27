import pygame, math

class Main_Menu:

    def __init__(self, width, height):
        '''Starts the main menu screen'''
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width,height))
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.screen_color = (255,255,255)
        pygame.display.set_caption("Stroop Game")
        # Fonts
        self.titleFont = pygame.font.Font("fonts/Square.ttf", 70)
        self.font = pygame.font.Font("fonts/Square.ttf", 50)
        # Text
        self.text1 = self.titleFont.render("Stroop Game", 1, pygame.Color("black"))
        self.text2 = self.font.render("Play", 1, pygame.Color("black"))
        self.text3 = self.font.render("Settings", 1, pygame.Color("black"))
        self.text4 = self.font.render("Credits", 1, pygame.Color("black"))
     
    def runScreen(self):
        self.screen.fill(self.screen_color)
        self.screen.blit(self.text1, (85,100))
        self.screen.blit(self.text2, (85,500))
        self.screen.blit(self.text3, (85,550))
        self.screen.blit(self.text4, (85,600))
        pygame.display.update()