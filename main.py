import pygame
import os

#dimensioni finestra
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#titolo
pygame.display.set_caption("Gamer")

WHITE = ((255, 255, 255))
BLACK = (0,0,0)

BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)

FPS = 60
VEL = 5
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40 

#recupero immagini astranove gialla
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
#dimensione e rotazione immagine GIALLA
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

#recupero immagini astranove rossa
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
#dimensione e rotazione immagine rossa
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

#funzione creazione finestra
def draw_window(red, yellow):
    
    #colore testata finestra
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    #posizione navicelle nella finestra di gioco
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y)) 
    WIN.blit(RED_SPACESHIP, (red.x, red.y)) 
    #colore finestra
    pygame.display.update()


def yellow_handle_movement(keys_pressed, yellow):
    #gestione pulsanti movimento navicella
    
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0 : #sinistra
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x: #destra
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: #sopra
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15: #sotto
        yellow.y += VEL

def red_handle_movement(keys_pressed, red):
    #gestione pulsanti movimento navicella
    
    if keys_pressed[pygame.K_LEFT]  and red.x - VEL > BORDER.x + BORDER.width : #sinistra
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH: #destra
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0: #sopra
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15: #sotto
        red.y += VEL

#funzione principale start
def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #gestione pulsanti movimento navicella
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)  
        red_handle_movement(keys_pressed, red)        
        draw_window(red, yellow)

    pygame.quit()

if __name__ == "__main__":
    main() 





