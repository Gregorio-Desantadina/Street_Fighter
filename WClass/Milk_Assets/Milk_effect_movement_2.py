from typing import Any
import pygame

class Milk_Effect(pygame.sprite.Sprite):
    def __init__(self, x, y, target, user):
        super().__init__()
        self.target = target
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()  ##pygame.Rect((x, y, 50, 10))
        self.rect.center = (x, y)
        self.impact = False
        self.user = user
        self.remove_projectile = False
        self.last_projectile_time = pygame.time.get_ticks()
        self.hit_timer = pygame.time.get_ticks()
        self.teclas_player1 = {
            'up':  'w',
            'down': pygame.K_s, 
            'left': pygame.K_a,
            'right': pygame.K_d,
            'attack1': pygame.K_r,
            'attack2': pygame.K_t, 
            'attack3': pygame.K_y,             
        }
        self.teclas_player2 = {
            'up':  'up',
            'down': pygame.K_DOWN, 
            'left': pygame.K_LEFT,
            'right': pygame.K_RIGHT,
            'attack1': pygame.K_KP1,
            'attack2': pygame.K_KP2, 
            'attack3': pygame.K_KP3,             
        }
        self.new_teclas_player1 = {
            'up':  's',
            'down': pygame.K_w, 
            'left': pygame.K_d,
            'right': pygame.K_a,
            'attack1': pygame.K_y,
            'attack2': pygame.K_r, 
            'attack3': pygame.K_t,             
        }
        self.new_teclas_player2 = {
            'up':  'down',
            'down': pygame.K_UP, 
            'left': pygame.K_RIGHT,
            'right': pygame.K_LEFT,
            'attack1': pygame.K_KP3,
            'attack2': pygame.K_KP1, 
            'attack3': pygame.K_KP2,             
        }


    def update(self, screen_width, screen_height, surface):
        self.rect.y = self.target.rect.y -80
        self.rect.x = self.target.rect.x +20
        current_time = pygame.time.get_ticks()
        if self.target.player == 1:
            self.target.movement_keys = self.new_teclas_player1
        else:
            self.target.movement_keys = self.new_teclas_player2
        if current_time - self.last_projectile_time > 3000:
            if self.target.player == 1:
                self.target.movement_keys = self.teclas_player1
            else:
                self.target.movement_keys = self.teclas_player2
            self.remove_projectile = True