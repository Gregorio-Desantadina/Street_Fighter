import pygame
from threading import Event
import time 

class Vamp():
    def __init__(self, player, x, y, SCREEN_WIDTH, SCREEN_HEIGHT, screen):
        self.player = player
        self.flip = False
        self.rect = pygame.Rect((x, y, 70, 90))
        self.vel_y = 0
        self.jump = 2
        self.dx = 0
        self.attacking = False
        self.fly = False
        self.attack_type = 0
        self.healt = 80
        self.energy = 120
        self.crouch = False
        self.attack_cooldown = 0
        self.attack_cooldown1 = 0
        self.attack_cooldown2 = 0
        self.attack_cooldown3 = 0
        self.attack_cooldown4 = 0
        self.attack_cooldown5 = 0
        self.attack_cooldown6 = 0
        self.attack_cooldown7 = 0
        self.attack_cooldown8 = 0

    def move(self, screen_width, screen_height, surface, target):
        SPEED = 17
        GRAVITY = 1.5
        attacking = False
        self.crouch = False
        self.dx = 0
        dy = 0

        key = pygame.key.get_pressed()

        #if self.attacking == False:
        
        #apply attack cooldown
        if self.attack_cooldown > 0:
           self.attack_cooldown -= 1
        if self.attack_cooldown1 > 0:
           self.attack_cooldown1 -= 1
        if self.attack_cooldown2 > 0:
           self.attack_cooldown2 -= 1
        if self.attack_cooldown3 > 0:
           self.attack_cooldown3 -= 1
        if self.attack_cooldown4 > 0:
           self.attack_cooldown4 -= 1
        if self.attack_cooldown5 > 0:
           self.attack_cooldown5 -= 1
        if self.attack_cooldown6 > 0:
           self.attack_cooldown6 -= 1
        if self.attack_cooldown7 > 0:
           self.attack_cooldown7 -= 1
        if self.attack_cooldown8 > 0:
           self.attack_cooldown8 -= 1

        if self.player == 1:
        #self.crouch
            if key[pygame.K_s] and self.fly == False:
                self.crouch = True
                GRAVITY = 3
            else:
                self.crouch = False
                GRAVITY = 2
            if key[pygame.K_s] and self.fly == True:
                dy = 15

            #movement
            if (key[pygame.K_a] or key[pygame.K_d]) and self.crouch == False:
                if key[pygame.K_a]:
                    self.dx = -SPEED
                if key[pygame.K_d]:
                    self.dx = SPEED
            if (key[pygame.K_a] or key[pygame.K_d]) and self.crouch == True:
                if key[pygame.K_a]:
                    self.dx = -SPEED/2
                if key[pygame.K_d]:
                    self.dx = SPEED/2
        
            if  (key[pygame.K_s]) and self.jump > 0 and self.fly == False:
                print(target.jump)
                self.vel_y = -25
                self.jump -= 1
            if (key[pygame.K_s]) and self.fly == True:
                self.vel_y = -15

           
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

        elif self.player == 2:
            #self.crouch
            if key[pygame.K_DOWN] and self.fly == False:
                self.crouch = True
                GRAVITY = 3
            elif self.fly == False:
                self.crouch = False
                GRAVITY = 2
            if key[pygame.K_s] and self.fly == True:
                self_vely = 15

            #movement
            if (key[pygame.K_LEFT] or key[pygame.K_RIGHT]) and self.crouch == False:
                if key[pygame.K_LEFT]:
                    self.dx = -SPEED
                if key[pygame.K_RIGHT]:
                    self.dx = SPEED
            if (key[pygame.K_LEFT] or key[pygame.K_RIGHT]) and self.crouch == True:
                if key[pygame.K_LEFT]:
                    self.dx = -SPEED/2
                if key[pygame.K_RIGHT]:
                    self.dx = SPEED/2
        
        
            #jumping
            """"
            if self.tecla_presionada() == "up"  and self.jump > 0:
                print(self.jump)
                self.vel_y = -25
                self.jump -= 1
            """
            if (key[pygame.K_UP]) and self.jump > 0 and self.fly == False:
                self.vel_y = -25
                self.jump -= 1
            elif (key[pygame.K_UP]) and self.fly == True:
                self.vel_y = -15


            #attack
            if (key[pygame.K_KP1] or key[pygame.K_KP2] or key[pygame.K_KP3]) and self.crouch==False and self.jump == 2:
                if key[pygame.K_KP1] and self.crouch==False:
                    self.attack_type = 1
                    if self.fly == True:
                        self.fly == False
                    if self.fly == False:
                        self.fly == True
                if key[pygame.K_KP2] and self.crouch==False:
                    self.attack_type = 2
                if key[pygame.K_KP3] and self.crouch==False:
                    self.attack_type = 3
                self.attack(surface, target)
            
            #self.crouch attack
            if (key[pygame.K_KP1] or key[pygame.K_KP2] or key[pygame.K_KP3]) and self.crouch==True and self.jump == 2:
                if key[pygame.K_KP1] and self.crouch==True:
                    self.attack_type = 4
                if key[pygame.K_KP2] and self.crouch==True:
                    self.attack_type = 5
                if key[pygame.K_KP3] and self.crouch==True:
                    self.attack_type = 6
                self.attack(surface, target)
        
            if (key[pygame.K_KP1] or key[pygame.K_KP2] or key[pygame.K_KP3]) and self.jump < 2:
                if key[pygame.K_KP1]:
                    self.attack_type = 7
                if key[pygame.K_KP2]:
                    self.attack_type = 8
                if key[pygame.K_KP3]:
                    self.attack_type = 9
                self.attack(surface, target)
        
        #Apply gavity
        while self.fly == False:
            self.vel_y += GRAVITY
            dy += self.vel_y

        
        #player stay screen
        if self.rect.left + self.dx < 0:
            self.dx = -self.rect.left
        if self.rect.right + self.dx > screen_width:
            self.dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 110:
            self.vel_y = 0
            self.jump = 2
            dy = screen_height - 110 - self.rect.bottom

        #player face each other
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True  


        self.rect.x += self.dx




    def draw(self, surface):
        if self.crouch == False and self.fly == False:
            pygame.draw.rect(surface, (255, 0, 0), self.rect)
        elif self.crouch == True:
            pygame.draw.rect(surface, (0, 255, 0), self.rect)
        if self.fly == True:
            pygame.draw.rect(surface, (0,255,255), self.rect)
