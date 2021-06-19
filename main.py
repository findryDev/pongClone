import pygame

pygame.init()


class field:
    def __init__(self):
        self.WIDTH = 900
        self.HEIGHT = 500
        self.FPS = 60
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('PONG')

    def draw(self, left, right, boll):
        self.window.fill((0, 0, 0))
        pygame.draw.rect(self.window, (255, 255, 255), left)
        pygame.draw.rect(self.window, (255, 255, 255), right)
        pygame.draw.circle(self.window, (255, 255, 255),
                           (b.circleX, b.circleY),
                           b.circleRad,
                           b.circleWidth)
        pygame.display.flip()


class paddleLeft(field):
    def __init__(self):
        super().__init__()
        self.rectWIDTH = self.WIDTH//80
        self.rectHEIGHT = self.HEIGHT//5
        self.rectPOSITION = (0, 0)
        self.rectCOLOR = (255, 255, 255)
        self.absolutePosition = 0
        self.VEL = 10
        self.rect = pygame.draw.rect(self.window,
                                     self.rectCOLOR,
                                     pygame.Rect(
                                     self.rectPOSITION[0],
                                     self.rectPOSITION[1],
                                     self.rectWIDTH,
                                     self.rectHEIGHT))

    def liftUpRect(self):
        if self.rect.y > 0:
            self.rect.y -= 1 * self.VEL
        print(self.rect.y)

    def liftDownRect(self):
        _, height = self.window.get_size()
        if self.rect.y < height - self.rectHEIGHT:
            self.rect.y += 1 * self.VEL
        print(self.rect.y)


class paddleRight(field):
    def __init__(self):
        super().__init__()
        self.rectWIDTH = self.WIDTH//80
        self.rectHEIGHT = self.HEIGHT//5
        self.rectPOSITION = (self.WIDTH - self.WIDTH//80, 0)
        self.rectCOLOR = (255, 255, 255)
        self.absolutePosition = 0
        self.VEL = 10
        self.rect = pygame.draw.rect(self.window,
                                     self.rectCOLOR,
                                     pygame.Rect(
                                     self.rectPOSITION[0],
                                     self.rectPOSITION[1],
                                     self.rectWIDTH,
                                     self.rectHEIGHT))

    def liftUpRect(self):
        if self.rect.y > 0:
            self.rect.y -= 1 * self.VEL
        print(self.rect.y)

    def liftDownRect(self):
        _, height = self.window.get_size()
        if self.rect.y < height - self.rectHEIGHT:
            self.rect.y += 1 * self.VEL
        print(self.rect.y)


class boll(field):
    def __init__(self):
        super().__init__()
        self.circleX = self.WIDTH//2
        self.circleY = self.HEIGHT//2
        self.circleRad = 10
        self.circleCOLOR = (255, 255, 255)
        self.circleWidth = 10
        self.VEL = 10
        self.rect =pygame.draw.circle(self.window,
                                      self.circleCOLOR,
                                      (self.circleX, self.circleY),
                                      self.circleRad,
                                      self.circleWidth)

    def move(self):
        self.circleX += 1 * self.VEL


gameFiled = field()

pR = paddleRight()
pL = paddleLeft()
b = boll()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(gameFiled.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP]:
            pR.liftUpRect()
        if key_pressed[pygame.K_DOWN]:
            pR.liftDownRect()
        if key_pressed[pygame.K_q]:
            pL.liftUpRect()
        if key_pressed[pygame.K_a]:
            pL.liftDownRect()
        b.move()
        gameFiled.draw(pL.rect, pR.rect, b.rect)


if __name__ == "__main__":
    main()
