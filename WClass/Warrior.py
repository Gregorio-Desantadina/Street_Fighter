import pygame
from threading import Event
import time 

class Fighter():
    def __init__(self, x, y):
        self.flip = False
        self.rect = pygame.Rect((x, y, 80, 100))
        self.vel_y = 0
        self.jump = 2
        self.attacking = False
        self.attack_type = 0
        self.healt = 100
        self.energy = 100
       

    def move(self, screen_width, screen_height, surface, target):
        SPEED = 15
        GRAVITY = 2
        attacking = False
        dx = 0
        dy = 0

        key = pygame.key.get_pressed()

        #if self.attacking == False:
        
        #movement
        if key[pygame.K_a]:
            dx = -SPEED
        if key[pygame.K_d]:
            dx = SPEED
        
        #jumping
        if self.tecla_presionada_W() and self.jump > 0:
            self.vel_y = -25
            self.jump -= 1

        #attack
        if key[pygame.K_r] or key[pygame.K_t] or key[pygame.K_y]:
            self.attack(surface, target)
            if key[pygame.K_r]:
                self.attack_type = 1
            if key[pygame.K_t]:
                self.attack_type = 2
            if key[pygame.K_y]:
                self.attack_type = 3

        
        #Apply gavity
        self.vel_y += GRAVITY
        dy += self.vel_y

        
        #player stay screen
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 110:
            self.vel_y = 0
            self.jump = 2
            dy = screen_height - 110 - self.rect.bottom

        #player face each other
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True  


        self.rect.x += dx
        self.rect.y += dy

    def tecla_presionada_W(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    return True
        return False

    def attack(self, surface, target):
        self.attacking = True
        if self.attack_type == 1 and self.energy >10:
            attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
            self.energy -= 10
            if attacking_rect.colliderect(target.rect):
                target.healt -= 10

            pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
        if self.attack_type == 2 and self.energy >20:
            attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 3 * self.rect.width, self.rect.height)
            self.energy -=20
            if attacking_rect.colliderect(target.rect):
                target.healt -= 20
            pygame.draw.rect(surface, (0, 0, 0), attacking_rect)

        if self.attack_type == 3:
            while self.energy < 100:
                self.energy += 1

                
                
                

           

            


    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)