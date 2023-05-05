import pygame
from threading import Event
import time 


class Character():
    def __init__(self, player, x, y, SCREEN_WIDTH, SCREEN_HEIGHT, screen, projectiles):
        self.SPEED = 20
        self.player = player
        self.flip = False
        self.rect = pygame.Rect((x, y, 80, 100))
        self.vel_y = 0
        self.__jumps = 0
        self.__jumps_limit = 2
        self.__grounded = True
        self.__airbone = False
        self.dx = 0
        self.attacking = False
        self.attack_type = 0
        self.healt = 100
        self.energy = 100
        self.crouch = False
        self.move_cooldown = 0
        self.attack_cooldown = 0
        self.attack_cooldown1 = 0
        self.attack_cooldown2 = 0
        self.attack_cooldown3 = 0
        self.attack_cooldown4 = 0
        self.attack_cooldown5 = 0
        self.attack_cooldown6 = 0
        self.attack_cooldown7 = 0
        self.attack_cooldown8 = 0
        self.stun_all = 0
        self.xstun = 0
        self.ystun = 0
        self.stunbounce = 0
        self.dmgmult = 1
        self.projectiles = projectiles


    def is_grounded(self):
        return(self.__grounded)
    
    def is_airbone(self):
        return(self.__airbone)
    
    def has_jumps(self):
        return (self.__jumps >= 0 and self.__jumps < self.__jumps_limit)



    def jump(self, quantity = 1):
        ##if(self.has_jumps()):
        if self.__jumps < self.__jumps_limit:
            self.__jumps += quantity
            self.vel_y = -25
            self.__grounded = False
            self.__airbone = True

    def apply_attack_cooldown(self):
        if self.move_cooldown > 0:
            self.move_cooldown -=1
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

    def movement(self, screen_width, screen_height, surface, target, events):
        key = pygame.key.get_pressed()
        dy = 0
        GRAVITY = 2
        if self.player == 1 and self.stun_all == 0 and self.healt > 0:
        #self.crouch
            if key[pygame.K_s]:
                self.crouch = True
                GRAVITY = 3
            else:
                self.crouch = False
                GRAVITY = 2

            #movement
            if (key[pygame.K_a] or key[pygame.K_d]) and self.crouch == False and self.move_cooldown == 0:
                if key[pygame.K_a]:
                    self.dx = -self.SPEED
                if key[pygame.K_d]:
                    self.dx = self.SPEED
            if (key[pygame.K_a] or key[pygame.K_d]) and self.crouch == True and self.move_cooldown == 0:
                if key[pygame.K_a]:
                    self.dx = -self.SPEED/2
                if key[pygame.K_d]:
                    self.dx = self.SPEED/2
        
            if "w" in self.get_event_keys(events):
                self.jump()

           
            #attack
            if (key[pygame.K_r] or key[pygame.K_t] or key[pygame.K_y]) and self.crouch==False and self.__grounded == True and self.__airbone == False:
                if key[pygame.K_r] and self.crouch==False:
                    self.attack_type = 1
                    self.attack1(surface, target)
                if key[pygame.K_t] and self.crouch==False:
                    self.attack_type = 2
                    self.attack2(surface, target)
                if key[pygame.K_y] and self.crouch==False:
                    self.attack_type = 3
                    self.attack3(surface, target)
            
            #self.crouch attack
            if (key[pygame.K_r] or key[pygame.K_t] or key[pygame.K_y]) and self.crouch==True and self.__grounded == True and self.__airbone == False:
                if key[pygame.K_r] and self.crouch==True:
                    self.attack_type = 4
                    self.attack4(surface, target)
                if key[pygame.K_t] and self.crouch==True:
                    self.attack_type = 5
                    self.attack5(surface, target)
                if key[pygame.K_y] and self.crouch==True:
                    self.attack_type = 6
                    self.attack6(surface, target)
                
        
            if (key[pygame.K_r] or key[pygame.K_t] or key[pygame.K_y]) and self.__grounded == False and self.__airbone == True:
                if key[pygame.K_r]:
                    self.attack_type = 7
                    self.attack7(surface, target)
                if key[pygame.K_t]:
                    self.attack_type = 8
                    self.attack8(surface, target)
                if key[pygame.K_y]:
                    self.attack_type = 9
                    self.attack9(surface, target)
               

        elif self.player == 2 and self.stun_all == 0 and self.healt > 0:
            #self.crouch
            if key[pygame.K_DOWN]:
                self.crouch = True
                GRAVITY = 3
            else:
                self.crouch = False
                GRAVITY = 2

            #movement
            if (key[pygame.K_LEFT] or key[pygame.K_RIGHT]) and self.crouch == False and self.move_cooldown == 0:
                if key[pygame.K_LEFT]:
                    self.dx = -self.SPEED
                if key[pygame.K_RIGHT]:
                    self.dx = self.SPEED
            if (key[pygame.K_LEFT] or key[pygame.K_RIGHT]) and self.crouch == True and self.move_cooldown == 0:
                if key[pygame.K_LEFT]:
                    self.dx = -self.SPEED/2
                if key[pygame.K_RIGHT]:
                    self.dx = self.SPEED/2
        
        
            #jumping
            if "up" in self.get_event_keys(events):
                self.jump()
            #attack
            if (key[pygame.K_KP1] or key[pygame.K_KP2] or key[pygame.K_KP3]) and self.crouch==False and self.__grounded == True and self.__airbone == False:
                if key[pygame.K_KP1] and self.crouch==False:
                    self.attack_type = 1
                    self.attack1(surface, target)
                if key[pygame.K_KP2] and self.crouch==False:
                    self.attack_type = 2
                    self.attack2(surface, target)
                if key[pygame.K_KP3] and self.crouch==False:
                    self.attack_type = 3
                    self.attack3(surface, target)
            
            #self.crouch attack
            if (key[pygame.K_KP1] or key[pygame.K_KP2] or key[pygame.K_KP3]) and self.crouch==True and self.__grounded == True and self.__airbone == False:
                if key[pygame.K_KP1] and self.crouch==True:
                    self.attack_type = 4
                    self.attack4(surface, target)
                if key[pygame.K_KP2] and self.crouch==True:
                    self.attack_type = 5
                    self.attack5(surface, target)
                if key[pygame.K_KP3] and self.crouch==True:
                    self.attack_type = 6
                    self.attack6(surface, target)
               
        
            if (key[pygame.K_KP1] or key[pygame.K_KP2] or key[pygame.K_KP3]) and self.__grounded == False and self.__airbone == True:
                if key[pygame.K_KP1]:
                    self.attack_type = 7
                    self.attack7(surface, target)
                if key[pygame.K_KP2]:
                    self.attack_type = 8
                    self.attack8(surface, target)
                if key[pygame.K_KP3]:
                    self.attack_type = 9
                    self.attack9(surface, target)
            
        #Stun all
        if self.stun_all > 0:
            self.stun_all -=1
        #X movement while stun
        if self.xstun > 0:
            self.dx -= -self.xstun * self.stunbounce
            self.xstun -=1
            if self.rect.left + self.dx < 0:
                self.stunbounce = 1
            if self.rect.right + self.dx > screen_width:
                self.stunbounce = -1
                
        #Y movement while stun
        if self.ystun > 0:
            self.vel_y -= self.ystun
            self.ystun -=1
        

            


        #Apply gavity
        self.vel_y += GRAVITY
        dy += self.vel_y

        
        #player stay screen
        if self.rect.left + self.dx < 0:
            self.dx = -self.rect.left
        if self.rect.right + self.dx > screen_width:
            self.dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 110:
            self.vel_y = 0
            self.__jumps = 0
            self.__airbone = False
            self.__grounded = True
            dy = screen_height - 110 - self.rect.bottom

        #player face each other
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True  


        self.rect.x += self.dx
        self.rect.y += dy


    def update(self, screen_width, screen_height, surface, target, events):
        self.apply_attack_cooldown()
        self.movement(screen_width, screen_height, surface, target, events)
        GRAVITY = 2
        attacking = False
        self.crouch = False
        self.dx = 0
        key = pygame.key.get_pressed()
        

        #if self.attacking == False:
        

        
        



    def get_event_keys(self, events):
            keys = []
            for event in events:
                if event.type == pygame.KEYDOWN:

                    keys.append(pygame.key.name(event.key))
            return keys

    def tecla_presionada(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return pygame.key.name(event.key)

    def attack1(self, surface, target):
        if self.attack_cooldown == 0:
            if self.attack_type == 1 and self.energy >=10 and self.attack_cooldown1 == 0:
                attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
                self.energy -= 1
                self.attack_cooldown = 5
                self.attack_cooldown1 = 10
                if attacking_rect.colliderect(target.rect):
                    target.stun_all = 10
                    target.xstun = 20
                    target.ystun = 6
                    target.healt -= target.dmgmult *  3
                    target.stunbounce = -(self.flip -0.5) *2

                pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
    def attack2(self, surface, target):
        if self.attack_cooldown == 0:
            if self.attack_type == 2 and self.energy >=25 and self.attack_cooldown2 == 0:
                attacking_rect = pygame.Rect(self.rect.centerx - (3 * self.rect.width * self.flip), self.rect.y, 3 * self.rect.width, self.rect.height)
                self.energy -=25
                self.attack_cooldown = 5
                self.attack_cooldown2 = 30
                if attacking_rect.colliderect(target.rect):
                    target.healt -= target.dmgmult *  7
                    target.stun_all = 15
                    target.xstun = 30
                    target.ystun = 3
                    target.stunbounce = -(self.flip -0.5) *2
                pygame.draw.rect(surface, (200, 100, 25), attacking_rect)

    def attack4(self, surface, target):
        if self.attack_cooldown == 0:
            if self.attack_type == 4 and self.energy >=5 and self.attack_cooldown4 == 0:
                attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip) - 400 * (self.flip - 0.5) , self.rect.y * 1.125, 2 * self.rect.width, self.rect.height / 2)
                self.energy -=5
                self.attack_cooldown4 = 3

                if attacking_rect.colliderect(target.rect):
                    target.healt -= target.dmgmult * 2
                    target.attack_cooldown = 5
                    target.vel_y -= 5.5
                    target.jump = 0
                    if target.energy >= 3:
                        target.energy -=3
                    else:
                        target.energy = 0

                pygame.draw.rect(surface, (255,255,255), attacking_rect)

    def attack5(self, surface, target):
        if self.attack_cooldown == 0:
            if self.attack_type == 5 and self.energy >=3 and self.attack_cooldown5 == 0:
                attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip) + 80 * (self.flip - 0.5), self.rect.y, 2 * self.rect.width, self.rect.height)
                self.energy -= 3
                if self.flip == True:
                    self.dx =- 30
                elif self.flip == False:
                    self.dx =+ 30
                if attacking_rect.colliderect(target.rect):
                    self.attack_cooldown5 = 60
                    self.attack_cooldown = 10
                    target.healt -= target.dmgmult *  3
                    target.vel_y  -=30
                    target.stun_all = 31
                    target.xstun = 8
                    target.stunbounce = -(self.flip -0.5) *2
                pygame.draw.rect(surface, (255,0,255), attacking_rect)
    
    def attack6(self, surface, target):
        if self.attack_cooldown == 0:
            pass

    def attack7(self, surface, target):
        if self.attack_cooldown == 0:
            if self.attack_type == 7 and self.energy >=20 and self.attack_cooldown7 == 0:
                attacking_rect = pygame.Rect(self.rect.centerx - (1.5 * self.rect.width), self.rect.y / 1.25, 3 * self.rect.width, 2 * self.rect.height)
                self.energy -= 20
                self.attack_cooldown = 5
                self.attack_cooldown7 = 35
                if attacking_rect.colliderect(target.rect):
                    target.healt -= target.dmgmult *  5
                    target.stun_all = 11
                    target.xstun = 30
                    target.stunbounce = -(self.flip -0.5) *2
                pygame.draw.rect(surface, (0,0,255), attacking_rect)

    def attack8(self, surface, target):
        if self.attack_cooldown == 0:
            if self.attack_type == 8 and self.energy >=15 and self.attack_cooldown8 == 0:
                attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y / 1.23, 2 * self.rect.width, self.rect.height)
                self.energy -= 15
                self.attack_cooldown = 5
                self.attack_cooldown8 = 45
                self.vel_y = -25
                if attacking_rect.colliderect(target.rect):
                    target.healt -= target.dmgmult *  4   
                    target.stun_all = 35
                    target.xstun = 3
                    target.vel_y = -40
                    target.stunbounce = -(self.flip -0.5) *2
                pygame.draw.rect(surface, (0,0,255), attacking_rect)

    def attack9(self, surface, target):
        if self.attack_cooldown == 0:
            pass
        
    def attack3(self, surface, target):
        if self.attack_cooldown == 0:
            if self.attack_type == 3:
                if self.energy < 100:
                    self.energy += 2
                    self.vel_y = 1
            
    def damage_manager (self, damage, allstun, xstun, ystun, block, stunbounce):
        self.healt -=damage
        self.stun_all = allstun
        self.xstun = xstun
        self.vel_y = -ystun
        self.stunbounce = stunbounce

    def draw(self, surface):
        if self.crouch == False:
            pygame.draw.rect(surface, (255, 0, 0), self.rect)
        elif self.crouch == True:
            pygame.draw.rect(surface, (0, 255, 0), self.rect)
        if self.stun_all > 0:
            pygame.draw.rect(surface, (50, 255, 120), self.rect)