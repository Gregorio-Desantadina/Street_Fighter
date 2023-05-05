import pygame


class fire(pygame.sprite.Sprite):
    def __init__(self, flip, x, y, target, user):
        super().__init__()
        self.direct = flip * 2
        self.target = target
        self.image = pygame.Surface((40, 40))
        self.image.fill((200, 200, 0))
        self.rect = self.image.get_rect()  
        self.rect.center = (x, y)
        self.dx = 0
        self.SPEED = -25
        self.impact = False
        self.user = user
        self.remove_projectile = False
        self.activated = False
        self.attack_type = 0
        self.second_movement = False
    

    def update(self, screen_width, screen_height, surface):
        if self.activated == False:
            self.rect.y = self.user.rect.y -100
            self.rect.x = self.user.rect.x +20
            if self.user.attack_type == 2:
                self.attack_type = 2
                self.activated = True
            if self.user.attack_type == 4:
                self.attack_type = 3
                self.activated = True
            if self.user.attack_type == 5:
                self.attack_type = 4
                self.activated = True
        elif self.activated == True:
            if self.attack_type == 2:
                self.rect.y += 3
                self.dx = self.SPEED * self.direct
                self.rect.x += self.dx
                if self.rect.colliderect(self.target.rect):
                    self.target.damage_manager (0.5, 16, 10, 10, True, -self.direct)
                    self.impact = True
                    self.user.projectile = False
                if self.rect.left + self.dx < -50:
                    self.remove_projectile = True
                    self.user.projectile = False
                if self.rect.right + self.dx > screen_width + 50:
                    self.remove_projectile = True
                    self.user.projectile = False


            if self.attack_type == 3:
                if self.second_movement == False:
                    self.rect.y += 2
                if self.rect.y >= self.user.rect.y +20:
                    self.second_movement = True
                if self.second_movement == True:
                    self.dx = -14 * self.direct
                    self.rect.x += self.dx
                if self.rect.colliderect(self.target.rect) or self.rect.right + self.dx > screen_width +20 or self.rect.left + self.dx < -20:
                    self.remove_projectile = True
                    attacking_rect = pygame.Rect(self.rect.centerx - (1.5 * self.rect.width), self.rect.y - 40, 3 * self.rect.width,2 * self.rect.height)
                    if attacking_rect.colliderect(self.target.rect):
                        self.target.damage_manager (10, 16, 10, 10, True, -self.direct)
                    if attacking_rect.colliderect(self.user.rect):
                        self.user.damage_manager (10, 16, 10, 10, True, self.direct)
                    pygame.draw.rect(surface, (0,0,255), attacking_rect)
                    

            if self.attack_type == 4:
                if self.second_movement == False:
                    self.rect.y += 25
                if self.rect.bottom  > screen_height - 100:
                    self.second_movement = True
                if self.second_movement == True:
                    self.remove_projectile = True
                    attacking_rect = pygame.Rect(self.user.rect.centerx - (2 * self.user.rect.width * self.user.flip), self.user.rect.y, 2 * self.user.rect.width, self.user.rect.height)
                    if attacking_rect.colliderect(self.target.rect):
                        self.target.damage_manager (0.5, 6, 20, 0, True, -self.direct)
                    pygame.draw.rect(surface, (0, 255, 0), attacking_rect)