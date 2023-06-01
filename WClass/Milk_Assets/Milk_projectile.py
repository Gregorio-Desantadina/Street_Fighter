import pygame
import math
from threading import Event
from WClass.Milk_Assets.Milk_effect_movement import spilled_milk


class Milk_Sachet(pygame.sprite.Sprite):
    def __init__(self, flip, x, y, target, user, projectiles):
        super().__init__()
        self.direct = flip * 2
        self.target = target
        self.projectiles = projectiles
        self.image = pygame.Surface((40, 40))
        self.image.fill((200, 200, 255))
        self.rect = self.image.get_rect()  ##pygame.Rect((x, y, 50, 10))
        self.rect.center = (x, y)
        self.dx = 0
        self.SPEED = -12
        self.impact = False
        self.user = user
        self.remove_projectile = False
        self.last_projectile_time = pygame.time.get_ticks()
        self.GRAVITY = 1
        self.vel_y = -8
        self.dy = 0
        self.milk_project = None
        


    def set_milk(self):
        self.milk_project = spilled_milk(self.direct, self.rect.x, self.rect.y + 60, self.target, self.user, self.projectiles)

    def update(self, screen_width, screen_height, surface):
        if self.rect.bottom + self.dy < screen_height - 110:
            self.dx = self.SPEED * (self.direct * 2) 
            self.rect.x += self.dx
            self.dy += self.vel_y
            if self.vel_y <= 6:
                self.vel_y += self.GRAVITY + -self.vel_y * 0.3
            
            if self.rect.left + self.dx < -20:
                self.direct = -self.direct
            if self.rect.right + self.dx > screen_width +20:
                self.direct = -self.direct
        else:
            self.vel_y = 0
            self.SPEED = 0
            self.dy = screen_height - 110 - self.rect.bottom
            self.set_milk()
            self.projectiles.add(self.milk_project)
            self.remove_projectile = True
        self.rect.y += self.dy