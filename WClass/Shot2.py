import pygame
from threading import Event


class project2(pygame.sprite.Sprite):
    def __init__(self, flip, x, y, target, user):
        super().__init__()
        self.direct = flip * 2
        self.target = target
        self.image = pygame.Surface((70, 90))
        self.image.fill((50, 200, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.dx = 0
        self.SPEED = 25 
        self.impact = False
        self.user = user
        self.hit = False
        self.remove_projectile = False

    def update(self, screen_width, screen_height, surface):
        if self.impact == False:
            self.dx = self.SPEED * self.direct
            self.rect.x += self.dx
            if self.rect.colliderect(self.target.rect) and self.hit == False:
                self.target.damage_manager (5, 20, 20, 1, True, self.direct)
                self.hit = True
            if self.rect.left + self.dx < -50 and self.direct == 1:
                self.impact = True
                self.user.projectile2 = False
                self.remove_projectile = True
            if self.rect.right + self.dx > screen_width + 90 and self.direct == -1:
                self.impact = True
                self.user.projectile2 = False
                self.remove_projectile = True
                
        
        
    

