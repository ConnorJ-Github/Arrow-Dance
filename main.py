import pygame

#set up the display
WIDTH, HEIGHT = 600, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

#set up the tab name
pygame.display.set_caption("Arrow-Dance")

#The background colour of the window
BACKGROUND_CLR = (255,255,255)

#Limits the FPS to 60
FPS = 60

#image height and width
ARROW_HEIGHT, ARROW_WIDTH = 96,96

#set up the images

frames = ['Assets/default_arrow.png','Assets/green_arrow.png', 'Assets/blue_arrow.png', 'Assets/red_arrow.png','Assets/pink_arrow.png']
active_frame_up = 0
active_frame_down = 0
active_frame_right = 0
active_frame_left = 0
mode = 0
count = 0


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

        pygame.display.update()


#Changing "image"
def update_arrow(mod, counter):

     act = 0

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


#Handles functions & other operations
        

clock = pygame.time.Clock()
    
run = True
while run:

     clock.tick(FPS)
     active_frame_up, count = update_arrow(mode, count)
     


     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               run = False
        
     keys_pressed = pygame.key.get_pressed()
     if keys_pressed[pygame.K_DOWN]: #Down arrow
          mode = 1
     if keys_pressed[pygame.K_UP]: #Up arrow
           mode = 2
     if keys_pressed[pygame.K_LEFT]: #Left Arrow
           mode = 3
     if keys_pressed[pygame.K_RIGHT]: #Right Arrow
          mode = 4
     if event.type == pygame.KEYUP:
          mode = 0

     draw_window()


pygame.quit()