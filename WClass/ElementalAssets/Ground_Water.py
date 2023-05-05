import pygame

class water_wave(pygame.sprite.Sprite):
    def __init__(self, flip, x, y, target, user):
        super().__init__()
        self.direct = flip * 2
        self.target = target
        self.image = pygame.Surface((40, 40))
        self.image.fill((40, 100, 200))
        self.rect = self.image.get_rect()  
        self.rect.center = (x, y)
        self.dx = 0
        self.SPEED = -10
        self.impact = False
        self.user = user
        self.remove_projectile = False
        self.activated = False
        self.attack_type = 0
        self.second_movement = False



    def update(self, screen_width, screen_height, surface):
        self.dx = self.SPEED * self.direct
        self.rect.x += self.dx
        if self.rect.colliderect(self.target.rect):
            self.target.damage_manager (0.1, 0, 9, 0, True, -self.direct)
        if self.rect.left + self.dx < -50:
            self.remove_projectile = True
            self.user.projectile = False
        if self.rect.right + self.dx > screen_width + 50:
            self.remove_projectile = True
            self.user.projectile = False