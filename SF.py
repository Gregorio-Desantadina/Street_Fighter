import pygame
from WClass.Warrior import Fighter
from WClass.Rockstar import Rock
from WClass.Vampire import Vamp
from WClass.Newcyberp import Cyber
from WClass.Elemental import Element
from WClass.Bot import Bot
from WClass.Milk import Milk

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("NADA")

clock = pygame.time.Clock()
FPS = 30

#define game variables
intro_count = 3
last_count_update = pygame.time.get_ticks()
score = [0, 0]#player scores. [P1, P2]
round_over = False
ROUND_OVER_COOLDOWN = 2000

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

count_font = pygame.font.Font("assets/fonts/turok.ttf", 80)
score_font = pygame.font.Font("assets/fonts/turok.ttf", 30)


#Define colours
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (200,200,100)

bg_image = pygame.image.load("textura/background3.jpg").convert_alpha()

def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))

#healtbar
def draw_healt_bar(healt, x, y):
    ratio = healt / 100
    pygame.draw.rect(screen, WHITE, (x - 3, y - 3, 406, 36))
    pygame.draw.rect(screen, BLACK, (x, y, 400, 30))
    pygame.draw.rect(screen, RED, (x, y, 400 * ratio, 30))
#energybar
def draw_energy_bar(energy, x, y):
    ratio2 = energy / 100
    pygame.draw.rect(screen, BLUE, (x, y + 40, 400 * ratio2, 30))

def draw_ground(x, y):
    pygame.draw.rect(screen, YELLOW, (x, y, 1000, 110))

#function for drawing text
def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

def get_event_keys(events):
    keys = []
    for event in events:
        if event.type == pygame.KEYDOWN:
            keys.append(pygame.key.name(event.key))
    return keys


projectiles = pygame.sprite.Group()
teclas_player1 = {
    'up':  'w',
    'down': pygame.K_s, 
    'left': pygame.K_a,
    'right': pygame.K_d,
    'attack1': pygame.K_r,
    'attack2': pygame.K_t, 
    'attack3': pygame.K_y,             
}
teclas_player2 = {
    'up':  'up',
    'down': pygame.K_DOWN, 
    'left': pygame.K_LEFT,
    'right': pygame.K_RIGHT,
    'attack1': pygame.K_KP1,
    'attack2': pygame.K_KP2, 
    'attack3': pygame.K_KP3,             
}

character_list1 = {
    0: Cyber(1, 200, 310, SCREEN_WIDTH, SCREEN_HEIGHT, screen, projectiles, teclas_player1),
    1: Bot(1, 200, 310, SCREEN_WIDTH, SCREEN_HEIGHT, screen, projectiles, teclas_player1),
    2: Milk(1, 200, 310, SCREEN_WIDTH, SCREEN_HEIGHT, screen, projectiles, teclas_player1)
}

character_list2 = {
    0: Cyber(2, 700, 310, SCREEN_WIDTH, SCREEN_HEIGHT, screen, projectiles, teclas_player2),
    1: Bot(2, 700, 310, SCREEN_WIDTH, SCREEN_HEIGHT, screen, projectiles, teclas_player2),
    2: Milk(2, 700, 310, SCREEN_WIDTH, SCREEN_HEIGHT, screen, projectiles, teclas_player2)
}


#create fighters11
figther_1 = Cyber(1, 200, 310, SCREEN_WIDTH, SCREEN_HEIGHT, screen, projectiles, teclas_player1)
figther_2 = Bot(2, 700, 310, SCREEN_WIDTH, SCREEN_HEIGHT, screen, projectiles, teclas_player2)



run = True
character_selector = True
char1number = 0
char2number = 0
char1select = False
char2select = False
while character_selector == True:
    clock.tick(FPS)
    draw_bg()
    events = pygame.event.get()
    key = pygame.key.get_pressed()
    figther_1 = character_list1[char1number]
    figther_2 = character_list2[char2number]

    if char1select== False:
        draw_text(" P1: " + figther_1.name, score_font, BLACK, 60, 250)
    else: 
        draw_text(" P1: " + figther_1.name, score_font, BLUE, 60, 250)
    if char2select == False:
        draw_text(" P2: " + figther_2.name, score_font, BLACK, 770, 250)
    else:
        draw_text(" P2: " + figther_2.name, score_font, BLUE, 770, 250)
    if char1select and char2select == True:
        character_selector = False
    
    
    if 'w' in get_event_keys(events) and char1select == False:
        char1number = (char1number + 1) % len(character_list1)
    if 's' in get_event_keys(events) and char1select == False:
        char1number =(char1number - 1) % len(character_list1)
    if 'up' in get_event_keys(events) and char2select == False:
        char2number =(char2number + 1) % len(character_list2)
    if 'down' in get_event_keys(events) and char2select == False:
        char2number =(char2number - 1) % len(character_list2)
    if 'r' in get_event_keys(events):
        char1select = True
    if 't' in get_event_keys(events):
        char1select = False
    if '[1]' in get_event_keys(events):
        char2select = True
    if '[2]' in get_event_keys(events):
        char2select = False



    pygame.display.update()

while run:
    clock.tick(FPS)

    draw_bg()

    #show player healt
    draw_healt_bar(figther_1.healt, 20, 10)
    draw_healt_bar(figther_2.healt, 580, 10)

    #show player energy
    draw_energy_bar(figther_1.energy, 20, 16)
    draw_energy_bar(figther_2.energy, 580, 16)

    draw_text("P1: " + str(score[0]), score_font, RED, 20, 80)
    draw_text("P2: " + str(score[1]), score_font, RED, 923, 80)

    events = pygame.event.get()

    if intro_count <= 0:
        #move fighters
        figther_1.update(SCREEN_WIDTH, SCREEN_HEIGHT, screen, figther_2, events)
        figther_2.update(SCREEN_WIDTH, SCREEN_HEIGHT, screen, figther_1, events)
    else:
        #display count timer
        draw_text(str(intro_count), count_font, RED, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
        #update count timer
        if (pygame.time.get_ticks() - last_count_update) >= 1000:
            intro_count -= 1
            last_count_update = pygame.time.get_ticks()

    figther_1.draw(screen)
    figther_2.draw(screen)
    
    for projectile in projectiles:
        if projectile.remove_projectile == True:
            projectiles.remove(projectile)

    projectiles.update(SCREEN_WIDTH, SCREEN_HEIGHT, screen)
    projectiles.draw(screen)


    if round_over == False:
        if figther_1.healt <= 0:
            score[1] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
        elif figther_2.healt <= 0:
            score[0] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()

    else:
        if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
            for projectile in projectiles:
                projectiles.remove(projectile)
            round_over = False
            intro_count = 4
            figther_1.__init__(1, 200, 310, SCREEN_WIDTH, SCREEN_HEIGHT, screen, projectiles, teclas_player1)
            figther_2.__init__(2, 700, 310, SCREEN_WIDTH, SCREEN_HEIGHT, screen, projectiles, teclas_player2)


        
    draw_ground(0, 490)
    
   

    
    for event in events:
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit() ##