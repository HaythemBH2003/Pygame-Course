########### SURFACE  CONTENT ###########
'''            FILL  IMAGE           '''
# <!> FILLING THE SURFACE WITH ANYTHING
  # ELSE LATER WILL COVER THE IMAGE <!>

######## COORDINATES CONVENTIONS #######
# (0, 0) -----------------> (MAX_X, 0) #
#    |                           |     #
#    |                           |     #
#    |                           |     #
#    |                           |     #
#   \ /                          |     #
# (0, MAX_Y) ---------- (MAX_X, MAX_Y) #
####### COORDINATES CONVENTIONS ########

###          INITIALISATION          ###
import pygame
pygame.init()
W, H = 700, 500
WINDOW = pygame.display.set_mode((W, H))
pygame.display.set_caption("GAME TITLE")
FPS = 60
COLOR = (126, 192, 255)

########       LOAD IMAGE       ########
'''           GENERAL FORM           '''
# IMG = pygame.image.load(PATH\FILE.ext)
                # IMG ----> LOADED IMAGE
                # PATH -----> IMAGE PATH
                # FILE.ext --> FILE NAME
                        # WITH EXTENSION
'''              EXAMPLE             '''
IMAGE = pygame.image.load(
    "Assets\spaceship_yellow.png")

######## RESIZE & ROTATE  IMAGE ########
RESIZED_IMAGE = pygame.transform.scale(
    IMAGE, (35, 205))
ROTATED_IMAGE = pygame.transform.rotate(
    RESIZED_IMAGE,60)

def draw_window():
    WINDOW.fill(COLOR) # WILL BE COVERED
                        # WITH THE IMAGE 
    ###  DRAW IMAGE ON MAIN SURFACE  ###
    '''         GENERAL FORM         '''
    # SURFACE.blit(IMAGE, (POS_X, POS_Y)) 
                # SURFACE ------> WINDOW
                # IMAGE --> LOADED IMAGE
    # pygame.display.update()
    '''           EXAMPLE            '''
    POS_X, POS_Y = 50, 50
    WINDOW.blit(RESIZED_IMAGE, (POS_X, POS_Y))
    WINDOW.blit(IMAGE, (POS_X + 50, POS_Y + 30))
    WINDOW.blit(ROTATED_IMAGE, (POS_X, POS_Y + 300))
    pygame.display.update()

def mainloop():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)        
        for event in pygame.event.get():
            draw_window()
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

mainloop()