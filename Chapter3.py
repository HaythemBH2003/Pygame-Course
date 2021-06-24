#############  DRAWING IN  PYGAME  #############

#####            INITIALISATION            #####
import pygame
pygame.init()
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
PINK = (255, 0, 255)
WINDOW = pygame.display.set_mode((750, 750))
pygame.display.set_caption("DRAWING WINDOW")
FPS = 40

def draw():
    WINDOW.fill(BLACK)
  #####          DRAWING   SHAPES           #####
   #######        DRAW   RECTANGLE        #######
    '''             GENERAL  FORM             '''
    # pygame.draw.rect(SU, C, (TL_X, TL_Y, W, H))
                # SU --------> SURFACE TO DRAW ON
                # C ------------------> RGB COLOR
                # TR_X -------> TOP_LEFT_CORNER X
                # TR_Y -------> TOP_LEFT_CORNER Y
                # W ------------> RECTANGLE WIDTH
                # H -----------> RECTANGLE HEIGHT
    '''                EXAMPLE                '''
    pygame.draw.rect(WINDOW, GREEN, (100, 100, 200, 300))
   #######        DRAW   A  CIRCLE        #######
    '''             GENERAL  FORM             '''
    # pygame.draw.circle(SU, C, (C_X, C_Y),  RAD)
                # SU --------> SURFACE TO DRAW ON
                # C ------------------> RGB COLOR
                # C_X ----------> CIRCLE CENTER X
                # C_Y ----------> CRICLE CENTER Y
                # RAD ------------> CIRCLE RADIUS
    '''                EXAMPLE                '''
    pygame.draw.circle(WINDOW, BLUE, (400, 400), 50)
   #######        DRAW  A  POLYGON        #######
    '''             GENERAL  FORM             '''
    # pygame.draw.polygon(SU, C, (POINTS COORDS))
                # SU --------> SURFACE TO DRAW ON
                # C ------------------> RGB COLOR
                # (POINTS COORDS) -> ((X1, Y1), (X2, Y2), ...)
    '''                EXAMPLE                '''
    pygame.draw.polygon(WINDOW, RED, ((500, 500), (600, 500), (600, 600)))
   
  #####          COLORING A PIXEL          #####
    '''             GENERAL  FORM             '''
    ''' STEP 1: GET PIXEL  ARRAY OF A SURFACE '''
   # PIXEL_ARRAY = pygame.PixelArray(SURFACE)
                # PIXEL_ARRAY --> ARRAY OF PIXELS
    '''        STEP 2: COLOR THE PIXEL        '''
   # PIXEL_ARRAY[PIXEL_Y, PIXEL_X] = COLOR
    '''                EXAMPLE                '''
    pixel_array = pygame.PixelArray(WINDOW)
    for i in range(700, 750):
        pixel_array[i, i] = PINK
    pygame.display.update()

def mainloop():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            draw()
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

mainloop()
