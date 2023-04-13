import pygame
from threading import Event


class project():
    def __init__(self, flip, x, y, target, user):
        self.direct = flip * 2
        self.target = target
        self.rect = pygame.Rect((x, y, 50, 10))
        self.dx = 0
        self.SPEED = -25
        self.impact = False
        self.user = user

    def move(self, screen_width, screen_height, surface, target):
        if self.impact == False:
            self.dx = self.SPEED * self.direct
            self.rect.x += self.dx
            if self.rect.colliderect(self.target.rect):
                self.target.healt -= 3
                self.target.stun_all = 20
                self.target.xstun = 10
                self.target.ystun = 6
                target.stunbounce = -self.direct
                self.impact = True
                self.user.projectile = False
            if self.rect.left + self.dx < -50:
                self.impact = True
                self.user.projectile = False
            if self.rect.right + self.dx > screen_width + 50:
                self.impact = True
                self.user.projectile = False
                
        
        
    def draw(self, surface):
        pygame.draw.rect(surface, (200, 200, 0), self.rect)

