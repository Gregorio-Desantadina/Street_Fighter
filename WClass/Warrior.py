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
        self.crouch = False
        self.attack_cooldown = 0
       

    def move(self, screen_width, screen_height, surface, target):
        SPEED = 20
        GRAVITY = 2
        attacking = False
        self.crouch = False
        dx = 0
        dy = 0

        key = pygame.key.get_pressed()

        #if self.attacking == False:

        #apply attack cooldown
        if self.attack_cooldown > 0:
           self.attack_cooldown -= 1
        
        #self.crouch
        if key[pygame.K_s]:
            self.crouch = True
            GRAVITY = 3
        else:
            self.crouch = False
            GRAVITY = 2

        #movement
        if (key[pygame.K_a] or key[pygame.K_d]) and self.crouch == False:
            if key[pygame.K_a]:
                dx = -SPEED
            if key[pygame.K_d]:
                dx = SPEED
        if (key[pygame.K_a] or key[pygame.K_d]) and self.crouch == True:
            if key[pygame.K_a]:
                dx = -SPEED/2
            if key[pygame.K_d]:
                dx = SPEED/2
        
        
        #jumping
        if self.tecla_presionada_W() and self.jump > 0:
            self.vel_y = -25
            self.jump -= 1


        #attack
        if (key[pygame.K_r] or key[pygame.K_t] or key[pygame.K_y]) and self.crouch==False and self.jump == 2:
            if key[pygame.K_r] and self.crouch==False:
                self.attack_type = 1
            if key[pygame.K_t] and self.crouch==False:
                self.attack_type = 2
            if key[pygame.K_y] and self.crouch==False:
                self.attack_type = 3
            self.attack(surface, target)
            
        #self.crouch attack
        if (key[pygame.K_r] or key[pygame.K_t] or key[pygame.K_y]) and self.crouch==True and self.jump == 2:
            if key[pygame.K_r] and self.crouch==True:
                self.attack_type = 4
            if key[pygame.K_t] and self.crouch==True:
                self.attack_type = 5
            if key[pygame.K_y] and self.crouch==True:
                self.attack_type = 6
            self.attack(surface, target)
        
        if (key[pygame.K_r] or key[pygame.K_t] or key[pygame.K_y]) and self.jump < 2:
            if key[pygame.K_r]:
                self.attack_type = 7
            if key[pygame.K_k]:
                self.attack_type = 8
            if key[pygame.K_y]:
                self.attack_type = 9
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
        if self.attack_cooldown == 0:
            if self.attack_type == 1 and self.energy >=10:
                attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
                self.energy -= 1
                self.attack_cooldown = 20
                if attacking_rect.colliderect(target.rect):
                    target.healt -= 10

                pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
            if self.attack_type == 2 and self.energy >=20:
                attacking_rect = pygame.Rect(self.rect.centerx - (3 * self.rect.width * self.flip), self.rect.y, 3 * self.rect.width, self.rect.height)
                self.energy -=20
                self.attack_cooldown = 40
                if attacking_rect.colliderect(target.rect):
                    target.healt -= 20
                pygame.draw.rect(surface, (0, 0, 0), attacking_rect)
        
            if self.attack_type == 4 and self.energy >=5:
                attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip) - 400 * (self.flip - 0.5) , self.rect.y * 1.125, 2 * self.rect.width, self.rect.height / 2)
                self.energy -=5
                self.attack_cooldown = 3
                if attacking_rect.colliderect(target.rect):
                    target.healt -=5
                    if target.energy >= 20:
                        target.energy -=10
                    else:
                        target.energy = 0
                pygame.draw.rect(surface, (255,255,255), attacking_rect)


            if self.attack_type == 7 and self.energy >=20:
                attacking_rect = pygame.Rect(self.rect.centerx - (1.5 * self.rect.width), self.rect.y / 1.25, 3 * self.rect.width, 2 * self.rect.height)
                self.energy -= 2
                self.attack_cooldown = 30
                if attacking_rect.colliderect(target.rect):
                    target.healt -= 10
                pygame.draw.rect(surface, (0,0,255), attacking_rect)
        
        if self.attack_type == 3:
            if self.energy < 100:
                self.energy += 1
                self.vel_y = 1
                

                
                
                

           

            


    def draw(self, surface):
        if self.crouch == False:
            pygame.draw.rect(surface, (255, 0, 0), self.rect)
        elif self.crouch == True:
            pygame.draw.rect(surface, (0, 255, 0), self.rect)
