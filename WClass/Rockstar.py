import pygame
from threading import Event
import time 
from WClass.rock_assests.shield import Shield

class Rock():
    def __init__(self, player, x, y, SCREEN_WIDTH, SCREEN_HEIGHT, screen, projectiles):
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
        self.attack_cooldown = 0
        self.attack_cooldown1 = 0
        self.attack_cooldown2 = 0
        self.attack_cooldown3 = 0
        self.attack_cooldown4 = 0
        self.attack_cooldown5 = 0
        self.attack_cooldown6 = 0
        self.attack_cooldown7 = 0
        self.attack_cooldown8 = 0
        self.attack_window1_1 = 0
        self.attack_window1_2 = 0
        self.attack_window2 = 0
        self.shield = 0
        self.wait_2 = 0
        self.i_2 = 0
        self.stun_all = 0
        self.xstun = 0
        self.ystun = 0
        self.stunbounce = 0
        self.dmgmult = 1
        self.heat = 0

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

    
    def get_event_keys(self, events):
            keys = []
            for event in events:
                if event.type == pygame.KEYDOWN:

                    keys.append(pygame.key.name(event.key))
            return keys
       

    def update(self, screen_width, screen_height, surface, target, events):
        SPEED = 18 + (self.heat / 13)
        GRAVITY = 2
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
        if self.attack_cooldown5 == 35:
            self.shield = 0
        if self.attack_cooldown6 > 0:
           self.attack_cooldown6 -= 1
        if self.attack_cooldown7 > 0:
           self.attack_cooldown7 -= 1
        if self.attack_cooldown8 > 0:
           self.attack_cooldown8 -= 1
        if self.attack_window1_1 > 0:
            self.attack_window1_1 -=1
        if self.attack_window1_2 > 0:
            self.attack_window1_2 -=1  
        if self.attack_window2 > 0:
            self.attack_window2 -=1   
        if self.heat > 0:
            self.heat -= 0.3
        
        if self.shield == 0:
            self.dmgmult = 1
        if self.shield == 1:
            self.dmgmult = 1.2        
        if self.shield == 2:
            self.dmgmult = 1.5

        self.shieldfire = Shield(self.rect.x - 30, self.rect.y - 20, target, self, self.shield)     
        if self.shield > 0:
            self.shieldfire.move()
            self.shieldfire.draw(surface)   

        
        
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
        
        if self.player == 1 and self.stun_all == 0 and self.healt > 0:
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
                    self.dx = -SPEED
                if key[pygame.K_d]:
                    self.dx = SPEED
            if (key[pygame.K_a] or key[pygame.K_d]) and self.crouch == True:
                if key[pygame.K_a]:
                    self.dx = -SPEED/2
                if key[pygame.K_d]:
                    self.dx = SPEED/2
        
            if "w" in self.get_event_keys(events):
                self.jump()

           
            #attack
            if (key[pygame.K_r] or key[pygame.K_t] or key[pygame.K_y]) and self.crouch==False and self.__grounded == True and self.__airbone == False:
                if key[pygame.K_r] and self.crouch==False:
                    self.attack_type = 1
                if key[pygame.K_t] and self.crouch==False:
                    self.attack_type = 2
                if key[pygame.K_y] and self.crouch==False:
                    self.attack_type = 3
                self.attack(surface, target)
            
            #self.crouch attack
            if (key[pygame.K_r] or key[pygame.K_t] or key[pygame.K_y]) and self.crouch==True and self.__grounded == True and self.__airbone == False:
                if key[pygame.K_r] and self.crouch==True:
                    self.attack_type = 4
                if key[pygame.K_t] and self.crouch==True:
                    self.attack_type = 5
                if key[pygame.K_y] and self.crouch==True:
                    self.attack_type = 6
                self.attack(surface, target)
        
            if (key[pygame.K_r] or key[pygame.K_t] or key[pygame.K_y]) and self.__grounded == False and self.__airbone == True:
                if key[pygame.K_r]:
                    self.attack_type = 7
                if key[pygame.K_t]:
                    self.attack_type = 8
                if key[pygame.K_y]:
                    self.attack_type = 9
                self.attack(surface, target)
               

        elif self.player == 2 and self.stun_all == 0 and self.healt > 0:
            #self.crouch
            if key[pygame.K_DOWN]:
                self.crouch = True
                GRAVITY = 3
            else:
                self.crouch = False
                GRAVITY = 2

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
            if "up" in self.get_event_keys(events):
                self.jump()


            #attack
            if (key[pygame.K_KP1] or key[pygame.K_KP2] or key[pygame.K_KP3]) and self.crouch==False and self.__grounded == True and self.__airbone == False:
                if key[pygame.K_KP1] and self.crouch==False:
                    self.attack_type = 1
                if key[pygame.K_KP2] and self.crouch==False:
                    self.attack_type = 2
                if key[pygame.K_KP3] and self.crouch==False:
                    self.attack_type = 3
                self.attack(surface, target)
            
            #self.crouch attack
            if (key[pygame.K_KP1] or key[pygame.K_KP2] or key[pygame.K_KP3]) and self.crouch==True and self.__grounded == True and self.__airbone == False:
                if key[pygame.K_KP1] and self.crouch==True:
                    self.attack_type = 4
                if key[pygame.K_KP2] and self.crouch==True:
                    self.attack_type = 5
                if key[pygame.K_KP3] and self.crouch==True:
                    self.attack_type = 6
                self.attack(surface, target)
        
            if (key[pygame.K_KP1] or key[pygame.K_KP2] or key[pygame.K_KP3]) and self.__grounded == False and self.__airbone == True:
                if key[pygame.K_KP1]:
                    self.attack_type = 7
                if key[pygame.K_KP2]:
                    self.attack_type = 8
                if key[pygame.K_KP3]:
                    self.attack_type = 9
                self.attack(surface, target)

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
            self.__grounded = True
            self.__airbone = False
            dy = screen_height - 110 - self.rect.bottom

        #player face each other
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True  


        self.rect.x += self.dx
        self.rect.y += dy


    def tecla_presionada(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return pygame.key.name(event.key)
    
    
    

    def attack(self, surface, target):
        self.attacking = True
        if self.attack_cooldown == 0:
            if self.attack_type == 1 and self.energy >=2:
                if self.attack_cooldown1 == 0: 
                    attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y -20, 2 * self.rect.width, self.rect.height * 1.20)
                    self.energy -= 2
                    self.attack_cooldown = 15
                    self.attack_cooldown1 = 40
                    if attacking_rect.colliderect(target.rect):
                        target.damage_manager(3 * self.dmgmult, 20, 6, 5, False, -(self.flip -0.5) *2)
                        self.attack_window1_1 = 20
                        self.attack_cooldown4 = 28
                    pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
                elif self.attack_window1_1 != 0 and self.attack_window1_2 == 0 and self.energy >=6:
                    attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y - 30, 2 * self.rect.width, self.rect.height * 1.30)
                    self.energy -= 3
                    self.attack_cooldown = 15
                    self.attack_cooldown1 = 40
                    if attacking_rect.colliderect(target.rect):
                        target.damage_manager(5 * self.dmgmult, 20, 5, -100, False, (self.flip -0.5) *2)
                        self.attack_window1_2 = 25
                        self.attack_cooldown4 = 28
                    pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
                elif self.attack_window1_2 != 0 and self.energy >=6:
                    attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
                    self.energy -= 4
                    self.attack_window1_2 = 0
                    if self.flip == True:
                        self.dx =- 10
                    elif self.flip == False:
                        self.dx =+ 10
                    if attacking_rect.colliderect(target.rect):
                        self.attack_cooldown = 10
                        self.attack_cooldown1 = 30
                        target.damage_manager(5 * self.dmgmult, 25, 20, 10, False, -(self.flip -0.5) *2)
                        self.attack_cooldown4 = 28
                    pygame.draw.rect(surface, (255,0,255), attacking_rect)


            if self.attack_type == 2 and self.energy >=25 and self.attack_cooldown2 == 0:
                attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y + 60, 2 * self.rect.width, self.rect.height * 0.5)
                if self.attack_window2 < self.heat / 2:
                    self.attack_window2 += 3
                elif self.attack_window2 >= self.heat / 2:
                    attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip) + 80 * (self.flip - 0.5), self.rect.y, 2 * self.rect.width, self.rect.height)
                    self.energy -= 15
                    self.attack_cooldown2 = 50
                    self.attack_cooldown = 20
                    self.vel_y = -30
                    self.__grounded = False
                    self.__airbone = True
                    self.__jumps = 1
                    if attacking_rect.colliderect(target.rect):
                        target.damage_manager(target.dmgmult * 5 + (self.heat / 3), 31, 10, 30, False, -(self.flip -0.5) *2)
                    pygame.draw.rect(surface, (255,0,255), attacking_rect)

                
        
            if self.attack_type == 4 and self.energy >=5 and self.attack_cooldown4 == 0:
                attacking_rect = pygame.Rect(self.rect.centerx -80, self.rect.y + 60, 2 * self.rect.width, self.rect.height * 0.5)
                self.energy -=2
                self.attack_cooldown4 = 1
                if self.heat < 100:
                    self.heat += 5
                self.dx = (60 + (self.heat / 3)) * -(self.flip - 0.5)
                if attacking_rect.colliderect(target.rect):
                    target.damage_manager(5 * self.dmgmult, 31, 27, 0, False, (self.flip -0.5) *2)
                    if self.heat < 80:
                        self.heat += 20
                    else:
                        self.heat = 100
                    self.attack_cooldown4 = 34

                pygame.draw.rect(surface, (255,255,255), attacking_rect)
            if self.attack_type == 5 and self.energy >=3 and self.attack_cooldown5 == 0:
                attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip) + 80 * (self.flip - 0.5), self.rect.y, 2 * self.rect.width, self.rect.height)
                self.energy -= 15
                self.attack_cooldown5 = 200
                self.attack_cooldown = 10
                self.shield = 1
                if attacking_rect.colliderect(target.rect):
                    self.shield = 2
                    target.damage_manager(target.dmgmult * 5 + (self.heat / 10), 31, 24, 3, False, -(self.flip -0.5) *2)
                pygame.draw.rect(surface, (255,0,255), attacking_rect)

            if self.attack_type == 7 and self.energy >=7 and self.attack_cooldown7 == 0:
                attacking_rect = pygame.Rect(self.rect.centerx -80, self.rect.y + 60, 2 * self.rect.width, self.rect.height)
                self.energy -= 7
                self.attack_cooldown = 5
                self.attack_cooldown7 = 15
                if attacking_rect.colliderect(target.rect):
                    self.__jumps = 1
                    self.vel_y = -20
                    target.damage_manager(3 * self.dmgmult, 11, 10, 0, False, -(self.flip -0.5) *2)
                    self.attack_window1_1 = 50
                pygame.draw.rect(surface, (0,0,255), attacking_rect)

            if self.attack_type == 8 and self.energy >=2 and self.attack_cooldown8 == 0:
                attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
                self.energy -= 2
                self.attack_cooldown = 2
                self.attack_cooldown8 = 2
                self.vel_y = 20
                if attacking_rect.colliderect(target.rect):
                    target.damage_manager(3 * self.dmgmult, 10, 3, -20, False, -(self.flip -0.5) *2)
                pygame.draw.rect(surface, (255,210,0), attacking_rect)
        
            if self.attack_type == 3:
                if self.energy < 100:
                    self.energy += 1 + self.heat / 75
                    self.vel_y = 1

    def damage_manager (self, damage, allstun, xstun, ystun, block, stunbounce):
        self.healt -=damage * self.dmgmult
        if self.attack_window2 == 0:
            if self.shield == 2 and block == False:
                self.stun_all = allstun * 0.6
                self.xstun = xstun * 0.8
                self.vel_y = -ystun * 0.8
            elif self.shield == 1:
                self.stun_all = allstun * 0.8
                self.xstun = xstun * 0.9
                self.vel_y = -ystun * 0.9
            if self.shield == 0:
                self.stun_all = allstun 
                self.xstun = xstun 
                self.vel_y = -ystun 
            self.stunbounce = stunbounce
            

    def draw(self, surface):
        if self.healt >= 0:
            if self.crouch == False:
                pygame.draw.rect(surface, (150 + + self.heat, 40, self.heat), self.rect)
            elif self.crouch == True:
                pygame.draw.rect(surface, (150 + self.heat, 80, self.heat), self.rect)
            if self.stun_all > 0:
                pygame.draw.rect(surface, (100 + self.heat, 13, 7 + self.heat), self.rect)
        else:
            if self.crouch == False:
                pygame.draw.rect(surface, (255, 0, 0), self.rect)
            elif self.crouch == True:
                pygame.draw.rect(surface, (0, 255, 0), self.rect)
            if self.stun_all > 0:
                pygame.draw.rect(surface, (50, 255, 120), self.rect)