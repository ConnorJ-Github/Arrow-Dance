import pygame
import random

pygame.init()

#set up the display
WIDTH, HEIGHT = 600, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

#set up the tab name
pygame.display.set_caption("Arrow-Dance")

#The background colour of the window
BACKGROUND_CLR = (255,255,255)

#Colours
BLACK = (0,0,0)

#Font
font = pygame.font.Font('Silkscreen-Regular.ttf',25)

#Limits the FPS to 60
FPS = 60

#image height and width
ARROW_HEIGHT, ARROW_WIDTH = 96,96

#set up the images
frames = ['Assets/default_arrow.png','Assets/green_arrow.png', 'Assets/blue_arrow.png', 'Assets/red_arrow.png','Assets/pink_arrow.png']
active_frame_up, active_frame_down, active_frame_right, active_frame_left = 0, 0, 0, 0
mode, mode1, mode2, mode3 = 0, 0, 0, 0
count = 0

#player score & lives
score = 0
life = 3

#player input
user_input = ''


#player life
def player_life(life):
     score_text = font.render(f'Lives: {life}', True, BLACK)
     WIN.blit(score_text, (475,0))

#player score
def player_score(score):
     score_text = font.render(f'Score: {score}', True, BLACK)
     WIN.blit(score_text, (0,0))


def create_sequence():
     
     default_sequence = ["up","down","left","right"]
     current_sequence = random.shuffle(default_sequence)
     return current_sequence



#draw the current sequence
def draw_sequence(): #maybe try using a class?

     #to do

     #create an array ["up","down","left","right"]
     #have the array order randomly change
     #use that as the current sequence.
     #display the sequence to the display.

     image = "Assets/default_arrow.png"
     rotation = [0,90,180,270]

     sequence_one = pygame.transform.scale(pygame.image.load(image), (50,50))
     sequence_one = pygame.transform.rotate(sequence_one, rotation[0])
     WIN.blit(sequence_one, (200,100))

     sequence_two = pygame.transform.scale(pygame.image.load(image), (50,50))
     sequence_two = pygame.transform.rotate(sequence_two, rotation[3])
     WIN.blit(sequence_two, (250,100))

     sequence_three = pygame.transform.scale(pygame.image.load(image), (50,50))
     sequence_three = pygame.transform.rotate(sequence_three, rotation[2])
     WIN.blit(sequence_three, (300,100))

     sequence_four = pygame.transform.scale(pygame.image.load(image), (50,50))
     sequence_four = pygame.transform.rotate(sequence_four, rotation[1])
     WIN.blit(sequence_four, (350,100))



#Changing "image"
def update_arrow(mod, counter):

     act = 0
     counter = 0

     if counter >= 60:
          counter = 0

     if mod == 1:
          if counter < 59:
               act = 1
          if counter >= 59:
               act = 0

     if mod == 2:
          if counter < 59:
               act = 2
          if counter >= 59:
               act = 0

     if mod == 3:
          if counter < 59:
               act = 3
          if counter >= 59:
               act = 0

     if mod == 4:
          if counter < 59:
               act = 4
          if counter >= 59:
               act = 0

     counter += 1

     return act, counter

#draws the window & content
def draw_window():

        levels = 0; 
        WIN.fill(BACKGROUND_CLR)

        upArrow = pygame.transform.scale(pygame.image.load(frames[active_frame_up]),(ARROW_HEIGHT,ARROW_WIDTH))
        WIN.blit(upArrow, (25, 200))

        leftArrow = pygame.transform.scale(pygame.image.load(frames[active_frame_left]),(ARROW_HEIGHT,ARROW_WIDTH))
        leftArrow = pygame.transform.rotate(leftArrow, 90)
        WIN.blit(leftArrow, (175, 200))

        rightArrow = pygame.transform.scale(pygame.image.load(frames[active_frame_right]),(ARROW_HEIGHT,ARROW_WIDTH))
        rightArrow = pygame.transform.rotate(rightArrow, 270)
        WIN.blit(rightArrow, (325, 200))

        downArrow = pygame.transform.scale(pygame.image.load(frames[active_frame_down]),(ARROW_HEIGHT,ARROW_WIDTH))
        downArrow = pygame.transform.rotate(downArrow, 180)
        WIN.blit(downArrow, (475, 200))

        header_text = font.render('Match the Sequence', True, BLACK)
        WIN.blit(header_text, (140,50))

        player_score(score)
        player_life(life)
        draw_sequence()

        pygame.display.update()


#Handles functions & other operations
        

clock = pygame.time.Clock()
    
run = True
while run:

     clock.tick(FPS)
     active_frame_up, count = update_arrow(mode, count)
     active_frame_down, count = update_arrow(mode1, count)
     active_frame_left, count = update_arrow(mode2, count)
     active_frame_right, count = update_arrow(mode3, count)

     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               run = False
        
     keys_pressed = pygame.key.get_pressed()
     if keys_pressed[pygame.K_UP]: #UP arrow
          mode = 1
     if keys_pressed[pygame.K_DOWN]: #DOWN arrow
           mode1 = 2
     if keys_pressed[pygame.K_LEFT]: #Left Arrow
           mode2 = 3
     if keys_pressed[pygame.K_RIGHT]: #Right Arrow
          mode3 = 4
     if event.type == pygame.KEYUP:
          mode = 0
          mode1 = 0
          mode2 = 0
          mode3 = 0

     draw_window()


pygame.quit()