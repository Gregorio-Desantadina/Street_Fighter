import pygame
from threading import Event

class Shield():
    def __init__(self, x, y, target, user, lvl):
        self.rect = pygame.Rect((x, y, 140, 120))
        self.level = lvl
        self.xposition = x
        self.yposition = y
        self.user = user
        self.target = target
        self.user = user
        self.timer = 30
    def move(self):
        if self.user.shield == 2:
            self.timer -=1
            if self.timer == 0:
                self.timer = 30
    
    def draw(self, surface):
        if self.user.shield == 2:
            pygame.draw.rect(surface, (200, 0, 0), self.rect)
        else:
            pygame.draw.rect(surface, (200, 55, 55), self.rect)
        