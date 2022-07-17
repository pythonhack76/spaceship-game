import pygame
import os

#dimensioni finestra
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#titolo
pygame.display.set_caption("Gamer")

WHITE = ((255, 255, 255))

FPS = 60
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40 

#recupero immagini astranove gialla
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
#dimensione e rotazione immagine GIALLA
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

#recupero immagini astranove rossa
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
#dimensione e rotazione immagine rossa
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

#funzione creazione finestra
def draw_window():
    
    #colore testata finestra
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SPACESHIP, (300, 100)) 
    #colore finestra
    pygame.display.update()



#funzione principale start
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
      
        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main() 





