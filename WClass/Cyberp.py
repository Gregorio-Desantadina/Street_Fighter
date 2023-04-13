import pygame
from threading import Event
import time 
from WClass.Shot import project 
from WClass.Shot2 import project2





class Cyber():
    def __init__(self, player, x, y, SCREEN_WIDTH, SCREEN_HEIGHT, screen):
        self.screen = screen
        self.screenHeight = SCREEN_HEIGHT
        self.screenWidth = SCREEN_WIDTH
        self.player = player
        self.flip = False
        self.rect = pygame.Rect((x, y, 80, 100))
        self.vel_y = 0
        self.__jumps = 0
        self.__jumps_limit = 2
        self.__grounded = True
        self.__airbone = False
        self.dx = 0
        self.dmgmult = 1
        self.projectile = False
        self.projectile2 = False
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
        self.attack_window1_1 = 0
        self.attack_window1_2 = 0
        self.attack_window4_1 = 0
        self.attack_y4 = 0
        self.stun_all = 0
        self.xstun = 0
        self.ystun = 0
        self.stunbounce = 0
        self.shot1 = None
        self.shot2 = None
       

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

    def set_projectile(self, target):
        self.shot1 = project(self.flip - 0.5, self.rect.x + 15, self.rect.y + 30, target, self)

    def set_projectile2(self, target, flip):
        if self.flip == False:
            self.shot2 = project2(self.flip - 0.5, self.screenWidth + 10, self.rect.y , target, self)
        else:
            self.shot2 = project2(self.flip - 0.5, - 80, self.rect.y , target, self)

    
    def get_event_keys(self, events):
            keys = []
            for event in events:
                if event.type == pygame.KEYDOWN:

                    keys.append(pygame.key.name(event.key))
            return keys
    

    
    def move(self, screen_width, screen_height, surface, target, events):
        SPEED = 20
        GRAVITY = 2
        attacking = False
        self.crouch = False
        self.dx = 0
        dy = 0


        key = pygame.key.get_pressed()

        #if self.attacking == False:
        
        #apply attack cooldown
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
        if self.attack_window1_1 > 0:
            self.attack_window1_1 -=1
        if self.attack_window1_2 > 0:
            self.attack_window1_2 -=1  
        if self.attack_window4_1 > 0:
            self.attack_window4_1 -=1
        if self.attack_window4_1 == 0:
            SPEED = 20
            self.attack_y4 = 0
        elif self.attack_window4_1 == 1:
            self.attack_cooldown4 = 20
            self.attack_cooldown = 20
        else:
            SPEED = 0
        

        if self.projectile == True:
            self.shot1.move(self.screenWidth, self.screenHeight, self.screen, target)
            self.shot1.draw(surface)
        if self.projectile2 == True:
            self.shot2.move(self.screenWidth, self.screenHeight, self.screen, target)
            self.shot2.draw(surface)
            

        
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
        
        if self.player == 1 and self.stun_all == 0:
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
                    self.dx = -SPEED
                if key[pygame.K_d]:
                    self.dx = SPEED
            if (key[pygame.K_a] or key[pygame.K_d]) and self.crouch == True and self.move_cooldown == 0:
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
               

        elif self.player == 2 and self.stun_all == 0:
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
                    self.dx = -SPEED
                if key[pygame.K_RIGHT]:
                    self.dx = SPEED
            if (key[pygame.K_LEFT] or key[pygame.K_RIGHT]) and self.crouch == True and self.move_cooldown == 0:
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


    def tecla_presionada(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return pygame.key.name(event.key)
    
    
    

    def attack(self, surface, target):
        self.attacking = True
        if self.attack_cooldown == 0:
            if self.attack_type == 1 and self.energy >=2:
                if self.attack_cooldown1 == 0: 
                    attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y + 40, 2 * self.rect.width, self.rect.height * 0.60)
                    self.energy -= 2
                    self.attack_cooldown = 5
                    self.attack_cooldown1 = 40
                    if attacking_rect.colliderect(target.rect):
                        target.stun_all = 10
                        target.xstun = 5
                        target.ystun = 3
                        target.healt -= 2
                        target.stunbounce = -(self.flip -0.5) *2
                        self.attack_window1_1 = 20
                    pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
                elif self.attack_window1_1 != 0 and self.attack_window1_2 == 0 and self.energy >=3:
                    attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y + 40, 2 * self.rect.width, self.rect.height * 0.60)
                    self.energy -= 3
                    self.attack_cooldown = 5
                    self.attack_cooldown1 = 40
                    if attacking_rect.colliderect(target.rect):
                        target.stun_all = 10
                        target.xstun = 5
                        target.ystun = 3
                        target.healt -= 2
                        target.stunbounce = (self.flip -0.5) *2
                        self.attack_window1_2 = 25
                    pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
                elif self.attack_window1_2 != 0 and self.energy >=6:
                    attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip) + 80 * (self.flip - 0.5), self.rect.y, 2 * self.rect.width, self.rect.height)
                    self.energy -= 6
                    self.attack_window1_2 = 0
                    if self.flip == True:
                        self.dx =- 60
                    elif self.flip == False:
                        self.dx =+ 60
                    if attacking_rect.colliderect(target.rect):
                        self.attack_cooldown = 10
                        self.attack_cooldown1 = 50
                        target.healt -= 4
                        target.vel_y  -=10
                        target.stun_all = 25
                        target.xstun = 30
                        target.stunbounce = -(self.flip -0.5) *2
                    pygame.draw.rect(surface, (255,0,255), attacking_rect)


            if self.attack_type == 2 and self.energy >=8 and self.attack_cooldown2 == 0:
                attacking_rect = pygame.Rect(self.rect.centerx - (self.rect.width * self.flip), self.rect.y,self.rect.width, self.rect.height)
                self.energy -=8
                self.move_cooldown = 25
                self.attack_cooldown = 10
                self.attack_cooldown2 = 30
                self.xstun = 25
                self.stunbounce = (self.flip -0.5) *2
                if attacking_rect.colliderect(target.rect):
                    target.healt -= 5
                    target.stun_all = 15
                    target.xstun = 10
                    target.ystun = 7
                    target.stunbounce = -(self.flip -0.5) *2
                pygame.draw.rect(surface, (200, 100, 25), attacking_rect)
        
            if self.attack_type == 4 and self.energy >=5 and self.attack_cooldown4 == 0:
                self.set_projectile2(target, self.flip)
                self.energy -= 15
                self.projectile2 = True
                self.attack_cooldown = 3
                self.attack_cooldown4 = 60

                
            if self.attack_type == 5 and self.energy >=15 and self.projectile == False:
                self.set_projectile(target)
                self.energy -= 15
                self.projectile = True
                self.attack_cooldown = 10
            

            if self.attack_type == 7 and self.energy >=20 and self.attack_cooldown7 == 0:
                if self.attack_window1_1 == 0:
                    attacking_rect = pygame.Rect(self.rect.centerx - (1.5 * self.rect.width), self.rect.y / 1.25, 3 * self.rect.width, 2 * self.rect.height)
                    self.energy -= 20
                    self.attack_cooldown = 5
                    self.attack_cooldown7 = 35
                    if attacking_rect.colliderect(target.rect):
                        target.healt -= 3
                        target.stun_all = 11
                        target.xstun = 10
                        target.stunbounce = -(self.flip -0.5) *2
                        self.attack_window1_1 = 50
                    pygame.draw.rect(surface, (0,0,255), attacking_rect)
            if self.attack_type == 8 and self.energy >=15 and self.attack_cooldown8 == 0:
                attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y / 1.23, 2 * self.rect.width, self.rect.height)
                self.energy -= 10
                self.attack_cooldown = 5
                self.attack_cooldown8 = 45
                self.vel_y = 25
                if attacking_rect.colliderect(target.rect):
                    target.healt -= 4  
                    target.stun_all = 15
                    target.xstun = 3
                    target.vel_y = +40
                    target.stunbounce = -(self.flip -0.5) *2
                pygame.draw.rect(surface, (0,0,255), attacking_rect)
        
            if self.attack_type == 3:
                if self.energy < 100:
                    self.energy += 2
                    self.vel_y = 1
            if self.attack_type == 6 and self.attack_cooldown6 == 0:
                if self.energy >= 20:
                    if self.flip == True:
                        self.rect.x = target.rect.x - 100
                    else:
                        self.rect.x = target.rect.x + 100
                    self.energy -=20
                    self.attack_cooldown6 = 10
                    self.attack_cooldown = 0
                    self.attack_cooldown1 = 0
                    self.attack_cooldown2 = 0
                    self.attack_cooldown5 = 0
                    target.stun_all = 8
            

    def draw(self, surface):
        screen = surface
        if self.crouch == False:
            pygame.draw.rect(surface, (140, 0, 255), self.rect)
        elif self.crouch == True:
            pygame.draw.rect(surface, (100, 50, 255), self.rect)
        if self.stun_all > 0:
            pygame.draw.rect(surface, (50, 20, 30), self.rect)



            """attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip) - 100 * (self.flip - 0.5) , self.rect.y - 30 + self.attack_y4 * 5, 2 * self.rect.width, self.rect.height / 2)
                self.energy -=1
                self.attack_cooldown4 = 1
                self.attack_window4_1 = 5
                self.attack_y4 +=1
                if attacking_rect.colliderect(target.rect):
                    target.healt -=0.5
                    target.attack_cooldown = 5
                    target.vel_y = 2
                pygame.draw.rect(surface, (255,255,255), attacking_rect)
                if self.attack_y4 == 17:
                    attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip) - 100 * (self.flip - 0.5) , self.rect.y + 40, 2 * self.rect.width, self.rect.height / 2)
                    self.attack_cooldown4 = 20
                    if attacking_rect.colliderect(target.rect):
                        target.healt -= 5
                        target.stun_all = 15
                        target.xstun = 30
                        target.ystun = 0
                        target.stunbounce = -(self.flip -0.5) *2
                        self.attack_cooldown = 20
                    pygame.draw.rect(surface, (255,0,255), attacking_rect)"""
    
