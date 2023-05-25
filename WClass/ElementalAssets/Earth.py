import pygame 

class earth(pygame.sprite.Sprite):
    def __init__(self, flip, x, y, target, user, projectiles):
        super().__init__()
        self.projectiles = projectiles
        self.direct = flip * 2
        self.target = target
        self.image = pygame.Surface((40, 40))
        self.image.fill((40, 255, 100))
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
            if self.user.attack_type == 1:
                self.attack_type = 1
                self.activated = True
            if self.user.attack_type == 4:
                self.attack_type = 3
                self.activated = True
            if self.user.attack_type == 5:
                self.attack_type = 4
                self.activated = True
        elif self.activated == True:


            if self.attack_type == 1:
                if self.rect.bottom + self.rect.y <= screen_height +310:
                    self.dx = self.SPEED * self.direct
                    self.rect.x += self.dx
                    self.SPEED +=1
                    self.rect.y += 10
                    if self.rect.left + self.dx < -20:
                        self.rect.y += 10
                        self.direct = -self.direct
                    if self.rect.right + self.dx > screen_width +20:
                        self.rect.y += 10
                        self.direct = -self.direct
                else:
                    self.remove_projectile = True
       


            if self.attack_type == 3:
                if self.second_movement == False:
                    self.rect.y += 25
                if self.rect.y >= self.user.rect.y +20:
                    if self.user.healt >=95:
                        self.user.healt = 100
                    else:
                        self.user.healt += 5
                    self.remove_projectile = True

                    

            if self.attack_type == 4:
                if self.second_movement == False:
                    self.rect.y += 25
                if self.rect.bottom  > screen_height - 100:
                    self.second_movement = True
                if self.second_movement == True:
                    self.remove_projectile = True
                    attacking_rect = pygame.Rect(self.user.rect.centerx - (2 * self.user.rect.width * self.user.flip), self.user.rect.y, 2 * self.user.rect.width, self.user.rect.height)
                    if attacking_rect.colliderect(self.target.rect):
                        self.target.damage_manager (0.5, 20, 20, 0, True, self.direct)
                    pygame.draw.rect(surface, (40, 100, 255), attacking_rect)