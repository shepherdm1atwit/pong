import pygame
class Ball:
    RADIUS = 7

    def __init__(self,x,y,vx,vy,screen,color,bgcolor):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.screen = screen
        self.color = color
        self.bgcolor = bgcolor
    def show(self, color):
        pygame.draw.circle(self.screen, color, (self.x, self.y), self.RADIUS)
    def update(self):
        self.show(self.bgcolor)
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.show(self.color)