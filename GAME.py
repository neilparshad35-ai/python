import pygame
import time
import random 

Width, Height = 1000, 800
win = pygame.display.set_mode((Width, Height))
pygame.display.set_caption('El Elegido')

BG = pygame.image.load('background.jpg')
BG = pygame.transform.smoothscale(BG,(Width, Height))

player_width = 40
player_height = 60

def draw(player):
    win.blit(BG, (0,0))
    pygame.draw.rect(win, 'white', player)
    pygame.display.update()

player_width = 40
player_height = 60
player_vel = 5
def main():
    run = True

    player = pygame.Rect(200, Height - player_height, player_width,player_height)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player.x -= player_vel
        if keys[pygame.K_d]:
            player.x += player_vel

        draw(player)

    pygame.quit()

if __name__ == "__main__":
    main()




