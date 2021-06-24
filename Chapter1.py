###############  PYGAME  ###############
''' PYGAME IS A 2-D GRAPHICS LIBRARY '''

import pygame
pygame.init()

''' EVERYTHING WE USE IN PYGAME IS NAMED
    A SURFACE                        '''

# <!> DO NOT NAME THE FILE: PYGAME <!> #

#########    SET UP  PYGAME    #########
###           GAME  WINDOW           ###

''' STEP 1:  WINDOW WIDTH AND HEIGHT '''
'''           GENERAL FORM           '''
#  WIN = pygame.display.set_mode((W, H))
                # WIN -----> GAME WINDOW
                # (W, H) -------> COUPLE
                # W -------------> WIDTH
                # H ------------> HEIGHT
'''              EXAMPLE             '''
W, H = 300, 500
WINDOW = pygame.display.set_mode((W, H))

''' STEP 2:   WINDOW TITLE           '''
'''           GENERAL FORM           '''
# <!!> WINDOW NEEDS TO BE DEFINED <!!> #
# pygame.display.set_caption(WINDOW_CAP)
            # WINDOW_CAP ---> GAME TITLE 
'''              EXAMPLE             '''
pygame.display.set_caption("GAME TITLE")

#########      MAIN  LOOP      #########
''' MAIN LOOP IS A FUNCTION THAT HANDLES 
    ALL GAME EVENTS LIKE: REDRAWING GAME
    WINDOW, CHECKING FOR COLLISIONS) '''
FPS = 60

def mainloop():
    ##           GAME  LOOP           ##
    clock = pygame.time.Clock()
               # clock ---> Clock OBJECT
               # TO CONTROL REFRESH RATE              
     # while not LOSING_CONDITIONS:
         # [...]
    lost = False  # lost --> LOSING COND
    while not lost:
        clock.tick(FPS)   # IMPOSING FPS
                          # REFRESH RATE 
                          # WILL   NEVER 
                          # SURPASS  THE
                          # SET      FPS           
        #  CHECK FOR ALL OCCURING EVENTS
         # for ev in pygame.event.get(): 
             # [...]
        for event in pygame.event.get():
            # pygame.event.get() RETURNS
                  # A LIST OF ALL EVENTS
            # CHECKING FOR EXITING EVENT
            if event.type == pygame.QUIT:
                LOST = True

    pygame.quit()

''' RUN THE FUNCTION ONLY WHEN EXECUTED IN
    THIS FILE AND NOT WHEN IMPORTED    '''
if __name__ == "__main__":
    mainloop() 