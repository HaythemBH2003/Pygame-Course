########### SURFACE  CONTENT ###########
'''            FILL  COLOR           '''
# <!> FILLING THE SURFACE WITH ANYTHING
  # ELSE LATER WILL COVER THE COLOR <!>

###          INITIALISATION          ###
import pygame
pygame.init()
W, H = 300, 400
WINDOW = pygame.display.set_mode((W, H))
pygame.display.set_caption("GAME TITLE")
FPS = 60

def mainloop():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)        
        ### FILL SURFACE  WITH COLOR ###
        '''       GENERAL FORM       '''
        # SURFACE.fill(COLOR)   
                        # COLOR ---> RGB
        # pygame.display.update()
        '''          EXAMPLE         '''
        COLOR = (129, 196, 255)
                    # COLOR -> (B, G, R)
                    # B, G, R ∈ [0, 255]
        WINDOW.fill(COLOR)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

mainloop()