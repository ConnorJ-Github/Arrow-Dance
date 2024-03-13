import pygame
import os

WIDTH, HEIGHT = 600, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Arrow-Dance")

#The background colour of the window
BACKGROUND_CLR = (255,255,255)

#Limits the FPS to 60
FPS = 60

#image height and width
ARROW_HEIGHT, ARROW_WIDTH = 96,96

#set up the images

DEFAULT_ARROW_IMAGE = pygame.image.load(os.path.join('Assets', 'default_arrow.png'))
DEFAULT_ARROW = pygame.transform.scale(DEFAULT_ARROW_IMAGE, (ARROW_HEIGHT,ARROW_WIDTH))

UP_ARROW = pygame.transform.rotate(DEFAULT_ARROW, 0)
LEFT_ARROW = pygame.transform.rotate(DEFAULT_ARROW, 90)
RIGHT_ARROW = pygame.transform.rotate(DEFAULT_ARROW, 270)
DOWN_ARROW = pygame.transform.rotate(DEFAULT_ARROW, 180)


RED_ARROW_IMAGE = pygame.image.load(os.path.join('Assets', 'red_arrow.png'))
RED_ARROW = pygame.transform.scale(RED_ARROW_IMAGE, (ARROW_HEIGHT,ARROW_WIDTH))

BLUE_ARROW_IMAGE = pygame.image.load(os.path.join('Assets', 'blue_arrow.png'))
BLUE_ARROW = pygame.transform.scale(BLUE_ARROW_IMAGE, (ARROW_HEIGHT,ARROW_WIDTH))

GREEN_ARROW_IMAGE = pygame.image.load(os.path.join('Assets', 'green_arrow.png'))
GREEN_ARROW = pygame.transform.scale(GREEN_ARROW_IMAGE, (ARROW_HEIGHT,ARROW_WIDTH))


#draws the window & content
def draw_window(up_arrow, down_arrow, left_arrow, right_arrow): 
        WIN.fill(BACKGROUND_CLR)
        WIN.blit(UP_ARROW,(up_arrow.x,up_arrow.y))
        WIN.blit(LEFT_ARROW,(left_arrow.x,left_arrow.y))
        WIN.blit(RIGHT_ARROW,(right_arrow.x,right_arrow.y))
        WIN.blit(DOWN_ARROW,(down_arrow.x,down_arrow.y))
        pygame.display.update()


#Handles functions & other operations
        
def main():
    up_arrow = pygame.Rect(25,200, ARROW_HEIGHT, ARROW_WIDTH)
    left_arrow = pygame.Rect(175,200, ARROW_HEIGHT,ARROW_WIDTH)
    right_arrow = pygame.Rect(325,200, ARROW_WIDTH,ARROW_HEIGHT)
    down_arrow = pygame.Rect(475,200, ARROW_HEIGHT,ARROW_WIDTH)

    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_DOWN]: #Down arrow
             down_arrow.y += 1
        if keys_pressed[pygame.K_UP]: #Up arrow
             up_arrow.y += 1
        if keys_pressed[pygame.K_LEFT]: #Left Arrow
             left_arrow.y += 1
        if keys_pressed[pygame.K_RIGHT]: #Right Arrow
             right_arrow.y += 1

        draw_window(up_arrow, down_arrow,left_arrow,right_arrow)


    pygame.quit()

if __name__ == "__main__":
    main()