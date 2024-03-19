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
WHITE = (255,255,255)

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


background_image = pygame.image.load('Assets/Background-image.png')
#background_image = pygame.transform.scale(background_image, (600,500))

#sound effects

correct_sfx = pygame.mixer.Sound('Assets/correct_ding.mp3')
incorrect_sfx = pygame.mixer.Sound('Assets/incorrect_ding.mp3')

#player score & lives
score = 0
life = 3

#user sequence
user_Sequence = []

#Sequence matched
matched = False
not_matched = False


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
     user_Sequence.clear()

#runs the create sequence function.
create_sequence()


#creates a user sequence list base on user input
def userinput_Sequence(userinput):

     user_Sequence.append(userinput)
     length = len(user_Sequence)

     print("user sequence bug", user_Sequence)

     if length == 4:
          match_userSequence(user_Sequence)


#Checks the user sequence to see if it is a match.
def match_userSequence(sequence):

     global score
     global life
     global matched, not_matched

     #debug
     #print("Current Sequence", default_sequence)
     #print("User Sequence", sequence)

     if sequence == default_sequence:
          score += 1
          matched = True
     else:
          life -= 1
          not_matched = True


#reset after sequence match or fail

def next_sequence():
     global matched,not_matched, trigger1,trigger2,trigger3,trigger4
     matched, not_matched = False, False
     trigger1,trigger2,trigger3,trigger4 = 0, 0, 0, 0
     create_sequence()



#draw the current sequence 
def draw_sequence():

     image = "Assets/default_arrow.png"
     rotation = [0,90,180,270] #0 = Up , 1 = Left, 2 = Down, 3 = Right

     for i in range(len(default_sequence)):

          match default_sequence[0]:
               case "UP":
                    sequence_one = pygame.transform.scale(pygame.image.load(image), (50,50))
                    sequence_one = pygame.transform.rotate(sequence_one, rotation[0])
                    WIN.blit(sequence_one, (200,100))
               case "LEFT":
                    sequence_one = pygame.transform.scale(pygame.image.load(image), (50,50))
                    sequence_one = pygame.transform.rotate(sequence_one, rotation[1])
                    WIN.blit(sequence_one, (200,100))
               case "RIGHT":
                    sequence_one = pygame.transform.scale(pygame.image.load(image), (50,50))
                    sequence_one = pygame.transform.rotate(sequence_one, rotation[3])
                    WIN.blit(sequence_one, (200,100))
               case "DOWN":
                    sequence_one = pygame.transform.scale(pygame.image.load(image), (50,50))
                    sequence_one = pygame.transform.rotate(sequence_one, rotation[2])
                    WIN.blit(sequence_one, (200,100))


          match default_sequence[1]:
               case "UP":
                    sequence_two = pygame.transform.scale(pygame.image.load(image), (50,50))
                    sequence_two = pygame.transform.rotate(sequence_two, rotation[0])
                    WIN.blit(sequence_two, (250,100))
               case "LEFT":
                    sequence_two = pygame.transform.scale(pygame.image.load(image), (50,50))
                    sequence_two = pygame.transform.rotate(sequence_two, rotation[1])
                    WIN.blit(sequence_two, (250,100))
               case "RIGHT":
                    sequence_two = pygame.transform.scale(pygame.image.load(image), (50,50))
                    sequence_two = pygame.transform.rotate(sequence_two, rotation[3])
                    WIN.blit(sequence_two, (250,100))
               case "DOWN":
                    sequence_two = pygame.transform.scale(pygame.image.load(image), (50,50))
                    sequence_two = pygame.transform.rotate(sequence_two, rotation[2])
                    WIN.blit(sequence_two, (250,100))

          match default_sequence[2]:
               case "UP":
                    sequence_three = pygame.transform.scale(pygame.image.load(image), (50,50))
                    sequence_three = pygame.transform.rotate(sequence_three, rotation[0])
                    WIN.blit(sequence_three, (300,100))
               case "LEFT":
                    sequence_three = pygame.transform.scale(pygame.image.load(image), (50,50))
                    sequence_three = pygame.transform.rotate(sequence_three, rotation[1])
                    WIN.blit(sequence_three, (300,100))
               case "RIGHT":
                    sequence_three = pygame.transform.scale(pygame.image.load(image), (50,50))
                    sequence_three = pygame.transform.rotate(sequence_three, rotation[3])
                    WIN.blit(sequence_three, (300,100))
               case "DOWN":
                    sequence_three = pygame.transform.scale(pygame.image.load(image), (50,50))
                    sequence_three = pygame.transform.rotate(sequence_three, rotation[2])
                    WIN.blit(sequence_three, (300,100))


          match default_sequence[3]:
               case "UP":
                    sequence_four = pygame.transform.scale(pygame.image.load(image), (50,50))
                    sequence_four = pygame.transform.rotate(sequence_four, rotation[0])
                    WIN.blit(sequence_four, (350,100))
               case "LEFT":
                    sequence_four = pygame.transform.scale(pygame.image.load(image), (50,50))
                    sequence_four = pygame.transform.rotate(sequence_four, rotation[1])
                    WIN.blit(sequence_four, (350,100))
               case "RIGHT":
                    sequence_four = pygame.transform.scale(pygame.image.load(image), (50,50))
                    sequence_four = pygame.transform.rotate(sequence_four, rotation[3])
                    WIN.blit(sequence_four, (350,100))
               case "DOWN":
                    sequence_four = pygame.transform.scale(pygame.image.load(image), (50,50))
                    sequence_four = pygame.transform.rotate(sequence_four, rotation[2])
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
        #WIN.blit(background_image, (0,0))

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

        if life == 0:
               WIN.fill(BLACK)
               end_text = font.render('Out of Lives', True, WHITE)
               WIN.blit(end_text, (200,150))

               quit_text = font.render('Press "Q" to Quit', True, WHITE)
               WIN.blit(quit_text, (130,200))


        pygame.display.update()


#Handles functions & other operations
up,down,left,right = False,False,False,False
trigger1,trigger2,trigger3,trigger4 = 0, 0, 0, 0  

pygame.key.get_repeat()
clock = pygame.time.Clock()

run = True
while run:

     pygame.key.set_repeat()

     clock.tick(FPS)
     active_frame_up, count = update_arrow(mode, count)
     active_frame_down, count = update_arrow(mode1, count)
     active_frame_left, count = update_arrow(mode2, count)
     active_frame_right, count = update_arrow(mode3, count)

     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               run = False
     
          if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_UP: #UP arrow
                    print(event.key)
                    mode = 1
                    up = True
                    #userinput_Sequence("UP")
               if event.key == pygame.K_DOWN: #DOWN arrow
                    mode1 = 2
                    down = True
                    #userinput_Sequence("DOWN")
               if event.key == pygame.K_LEFT: #Left Arrow
                    mode2 = 3
                    left = True
                    #userinput_Sequence("LEFT")
               if event.key == pygame.K_RIGHT: #Right Arrow
                    mode3 = 4
                    right = True
                    #userinput_Sequence("RIGHT")
               if event.key == pygame.K_SPACE: #space temp solution to generate new solutions quickly. 
                    create_sequence()
               if event.key == pygame.K_q:
                    pygame.Quit()

          if event.type == pygame.KEYUP:
               mode, mode1, mode2, mode3 = 0, 0, 0, 0

     if up == True and trigger1 == 0:
          userinput_Sequence("UP")
          trigger1 +=1
     
     if down == True and trigger2 == 0:
          userinput_Sequence("DOWN")
          trigger2 += 1

     if left == True and trigger3 == 0:
          userinput_Sequence("LEFT")
          trigger3 += 1

     if right == True and trigger4 == 0:
          userinput_Sequence("RIGHT")
          trigger4 += 1


     if matched == True:
          correct_sfx.play()
          next_sequence()
          up, left, right, down = False, False, False, False
     
     if not_matched == True:
          incorrect_sfx.play()
          next_sequence()
          up, left, right, down = False, False, False, False



     draw_window()


pygame.quit()

if __name__ == "__main__":
    main()