import pygame
from threading import Event
import time 



class Vamp():
    def __init__(self, player, x, y, SCREEN_WIDTH, SCREEN_HEIGHT, screen, projectiles):
        self.screen = screen
        self.screenHeight = SCREEN_HEIGHT
        self.screenWidth = SCREEN_WIDTH
        self.player = player
        self.flip = False
        self.rect = pygame.Rect((x, y, 80, 100))
        self.vel_y = 0
        self.__jumps = 0
        self.__jumps_limit = 3
        self.__grounded = True
        self.__airbone = False
        self.dx = 0
        self.dmgmult = 1
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
        self.stun_all = 0
        self.xstun = 0
        self.ystun = 0
        self.stunbounce = 0
        self.fly = False

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
            self.vel_y = -16
            self.__grounded = False
            self.__airbone = True

    
    def get_event_keys(self, events):
            keys = []
            for event in events:
                if event.type == pygame.KEYDOWN:

                    keys.append(pygame.key.name(event.key))
            return keys
    
    def update(self, screen_width, screen_height, surface, target, events):
        SPEED = 20
        GRAVITY = 1
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
           self.attack_window1_1 -= 1

        
        if self.fly == True and self.energy >10:
            self.energy -=0.2
        elif self.fly == True:
            self.fly = False
        
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
            if key[pygame.K_s] and self.fly == False:
                self.crouch = True
                GRAVITY = 2.5
            else:
                self.crouch = False
                GRAVITY = 1

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
        
            if "w" in self.get_event_keys(events) and self.fly == False:
                self.jump()
            if (key[pygame.K_w]) and self.fly == True:
                self.vel_y = -20
            elif (key[pygame.K_s]) and self.fly == True:
                self.vel_y = 20
            elif self.fly == True:
                self.vel_y = 0

           
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
                (surface, target)
               

        elif self.player == 2 and self.stun_all == 0 and self.healt > 0:
            #self.crouch
            if key[pygame.K_DOWN]:
                self.crouch = True
                GRAVITY = 2.5
            else:
                self.crouch = False
                GRAVITY = 1

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
            if (key[pygame.K_UP]) and self.fly == True:
                self.vel_y = -20
            elif (key[pygame.K_DOWN]) and self.fly == True:
                self.vel_y = 20
            elif self.fly == True:
                self.vel_y = 0

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
        if self.fly == False:
            self.vel_y += GRAVITY
        dy += self.vel_y
        if self.energy >0 and self.fly == 2:
            self.energy -=1

        
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
                    attacking_rect = pygame.Rect(self.rect.centerx - (self.rect.width * self.flip), self.rect.y,self.rect.width, self.rect.height)
                    self.energy -=2
                    self.attack_cooldown1 = 30
                    if attacking_rect.colliderect(target.rect):
                        self.attack_window1_1 = 25
                        self.move_cooldown = 20
                        self.xstun = 18
                        self.stunbounce = -(self.flip -0.5) *2
                        target.damage_manager (3, 23, 0, 3, False, -(self.flip -0.5) *2)
                    pygame.draw.rect(surface, (200, 100, 25), attacking_rect)
                elif self.attack_cooldown1 <=10 and self.attack_window1_1 != 0:
                    attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
                    self.attack_cooldown = 10
                    self.attack_cooldown1 = 30
                    if attacking_rect.colliderect(target.rect):
                        self.move_cooldown = 20
                        self.xstun = 20
                        self.stunbounce = (self.flip -0.5) *2
                        target.damage_manager (5, 15, 18, 3, False, -(self.flip -0.5) *2)
                    pygame.draw.rect(surface, (255, 255, 255), attacking_rect)


            if self.attack_type == 2 and self.energy > 1 and self.fly == True:
                if self.attack_cooldown2 == 0:
                    attacking_rect = pygame.Rect(self.rect.centerx - (self.rect.width * self.flip), self.rect.y,self.rect.width, self.rect.height)
                    self.attack_cooldown2 = 2
                    self.energy -=1
                    if attacking_rect.colliderect(target.rect):
                        self.stunbounce = (self.flip -0.5) *2
                        target.damage_manager (0.2, 5, 0, -self.vel_y +2, False, 0)
                        target.rect.x = self.rect.x
                        if self.healt < 50:
                            self.healt += 0.3
                    pygame.draw.rect(surface, (200, 100, 25), attacking_rect)


            if self.attack_type == 3:
                if self.energy < 100:
                    self.energy += 2
                    self.vel_y = 1

            if self.attack_type == 6 and self.attack_cooldown6 == 0:
                if self.fly == False:
                    self.fly = True
                    self.attack_cooldown6 = 10
                else:
                    self.fly = False
                    self.attack_cooldown6 = 10

                        



    def damage_manager (self, damage, allstun, xstun, ystun, block, stunbounce):
        self.healt -=damage
        self.stun_all = allstun
        self.xstun += xstun
        self.vel_y -= ystun
        self.stunbounce = stunbounce
            

    def draw(self, surface):
        screen = surface
        if self.crouch == False:
            pygame.draw.rect(surface, (140, 0, 255), self.rect)
        elif self.crouch == True:
            pygame.draw.rect(surface, (100, 50, 255), self.rect)
        if self.stun_all > 0:
            pygame.draw.rect(surface, (50, 20, 30), self.rect)
    