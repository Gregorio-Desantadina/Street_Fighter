import pygame
from WClass.BaseCharacter import Character
from WClass.Milk_Assets.Milk_projectile import Milk_Sachet

class Milk (Character):
    def __init__(self, player, x, y, SCREEN_WIDTH, SCREEN_HEIGHT, screen, projectiles, movement_keys):
        self.projectile = False
        self.projectile2 = False
        self.shot1 = None
        self.shot2 = None
        self.shot3 = None
        self.projectiles = projectiles
        super().__init__(player, x, y, SCREEN_WIDTH, SCREEN_HEIGHT, screen, projectiles, movement_keys)
        self.name = "Milk"


    def set_projectile(self, target):
        self.shot1 = Milk_Sachet(self.flip - 0.5, self.rect.x + 40, self.rect.y + 30, target, self, self.projectiles)

    def attack5(self, surface, target):
        if self.energy >= 15 and self.attack_cooldown5 <= 0:
            self.energy -=15
            self.attack_cooldown5 = 60
            self.set_projectile(target)
            self.projectiles.add(self.shot1)
            self.attack_type = 0
        else:
            self.attack_type = 0