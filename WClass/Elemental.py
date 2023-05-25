import pygame
from WClass.BaseCharacter import Character
from WClass.ElementalAssets.Fire import fire
from WClass.ElementalAssets.Water import water
from WClass.ElementalAssets.Earth import earth

class Element (Character):
    def __init__(self, player, x, y, SCREEN_WIDTH, SCREEN_HEIGHT, screen, projectiles):
        super().__init__(player, x, y, SCREEN_WIDTH, SCREEN_HEIGHT, screen, projectiles)


    def set_element_fire(self, surface, target):
        self.element_fire = fire(self.flip - 0.5, self.rect.x + 15, self.rect.y + 30, target, self)

    def set_element_water(self, surface, target):
        self.element_water = water(self.flip - 0.5, self.rect.x + 15, self.rect.y + 30, target, self, self.projectiles)
    
    def set_element_earth(self, surface, target):
        self.element_earth = earth(self.flip - 0.5, self.rect.x + 15, self.rect.y + 30, target, self, self.projectiles)
    



    def attack1(self, surface, target):
        if self.energy >= 7 and self.attack_cooldown == 0 and self.attack_cooldown1 == 0:
            attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
            self.energy -= 7
            self.attack_cooldown = 10
            self.attack_cooldown1 = 20
            self.set_element_fire(surface, target)
            self.projectiles.add(self.element_fire)
            if attacking_rect.colliderect(target.rect):
                target.damage_manager (3, 8, 8, 8, False, -(self.flip -0.5) *2)
            pygame.draw.rect(surface, (255, 50, 0), attacking_rect)

    def attack2(self, surface, target):
        self.set_element_water(surface, target)
        self.projectiles.add(self.element_water)
    
    def attack4(self, surface, target):
        self.set_element_earth(surface, target)
        self.projectiles.add(self.element_earth)