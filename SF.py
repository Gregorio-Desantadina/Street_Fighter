import pygame
from WClass.Warrior import Fighter
from WClass.Rockstar import Rock
from WClass.Vampire import Vamp
from WClass.Cyberp import Cyber

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Juego de Milk-Chan")

clock = pygame.time.Clock()
FPS = 30

#Define colours
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

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

#create fighters11
figther_1 = Rock(1, 200, 310, SCREEN_WIDTH, SCREEN_HEIGHT, screen)
figther_2 = Cyber(2, 700, 310, SCREEN_WIDTH, SCREEN_HEIGHT, screen)

run = True
while run:
    clock.tick(FPS)

    draw_bg()

    #show player healt
    draw_healt_bar(figther_1.healt, 20, 10)
    draw_healt_bar(figther_2.healt, 580, 10)

    #show player energy
    draw_energy_bar(figther_1.energy, 20, 16)
    draw_energy_bar(figther_2.energy, 580, 16)

    events = pygame.event.get()

    figther_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, figther_2, events)
    figther_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, figther_1, events)
    figther_1.draw(screen)
    figther_2.draw(screen)
    
   

    
    for event in events:
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()