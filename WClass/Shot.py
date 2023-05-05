import pygame


class project(pygame.sprite.Sprite):
    def __init__(self, flip, x, y, target, user):
        super().__init__()
        self.direct = flip * 2
        self.target = target
        self.image = pygame.Surface((50, 10))
        self.image.fill((200, 200, 0))
        self.rect = self.image.get_rect()  ##pygame.Rect((x, y, 50, 10))
        self.rect.center = (x, y)
        self.dx = 0
        self.SPEED = -25
        self.impact = False
        self.user = user
        self.remove_projectile = False
        

    def update(self, screen_width, screen_height, surface):
        if self.impact == False:
            self.dx = self.SPEED * self.direct
            self.rect.x += self.dx
            if self.rect.colliderect(self.target.rect):
                self.impact = True
                self.user.projectile = False
            if self.rect.left + self.dx < -50:
                self.remove_projectile = True
                self.user.projectile = False
            if self.rect.right + self.dx > screen_width + 50:
                self.remove_projectile = True
                self.user.projectile = False
        else: 
            self.target.damage_manager (2, 16, 10, 10, True, -self.direct)
            self.remove_projectile = True

                
        


