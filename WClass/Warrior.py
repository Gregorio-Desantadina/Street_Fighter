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
        SPEED = 20
        GRAVITY = 2
        attacking = False
        crouch = False
        dx = 0
        dy = 0

        key = pygame.key.get_pressed()

        #if self.attacking == False:
        
        #crouch
        if key[pygame.K_s]:
            crouch = True
            GRAVITY = 3
        else:
            crouch = False
            GRAVITY = 2

        #movement
        if (key[pygame.K_a] or key[pygame.K_d]) and crouch == False:
            if key[pygame.K_a]:
                dx = -SPEED
            if key[pygame.K_d]:
                dx = SPEED
        if (key[pygame.K_a] or key[pygame.K_d]) and crouch == True:
            if key[pygame.K_a]:
                dx = -SPEED/2
            if key[pygame.K_d]:
                dx = SPEED/2
        
        
        #jumping
        if self.tecla_presionada_W() and self.jump > 0:
            self.vel_y = -25
            self.jump -= 1


        #attack
        if (key[pygame.K_r] or key[pygame.K_t] or key[pygame.K_y]) and crouch==False:
            if key[pygame.K_r] and crouch==False:
                self.attack_type = 1
            if key[pygame.K_t] and crouch==False:
                self.attack_type = 2
            if key[pygame.K_y] and crouch==False:
                self.attack_type = 3
            self.attack(surface, target)
            
        #crouch attack
        if (key[pygame.K_r] or key[pygame.K_t] or key[pygame.K_y]) and crouch==True:
            if key[pygame.K_r] and crouch==True:
                self.attack_type = 4
            if key[pygame.K_t] and crouch==True:
                self.attack_type = 5
            if key[pygame.K_y] and crouch==True:
                self.attack_type = 6
            self.attack(surface, target)
        
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
        if self.attack_type == 1 and self.energy >=10:
            attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
            self.energy -= 1
            if attacking_rect.colliderect(target.rect):
                target.healt -= 10

            pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
        if self.attack_type == 2 and self.energy >=20:
            attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 3 * self.rect.width, self.rect.height)
            self.energy -=20
            if attacking_rect.colliderect(target.rect):
                target.healt -= 20
            pygame.draw.rect(surface, (0, 0, 0), attacking_rect)

        if self.attack_type == 3:
            if self.energy < 100:
                self.energy += 1
                self.vel_y = 1
        
        if self.attack_type == 4 and self.energy >=5:
            attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip) + 300, self.rect.y * 1.125, self.rect.width, self.rect.height / 2)
            self.energy -=5
            if attacking_rect.colliderect(target.rect):
                target.healt -=5
                if target.energy >= 20:
                    target.energy -=10
                else:
                    target.energy = 0
            pygame.draw.rect(surface, (255,255,255), attacking_rect)
                

                
                
                

           

            


    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)