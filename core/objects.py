import pygame

from core.constants import WHITE


class Paddle:
    COLOR = WHITE
    VEL = 4

    def __init__(self, x, y, width, height) -> None:
        self.x = self.original_X = x
        self.y = self.original_Y = y
        self.width = width
        self.height = height
    
    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))
    
    def move(self, up=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL
    
    def reset(self):
        self.x = self.original_X
        self.y = self.original_Y

class Ball:
    MAX_VEL = 7
    COLOR = WHITE

    def __init__(self, x, y, radius) -> None:
        self.x = self.original_X = x
        self.y = self.original_Y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0
    
    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)
    
    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel
    
    def reset(self):
        self.x = self.original_X
        self.y = self.original_Y
        self.y_vel = 0
        self.x_vel *= -1

if __name__ == '__main__':
    pass