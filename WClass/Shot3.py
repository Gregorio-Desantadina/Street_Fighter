import pygame
from threading import Event


class project3(pygame.sprite.Sprite):
    def __init__(self, flip, x, y, target, user):
        super().__init__()
        self.direct = flip * 2
        self.target = target
        self.image = pygame.Surface((40, 40))
        self.image.fill((200, 200, 255))
        self.rect = self.image.get_rect()  ##pygame.Rect((x, y, 50, 10))
        self.rect.center = (x, y)
        self.dx = 0
        self.SPEED = -20
        self.impact = False
        self.user = user
        self.remove_projectile = False
        self.last_projectile_time = pygame.time.get_ticks()
        self.GRAVITY = 1
        self.vel_y = 0
        
        self.dy = 0
        

    def update(self, screen_width, screen_height, surface):
        if self.rect.bottom + self.dy < screen_height - 110:
            self.dx = self.SPEED * self.direct
            self.rect.x += self.dx
            self.SPEED -=2
            self.vel_y += self.GRAVITY
            self.dy += self.vel_y
            if self.rect.left + self.dx < -20:
                self.vel_y -= 10
                self.direct = -self.direct
            if self.rect.right + self.dx > screen_width +20:
                self.vel_y -= 10
                self.direct = -self.direct
        else:
            self.vel_y = 0
            self.SPEED = 0
            self.dy = screen_height - 110 - self.rect.bottom
            current_time = pygame.time.get_ticks()
            delay = 1000
            if current_time - self.last_projectile_time > delay:
                attacking_rect = pygame.Rect(self.rect.centerx - (1.5 * self.rect.width), self.rect.y - 40, 3 * self.rect.width,2 * self.rect.height)
                if attacking_rect.colliderect(self.target.rect):
                    self.target.damage_manager (15, 16, 10, 10, True, -self.direct)
                if attacking_rect.colliderect(self.user.rect):
                    self.user.damage_manager (15, 16, 10, 10, True, self.direct)
                pygame.draw.rect(surface, (0,0,255), attacking_rect)
                self.remove_projectile = True
                self.last_projectile_time = current_time
        self.rect.y += self.dy
                
        


