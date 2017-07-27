import pygame, sys
from source import MainMenu

class Main:

    def __init__(self):
        # Screen Settings
        self.width  = 600
        self.height = 800
        # Game clock
        self.clock = pygame.time.Clock()
        # 1 = Game, 2 = Main Menu, 3 = Settings, 4 = Credits
        self.currentScreen = 2

    def detectClick(self):
        self.mousePos = pygame.mouse.get_pos()
        return self.mousePos
        # print(self.mousePos)

    def runGame(self):
        '''Starts the game'''
        self.main_menu = MainMenu.Main_Menu(self.width,self.height)
        self.main_menu.runScreen()
        
        while True:
            self.clock.tick(10)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    sys.exit()
            if self.currentScreen == 1:
                pass
            elif self.currentScreen == 2:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.detectClick()[0] >= 87 and self.detectClick()[1] >= 500 and self.detectClick()[0] <= 195 and self.detectClick()[1] <= 540:
                        self.currentScreen = 1
                        print("Clicked Play")
                    if self.detectClick()[0] >= 87 and self.detectClick()[1] >= 550 and self.detectClick()[0] <= 290 and self.detectClick()[1] <= 590:
                        self.currentScreen = 3
                        print("Clicked Settings")
                    if self.detectClick()[0] >= 87 and self.detectClick()[1] >= 610 and self.detectClick()[0] <= 260 and self.detectClick()[1] <= 640:
                        self.currentScreen = 4
                        print("Clicked Credits")
            elif self.currentScreen == 3:
                pass
            elif self.currentScreen == 4:
                pass
            if pygame.mouse.get_pressed()[0] == 1:
                self.detectClick()

def main():
    pygame.init()
    main = Main()
    main.runGame()
main()