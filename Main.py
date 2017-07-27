import pygame, sys
from source import MainMenu

class Main:

    def __init__(self):
        # Screen Settings
        self.width  = 600
        self.height = 800
        # Game clock
        self.clock = pygame.time.Clock()
    
    def runGame(self):
        '''Starts the game'''
        self.main_menu = MainMenu.Main_Menu(self.width,self.height)
        self.clock.tick
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    sys.exit()

def main():
    pygame.init()
    main = Main()
    main.runGame()
main()