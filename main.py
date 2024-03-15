import pygame
import random
import time

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


#player life
def player_life(life):
     life_text = font.render(f'Lives: {life}', True, BLACK)
     WIN.blit(life_text, (475,0))

#player score
def player_score(score):
     score_text = font.render(f'Score: {score}', True, BLACK)
     WIN.blit(score_text, (0,0))


#creates a random sequence.
def create_sequence():
     global default_sequence
     default_sequence = ["UP","DOWN","LEFT","RIGHT"]
     random.shuffle(default_sequence)

#runs the create sequence function.
create_sequence()

user_Sequence = []
#check if user input matches the sequence.
def userinput_Sequence(userinput):

     user_Sequence.append(userinput)
     length = len(user_Sequence)

     if length == 3:
          match_userSequence(user_Sequence)
     elif length > 3:
          user_Sequence.clear()


def match_userSequence(sequence):

     global score
     global life

     if(sequence) == default_sequence:
          score += 1
          match_text = font.render('Pair Matched!', True, BLACK)
          WIN.blit(match_text, (475,0))
     else:
          life -= 1

     




#match sequence with user input

#draw the current sequence #needs improving "some day"
def draw_sequence(): #maybe try using a class?

     image = "Assets/default_arrow.png"
     rotation = [0,90,180,270]

     #I know this code is awful, pygame was giving me weird errors the better way  https://www.youtube.com/watch?v=dQw4w9WgXcQ

     for i in range(len(default_sequence)):
          if default_sequence[0] == "UP":
               sequence_one = pygame.transform.scale(pygame.image.load(image), (50,50))
               sequence_one = pygame.transform.rotate(sequence_one, rotation[0])
               WIN.blit(sequence_one, (200,100))
          if default_sequence[0] == "LEFT":
               sequence_one = pygame.transform.scale(pygame.image.load(image), (50,50))
               sequence_one = pygame.transform.rotate(sequence_one, rotation[2])
               WIN.blit(sequence_one, (200,100))
          if default_sequence[0] == "RIGHT":
               sequence_one = pygame.transform.scale(pygame.image.load(image), (50,50))
               sequence_one = pygame.transform.rotate(sequence_one, rotation[1])
               WIN.blit(sequence_one, (200,100))
          if default_sequence[0] == "DOWN":
               sequence_one = pygame.transform.scale(pygame.image.load(image), (50,50))
               sequence_one = pygame.transform.rotate(sequence_one, rotation[3])
               WIN.blit(sequence_one, (200,100))

          if default_sequence[1] == "UP":
               sequence_two = pygame.transform.scale(pygame.image.load(image), (50,50))
               sequence_two = pygame.transform.rotate(sequence_two, rotation[0])
               WIN.blit(sequence_two, (250,100))
          if default_sequence[1] == "LEFT":
               sequence_two = pygame.transform.scale(pygame.image.load(image), (50,50))
               sequence_two = pygame.transform.rotate(sequence_two, rotation[2])
               WIN.blit(sequence_two, (250,100))
          if default_sequence[1] == "RIGHT":
               sequence_two = pygame.transform.scale(pygame.image.load(image), (50,50))
               sequence_two = pygame.transform.rotate(sequence_two, rotation[1])
               WIN.blit(sequence_two, (250,100))
          if default_sequence[1] == "DOWN":
               sequence_two = pygame.transform.scale(pygame.image.load(image), (50,50))
               sequence_two = pygame.transform.rotate(sequence_two, rotation[3])
               WIN.blit(sequence_two, (250,100))

          if default_sequence[2] == "UP":
               sequence_three = pygame.transform.scale(pygame.image.load(image), (50,50))
               sequence_three = pygame.transform.rotate(sequence_three, rotation[0])
               WIN.blit(sequence_three, (300,100))
          if default_sequence[2] == "LEFT":
               sequence_three = pygame.transform.scale(pygame.image.load(image), (50,50))
               sequence_three = pygame.transform.rotate(sequence_three, rotation[2])
               WIN.blit(sequence_three, (300,100))
          if default_sequence[2] == "RIGHT":
               sequence_three = pygame.transform.scale(pygame.image.load(image), (50,50))
               sequence_three = pygame.transform.rotate(sequence_three, rotation[1])
               WIN.blit(sequence_three, (300,100))
          if default_sequence[2] == "DOWN":
               sequence_three = pygame.transform.scale(pygame.image.load(image), (50,50))
               sequence_three = pygame.transform.rotate(sequence_three, rotation[3])
               WIN.blit(sequence_three, (300,100))
          
          if default_sequence[3] == "UP":
               sequence_four = pygame.transform.scale(pygame.image.load(image), (50,50))
               sequence_four = pygame.transform.rotate(sequence_four, rotation[0])
               WIN.blit(sequence_four, (350,100))
          if default_sequence[3] == "LEFT":
               sequence_four = pygame.transform.scale(pygame.image.load(image), (50,50))
               sequence_four = pygame.transform.rotate(sequence_four, rotation[2])
               WIN.blit(sequence_four, (350,100))
          if default_sequence[3] == "RIGHT":
               sequence_four = pygame.transform.scale(pygame.image.load(image), (50,50))
               sequence_four = pygame.transform.rotate(sequence_four, rotation[1])
               WIN.blit(sequence_four, (350,100))
          if default_sequence[3] == "DOWN":
               sequence_four = pygame.transform.scale(pygame.image.load(image), (50,50))
               sequence_four = pygame.transform.rotate(sequence_four, rotation[3])
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

        #controls if the sequence is drawn

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
          userinput_Sequence("UP")
     if keys_pressed[pygame.K_DOWN]: #DOWN arrow
           mode1 = 2
           userinput_Sequence("DOWN")
     if keys_pressed[pygame.K_LEFT]: #Left Arrow
           mode2 = 3
           userinput_Sequence("LEFT")
     if keys_pressed[pygame.K_RIGHT]: #Right Arrow
          mode3 = 4
          userinput_Sequence("RIGHT")
     if keys_pressed[pygame.K_SPACE]: #space temp solution to generate new solutions quickly. 
          create_sequence()
     if event.type == pygame.KEYUP:
          mode = 0
          mode1 = 0
          mode2 = 0
          mode3 = 0

     draw_window()


pygame.quit()