import pygame
from threading import Event
from WClass.Shot import project 
from WClass.Shot2 import project2
from WClass.Shot3 import project3
from WClass.BaseCharacter import Character

class Cyber (Character):
    def __init__(self, player, x, y, SCREEN_WIDTH, SCREEN_HEIGHT, screen, projectiles):
        self.projectile = False
        self.projectile2 = False
        self.attack_window1_1 = 0
        self.attack_window1_2 = 0
        self.attack_window4_1 = 0
        self.attack_y4 = 0
        self.shot1 = None
        self.shot2 = None
        self.shot3 = None
        self.projectiles = projectiles
        super().__init__(player, x, y, SCREEN_WIDTH, SCREEN_HEIGHT, screen, projectiles)
        

    def set_projectile(self, target):
        self.shot1 = project(self.flip - 0.5, self.rect.x + 15, self.rect.y + 30, target, self)

    def set_projectile2(self, target, flip):
        if self.flip == False:
            self.shot2 = project2(self.flip - 0.5, 1010, self.rect.y , target, self)
        else:
            self.shot2 = project2(self.flip - 0.5, - 10, self.rect.y , target, self)

    def set_projectile3(self, target):
        self.shot3 = project3(self.flip - 0.5, self.rect.x + 15, self.rect.y + 30, target, self)

    def attack1(self, surface, target):
        if self.attack_cooldown == 0:
            if self.attack_type == 1 and self.energy >=2:
                if self.attack_cooldown1 == 0: 
                    attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y + 40, 2 * self.rect.width, self.rect.height * 0.60)
                    self.energy -= 2
                    self.attack_cooldown = 5
                    self.attack_cooldown1 = 40
                    if attacking_rect.colliderect(target.rect):
                        target.damage_manager (2, 10, 5, 3, False, -(self.flip -0.5) *2)
                        self.attack_window1_1 = 20
                    pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
                elif self.attack_window1_1 != 0 and self.attack_window1_2 == 0 and self.energy >=3:
                    attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y + 40, 2 * self.rect.width, self.rect.height * 0.60)
                    self.energy -= 3
                    self.attack_cooldown = 5
                    self.attack_cooldown1 = 40
                    if attacking_rect.colliderect(target.rect):
                        target.damage_manager (2, 10, 5, 3, False, -(self.flip -0.5) *2)
                        self.attack_window1_2 = 25
                    pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
                elif self.attack_window1_2 != 0 and self.energy >=6:
                    attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip) + 80 * (self.flip - 0.5), self.rect.y, 2 * self.rect.width, self.rect.height)
                    self.energy -= 6
                    self.attack_window1_2 = 0
                    if self.flip == True:
                        self.dx =- 60
                    elif self.flip == False:
                        self.dx =+ 60
                    if attacking_rect.colliderect(target.rect):
                        self.attack_cooldown = 10
                        self.attack_cooldown1 = 50
                        target.damage_manager (4, 25, 30, 10, False, -(self.flip -0.5) *2)
                    pygame.draw.rect(surface, (255,0,255), attacking_rect)

    def attack2(self, surface, target):
        if self.attack_cooldown == 0:
            if self.attack_type == 2 and self.energy >=8 and self.attack_cooldown2 == 0:
                attacking_rect = pygame.Rect(self.rect.centerx - (self.rect.width * self.flip), self.rect.y,self.rect.width, self.rect.height)
                self.energy -=8
                self.move_cooldown = 25
                self.attack_cooldown = 10
                self.attack_cooldown2 = 30
                self.xstun = 25
                self.stunbounce = (self.flip -0.5) *2
                if attacking_rect.colliderect(target.rect):
                    target.damage_manager (5, 15, 17, 7, False, -(self.flip -0.5) *2)
                pygame.draw.rect(surface, (200, 100, 25), attacking_rect)
        
    def attack4(self, surface, target):
        if self.attack_cooldown == 0:
            if self.attack_type == 4 and self.energy >=5 and self.attack_cooldown4 == 0:
                self.set_projectile2(target, self.flip)
                self.projectiles.add(self.shot2)
                self.energy -= 15
                self.projectile2 = True
                self.attack_cooldown = 3
                self.attack_cooldown4 = 60

    def attack5(self, surface, target):
        if self.attack_cooldown == 0:
            if self.attack_type == 5 and self.energy >=15: ##and self.projectile == False
                self.set_projectile(target)
                self.projectiles.add(self.shot1)
                self.energy -= 15
                self.projectile = True
                self.attack_cooldown = 10
            
    def attack7(self, surface, target):
        if self.attack_cooldown == 0:
            if self.attack_type == 7 and self.energy >=20 and self.attack_cooldown7 == 0:
                self.set_projectile3(target)
                self.projectiles.add(self.shot3)
                self.energy -= 15
                self.attack_cooldown7 = 20

    def attack8(self, surface, target):
        if self.attack_cooldown == 0:
            if self.attack_type == 8 and self.energy >=15 and self.attack_cooldown8 == 0:
                attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y / 1.23, 2 * self.rect.width, self.rect.height)
                self.energy -= 10
                self.attack_cooldown = 5
                self.attack_cooldown8 = 45
                self.vel_y = 25
                if attacking_rect.colliderect(target.rect):
                    target.damage_manager (4, 15, 3, -40, False, -(self.flip - 0.5) * 2)
                pygame.draw.rect(surface, (0,0,255), attacking_rect)
        
    def attack3(self, surface, target):
        if self.attack_cooldown == 0:
            if self.attack_type == 3:
                if self.energy < 100:
                    self.energy += 2
                    self.vel_y = 1
            if self.attack_type == 6 and self.attack_cooldown6 == 0:
                if self.energy >= 20:
                    if self.flip == True:
                        self.rect.x = target.rect.x - 100
                    else:
                        self.rect.x = target.rect.x + 100
                    self.energy -=20
                    self.attack_cooldown6 = 10
                    self.attack_cooldown = 0
                    self.attack_cooldown1 = 0
                    self.attack_cooldown2 = 0
                    self.attack_cooldown5 = 0
                    target.stun_all = 8


    def draw(self, surface):
        screen = surface
        if self.crouch == False:
            pygame.draw.rect(surface, (140, 0, 255), self.rect)
        elif self.crouch == True:
            pygame.draw.rect(surface, (100, 50, 255), self.rect)
        if self.stun_all > 0:
            pygame.draw.rect(surface, (50, 20, 30), self.rect)
        
        