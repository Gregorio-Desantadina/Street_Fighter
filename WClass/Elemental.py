import pygame
from WClass.BaseCharacter import Character
from WClass.ElementalAssets.Fire import fire
from WClass.ElementalAssets.Water import water

class Element (Character):
    def __init__(self, player, x, y, SCREEN_WIDTH, SCREEN_HEIGHT, screen, projectiles):
        super().__init__(player, x, y, SCREEN_WIDTH, SCREEN_HEIGHT, screen, projectiles)


    def set_element_fire(self, surface, target):
        self.element_fire = fire(self.flip - 0.5, self.rect.x + 15, self.rect.y + 30, target, self)

    def set_element_water(self, surface, target):
        self.element_water = water(self.flip - 0.5, self.rect.x + 15, self.rect.y + 30, target, self, self.projectiles)



    def attack1(self, surface, target):
        self.set_element_fire(surface, target)
        self.projectiles.add(self.element_fire)

    def attack2(self, surface, target):
        self.set_element_water(surface, target)
        self.projectiles.add(self.element_water)