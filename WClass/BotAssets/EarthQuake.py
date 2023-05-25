import pygame

class stone(pygame.sprite.Sprite):
    def __init__(self, flip, x, y, target, user, projectiles ,orientation, second):
        super().__init__()
        self.projectiles = projectiles
        self.orientation = orientation
        self.direct = flip * 2
        self.target = target
        self.image = pygame.Surface((100, 60))
        self.image.fill((200, 200, 0))
        self.rect = self.image.get_rect()  
        self.rect.center = (x, y)
        self.dx = 0
        self.SPEED = 5 * self.orientation
        self.impact = False
        self.user = user
        self.remove_projectile = False
        self.activated = False
        self.attack_type = 0
        self.second_movement = False
        self.second = second

    def set_stone(self, surface, target, orientation):
        if orientation == 0:
            self.stone = stone(self.direct, self.rect.left, self.rect.y + 100, target, self, self.projectiles, -1, True)
        else:
            self.stone = stone(-self.direct, self.rect.right, self.rect.y + 100, target, self, self.projectiles, 1, True)

    def update(self, screen_width, screen_height, surface):
        self.dx = self.SPEED 
        self.rect.x += self.dx
        if self.rect.y > screen_height - 140:
            self.rect.y -= 10
        elif self.rect.y > screen_height - 160:
            self.rect.y -= 5
            if self.activated == False and self.second == False:
                if self.orientation == -1:
                    self.set_stone(surface, self.target, 0)
                    self.projectiles.add(self.stone)
                else:
                    self.set_stone(surface, self.target, 1)
                    self.projectiles.add(self.stone)
                self.activated = True
        else:
            self.remove_projectile = True
            
        if self.rect.colliderect(self.target.rect) and self.impact == False:
            self.target.damage_manager (5, 16, 20, 10, True, self.orientation)
            self.impact = True

        
