import pygame
from WClass.Milk_Assets.Milk_effect_movement_2 import Milk_Effect

class spilled_milk(pygame.sprite.Sprite):
    def __init__(self, flip, x, y, target, user, projectiles):
        super().__init__()
        self.target = target
        self.image = pygame.Surface((200, 20))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()  ##pygame.Rect((x, y, 50, 10))
        self.rect.center = (x, y)
        self.impact = False
        self.user = user
        self.remove_projectile = False
        self.last_projectile_time = pygame.time.get_ticks()
        self.hit_timer = pygame.time.get_ticks()
        self.confused = None
        self.projectiles = projectiles

    def set_milk(self):
        self.milk_effect = Milk_Effect( self.target.rect.x +40, self.target.rect.y -80, self.target, self.user)

    def update(self, screen_width, screen_height, surface):
        if self.rect.colliderect(self.target.rect) and self.impact == False:
            self.target.damage_manager (1, 0, 0, 6, True, 1)
            self.impact = True
            self.hit_timer = pygame.time.get_ticks()
            self.set_milk()
            self.projectiles.add(self.milk_effect)
        if self.rect.colliderect(self.user.rect) and self.user.healt <= 99.95:
            self.user.healt += 0.075
        current_time = pygame.time.get_ticks()
        delay = 200
        if current_time - self.hit_timer > delay:
            self.impact = False
        if current_time - self.last_projectile_time > 5000:
            self.remove_projectile = True
        