import pygame
import os

WIDTH, HEIGHT = 600, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Arrow-Dance")


BACKGROUND_CLR = (255,255,255)

FPS = 60

ARROW_HEIGHT, ARROW_WIDTH = 96,96


DEFAULT_ARROW_IMAGE = pygame.image.load(os.path.join('Assets', 'default_arrow.png'))
DEFAULT_ARROW = pygame.transform.scale(DEFAULT_ARROW_IMAGE, (ARROW_HEIGHT,ARROW_WIDTH))

LEFT_ARROW = pygame.transform.rotate(DEFAULT_ARROW, 90)
RIGHT_ARROW = pygame.transform.rotate(DEFAULT_ARROW, 270)
DOWN_ARROW = pygame.transform.rotate(DEFAULT_ARROW, 180)


RED_ARROW_IMAGE = pygame.image.load(os.path.join('Assets', 'red_arrow.png'))
RED_ARROW = pygame.transform.scale(RED_ARROW_IMAGE, (ARROW_HEIGHT,ARROW_WIDTH))

BLUE_ARROW_IMAGE = pygame.image.load(os.path.join('Assets', 'blue_arrow.png'))
BLUE_ARROW = pygame.transform.scale(BLUE_ARROW_IMAGE, (ARROW_HEIGHT,ARROW_WIDTH))

GREEN_ARROW_IMAGE = pygame.image.load(os.path.join('Assets', 'green_arrow.png'))
GREEN_ARROW = pygame.transform.scale(GREEN_ARROW_IMAGE, (ARROW_HEIGHT,ARROW_WIDTH))

def draw_window(): 
        WIN.fill(BACKGROUND_CLR)
        WIN.blit(DEFAULT_ARROW,(25,200))
        WIN.blit(LEFT_ARROW,(175,200))
        WIN.blit(RIGHT_ARROW,(325,200))
        WIN.blit(DOWN_ARROW,(475,200))
        pygame.display.update()

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