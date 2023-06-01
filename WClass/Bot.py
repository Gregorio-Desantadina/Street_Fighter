import pygame
from threading import Event
from WClass.BaseCharacter import Character
from WClass.BotAssets.EarthQuake import stone

class Bot (Character):
    def __init__(self, player, x, y, SCREEN_WIDTH, SCREEN_HEIGHT, screen, projectiles, movement_keys):
        self.combo = False
        self.combo2 = False
        self.combo4 = False
        self.combo5 = False
        self.hit_count = 0
        self.first = False
        self.pressed_key = {
            1: pygame.K_t,
            2: pygame.K_KP2,
        }
        super().__init__(player, x, y, SCREEN_WIDTH, SCREEN_HEIGHT, screen, projectiles, movement_keys)
        self.name = "Bot"

    def set_stone(self, surface, target, orientation):
        if orientation == 0:
            self.stone = stone(self.flip - 0.5, self.rect.left, self.rect.y + 100, target, self, self.projectiles, -1, False)
        else:
            self.stone = stone(-self.flip - 0.5, self.rect.right, self.rect.y + 100, target, self, self.projectiles, 1, False)


    def attack1(self, surface, target):
        if self.attack_cooldown1 == 0 and self.attack_cooldown == 0 and self.energy >= 15:
            if self.attack_type == 1 and self.combo == False:
                attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip) + 80 * (self.flip - 0.5), self.rect.y, 2 * self.rect.width, self.rect.height)
                self.energy -= 15
                self.move_cooldown = 50
                self.attack_cooldown = 5
                if attacking_rect.colliderect(target.rect):
                    target.damage_manager (2, 10, 0, 0, False, -(self.flip -0.5) *2)
                    self.combo = True
                else:
                    self.move_cooldown = 5
                    self.attack_cooldown = 10
                    self.attack_cooldown1 = 30
                    self.attack_type = 0
                pygame.draw.rect(surface, (255,255,255), attacking_rect)
            if self.combo == True and self.attack_cooldown == 0:
                attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y + 40, 2 * self.rect.width, self.rect.height)
                self.energy -= 0.5
                self.attack_cooldown = 2
                self.hit_count += 1
                if attacking_rect.colliderect(target.rect):
                    target.damage_manager (0.3, 5, 0, 0, False, -(self.flip -0.5) *2)
                else:
                    self.attack_type = 0
                    self.move_cooldown = 0
                    self.combo = False
                pygame.draw.rect(surface, (255,255,255), attacking_rect)   
            if self.hit_count == 10 and self.combo == True:
                attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
                self.energy -= 1
                self.attack_cooldown1 = 60
                self.attack_cooldown = 10
                self.hit_count = 0
                self.combo = False
                self.attack_type = 0
                if attacking_rect.colliderect(target.rect):
                    target.damage_manager (2, 10, 30, 5, False, -(self.flip -0.5) *2)
                pygame.draw.rect(surface, (255,255,255), attacking_rect) 
        elif self.combo == False:
            self.attack_type = 0

    def attack2(self, surface, target):
        key = pygame.key.get_pressed()
        if self.energy >=8:
            if self.combo2 == False:
                self.move_cooldown = 15
                self.energy -=8
                self.last_time = pygame.time.get_ticks()
                self.combo2 = True
            current_time = pygame.time.get_ticks()
            delay = 500
            if current_time - self.last_time >= delay:
                if key[self.pressed_key[1 * self.player]]:
                    attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
                    if attacking_rect.colliderect(target.rect):
                        target.damage_manager (8, 25, 30, 10, False, -(self.flip -0.5) *2)
                    pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
                    self.attack_cooldown2 = 40
                    self.attack_type = 0
                    self.combo2 = False
                else:
                    attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y / 1.23, 2 * self.rect.width, self.rect.height)
                    if attacking_rect.colliderect(target.rect):
                        target.damage_manager (8, 25, 10, 40, False, -(self.flip -0.5) *2)
                    pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
                    self.attack_cooldown2 = 10
                    self.attack_type = 0
                    self.combo2 = False
        else:
            self.attack_type = 0


    def attack4(self, surface, target):
        key = pygame.key.get_pressed()
        if self.energy >= 9:
            if self.combo4 == False:
                self.move_cooldown = 15
                self.energy -=10
                self.first = False
                self.last_time = pygame.time.get_ticks()
                self.combo4 = True
            current_time = pygame.time.get_ticks()
            delay = 500
            delay2 = 1000
            if current_time - self.last_time >= delay:
                if self.vel_y == 0 and self.combo4 == True and self.first == False:
                    self.damage_manager (0, 0, 0, 34, False, -(self.flip -0.5) *2)
                    self.__grounded = False
                    self.__airbone = True
                    self.move_cooldown == 0
            if current_time - self.last_time >= delay + 450 and self.first == False:
                    self.damage_manager (0, 0, 0, -44, False, -(self.flip -0.5) *2)
                    self.first = True
            if self.first == True and self.vel_y == 0:
                self.move_cooldown = 10
                self.set_stone(surface, target, 0)
                self.projectiles.add(self.stone)
                self.set_stone(surface, target, 1)
                self.projectiles.add(self.stone)
                self.attack_type = 0
                self.combo4 = False
                self.first = False
        else:
            self.attack_type = 0
    
    def attack5(self, surface, target):
        key = pygame.key.get_pressed()
        if self.combo5 == False and self.energy >= 14:
            self.move_cooldown = 15
            self.energy -=8
            self.first = False
            self.last_time = pygame.time.get_ticks()
            self.combo5 = True
        current_time = pygame.time.get_ticks()
        delay = 500
        if current_time - self.last_time >= delay:
            if self.vel_y == 0 and self.combo5 == True and self.first == False:
                self.damage_manager (0, 0, 36, 20, False, -(self.flip -0.5) *2)
                self.move_cooldown = 20
                self.first = True
                self.__grounded = False
                self.__airbone = True
                self.move_cooldown == 36
            if self.vel_y == 0 and self.combo5 == True:
                pass
        if self.xstun >= 16:
                attacking_rect = pygame.Rect(self.rect.centerx - (self.rect.width * self.flip), self.rect.y,self.rect.width, self.rect.height)
                '''self.attack_cooldown = 10
                self.attack_cooldown2 = 30'''
                if attacking_rect.colliderect(target.rect):
                    target.damage_manager (0.3, 15, 17, 7, False, -(self.flip -0.5) *2)
                pygame.draw.rect(surface, (200, 100, 25), attacking_rect)
        elif self.first == True:
            self.attack_type = 0
            self.combo5 = False
            self.first = False
    
        

    def attack7(self, surface, target):
        if self.attack_cooldown ==0 and self.attack_cooldown7 == 0 and self.energy >=4:
            self.energy -=4
            attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y / 0.83, 2 * self.rect.width, self.rect.height)
            if attacking_rect.colliderect(target.rect):
                target.damage_manager (2, 10, 10, -15, False, -(self.flip -0.5) *2)
            pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
            self.attack_cooldown7 = 20
            self.attack_type = 10
            self.attack_type = 0
        else:
            self.attack_type = 0


    def damage_manager (self, damage, allstun, xstun, ystun, block, stunbounce):
        self.healt -=damage
        if self.move_cooldown == 0:
            self.stun_all = allstun
            self.xstun = xstun
            self.vel_y = -ystun
            self.stunbounce = stunbounce
        


    def draw(self, surface):
        screen = surface
        if self.crouch == False and self.move_cooldown == 0:
            pygame.draw.rect(surface, (150, 150, 150), self.rect)
        elif self.crouch == True and self.move_cooldown == 0:
            pygame.draw.rect(surface, (100, 50, 255), self.rect)
        if self.move_cooldown != 0:
            pygame.draw.rect(surface, (200, 200, 200), self.rect)
        if self.stun_all > 0:
            pygame.draw.rect(surface, (50, 20, 30), self.rect)

