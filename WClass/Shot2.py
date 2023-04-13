import pygame
from threading import Event


class project2():
    def __init__(self, flip, x, y, target, user):
        self.direct = flip * 2
        self.target = target
        self.rect = pygame.Rect((x, y, 70, 90))
        self.dx = 0
        self.SPEED = 25
        self.impact = False
        self.user = user
        self.hit = False

    def move(self, screen_width, screen_height, surface, target):
        if self.impact == False:
            self.dx = self.SPEED * self.direct
            self.rect.x += self.dx
            if self.rect.colliderect(self.target.rect) and self.hit == False:
                self.target.healt -= 5
                self.target.stun_all = 20
                self.target.xstun = 20
                self.target.ystun = 1
                target.stunbounce = self.direct 
                self.hit = True
            if self.rect.left + self.dx < -50 and self.direct == 1:
                self.impact = True
                self.user.projectile2 = False
            if self.rect.right + self.dx > screen_width + 90 and self.direct == -1:
                self.impact = True
                self.user.projectile2 = False
                
        
        
    def draw(self, surface):
        pygame.draw.rect(surface, (55, 200, 255), self.rect)

