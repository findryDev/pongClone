from typing import SupportsAbs
import pygame
import os



class field:
    def __init__(self):
        self.WIDTH = 900
        self.HEIGHT = 500
        self.FPS = 60


class gameObject(field):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.rectWIDTH = self.WIDTH//10
        self.rectHEIGHT = self.HEIGHT//10
        self.rectPOSITION = (0, 0, self.rectWIDTH, self.rectHEIGHT)
        self.rectCOLOR = (255, 255, 0)

    def draw(self):
        pygame.draw.rect(self.window, self.rectCOLOR, self.rectPOSITION)
        pygame.display.update()


gameFiled = field()

WIN = pygame.display.set_mode((gameFiled.WIDTH, gameFiled.HEIGHT))
pygame.display.set_caption('PONG')

gameOBJ = gameObject(WIN)

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(gameFiled.FPS)
        for event in pygame.event.get():
            gameOBJ.draw()
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()




if __name__ == "__main__":
    main()


