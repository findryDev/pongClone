import pygame
import random
import os
pygame.init()

directX = random.randint(0, 1)
directY = random.randint(0, 1)


class field:
    def __init__(self):
        self.WIDTH = 900
        self.HEIGHT = 500
        self.field_center = (self.WIDTH//2, self.HEIGHT//2)
        self.FPS = 60
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.background = pygame.transform.scale(pygame.image.load
                                                 (os.path.join
                                                  ("assets",
                                                   "background",
                                                   "industrial-background.jpg")
                                                  ),
                                                 (self.WIDTH, self.HEIGHT)
                                                 )
        pygame.display.set_caption('PONG')

    def draw(self, left, right, ball):
        self.window.fill((0, 0, 0))
        self.window.blit(self.background, (0, 0))
        pygame.draw.rect(self.window, left.paddle_color, left.shape_paddle)
        pygame.draw.rect(self.window, right.paddle_color, right.shape_paddle)
        pygame.draw.circle(self.window, ball.ball_color,
                           (ball.ball_x, ball.ball_y),
                           ball.ball_rad,
                           ball.ball_width)
        pygame.display.flip()


class paddle(field):
    def __init__(self, site):
        super().__init__()
        self.paddle_width = self.WIDTH//80
        self.paddle_hight = self.HEIGHT//5
        if site == "left":
            self.paddle_position = (0, 0)
        if site == "right":
            self.paddle_position = (self.WIDTH - self.WIDTH//80, 0)
        self.paddle_color = (0, 0, 0)
        self.paddle_absolut_position = 0
        self.paddle_vel = 10
        self.shape_paddle = pygame.draw.rect(self.window,
                                             self.paddle_color,
                                             pygame.
                                             Rect(self.paddle_position[0],
                                                  self.paddle_position[1],
                                                  self.paddle_width,
                                                  self.paddle_hight))
        self.up = False
        self.down = False

    def go_up(self):
        if self.shape_paddle.y > 0:
            self.shape_paddle.y -= 1 * self.paddle_vel
        self.up = True

    def go_down(self):
        _, height = self.window.get_size()
        if self.shape_paddle.y < height - self.paddle_hight:
            self.shape_paddle.y += 1 * self.paddle_vel
        self.down = True

    def if_paddle_in_place(self):
        self.up = False
        self.down = False


class ball(field):
    def __init__(self, paddle_right, paddle_left):
        super().__init__()
        self.ball_x = self.WIDTH//2
        self.ball_y = self.HEIGHT//2
        self.ball_rad = 10
        self.ball_color = (0, 0, 0)
        self.ball_width = 10
        self.ball_vel = 10
        self.ball_shape =pygame.draw.circle(self.window,
                                            self.ball_color,
                                            (self.ball_x, self.ball_y),
                                            self.ball_rad,
                                            self.ball_width)
        self.paddle_right = paddle_right
        self.paddle_left = paddle_left

    def checkCollideLeft(self):
        if self.paddle_left.shape_paddle.collidepoint(self.ball_x, self.ball_y):
            return True
        centerPt = pygame.math.Vector2(self.ball_x, self.ball_y)
        cornerPts = [self.paddle_left.shape_paddle.bottomleft,
                     self.paddle_left.shape_paddle.bottomright,
                     self.paddle_left.shape_paddle.topleft,
                     self.paddle_left.shape_paddle.topright]
        if [p for p in cornerPts if pygame.math.Vector2(p).distance_to(centerPt) <= self.ball_rad]:
            return True
        return False

    def checkCollideRight(self):
        if self.paddle_right.shape_paddle.collidepoint(self.ball_x, self.ball_y):
            return True
        centerPt = pygame.math.Vector2(self.ball_x, self.ball_y)
        cornerPts = [self.paddle_right.shape_paddle.bottomleft,
                     self.paddle_right.shape_paddle.bottomright,
                     self.paddle_right.shape_paddle.topleft,
                     self.paddle_right.shape_paddle.topright]
        if [p for p in cornerPts if pygame.math.Vector2(p).distance_to(centerPt) <= self.ball_rad]:
            return True
        return False

    def move(self):
        global directY
        global directX
        if directX == 0:
            self.ball_x += 1 * self.ball_vel
            if self.checkCollideRight():
                directX = 1
                if self.paddle_right.up:
                    self.ball_y += 1 * self.ball_vel * 10
                    if self.ball_y >= self.HEIGHT:
                        directY = 1
                elif self.paddle_right.down:
                    self.ball_y -= 1 * self.ball_vel * 10
                    #self.ball_shape.y -= 1 * self.ball_vel
                    if self.ball_y < 0:
                        directY = 0
                else:
                    pass
        elif directX == 1:
            self.ball_x -= 1 * self.ball_vel
            if self.checkCollideLeft():
                directX = 0
                if self.paddle_left.up:
                    self.ball_y += 1
                    if self.ball_y >= self.HEIGHT:
                        directY = 1
                elif self.paddle_left.down:
                    self.ball_y -= 1 * self.ball_vel
                    #self.ball_shape.y -= 1 * self.ball_vel
                    if self.ball_y < 0:
                        directY = 0
                else:
                    pass
        if self.ball_x < 0:
            self.ball_x = self.field_center[0]
            self.ball_y = self.field_center[1]
        if self.ball_x >= self.WIDTH:
            self.ball_x = self.field_center[0]
            self.ball_y= self.field_center[1]

        '''
        if directY == 0:
            self.ball_y += 1
            if self.ball_y >= self.HEIGHT:
                directY = 1
        elif directY == 1:
            self.ball_y -= 1 * self.ball_vel
            self.ball_shape.y -= 1 * self.ball_vel
            if self.ball_y < 0:
                directY = 0
        '''



gameFiled = field()

pR = paddle("right")
pL = paddle("left")
b = ball(pR, pL)


def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(gameFiled.FPS)
        gameFiled.window.blit(gameFiled.background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP]:
            pR.go_up()
        if key_pressed[pygame.K_DOWN]:
            pR.go_down()
        if key_pressed[pygame.K_q]:
            pL.go_up()
        if key_pressed[pygame.K_a]:
            pL.go_down()
        b.move()
        pL.if_paddle_in_place()
        pR.if_paddle_in_place()
        gameFiled.draw(pL, pR, b)


if __name__ == "__main__":
    main()
