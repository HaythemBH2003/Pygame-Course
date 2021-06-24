######### WRITE TEXT IN PYGAME #########

#####        INITIALISATION        #####
import pygame
pygame.init()
W, H = 750, 750
WINDOW = pygame.display.set_mode((W, H))
pygame.display.set_caption("WRITE TEXT")
BLUE = (126, 192, 255)
BLACK = (255, 255, 255)
FPS = 40

def draw():
    WINDOW.fill(BLACK)
    ######      ADDING  TEXT      ######
    '''  STEP 1: CREATE FONT OCJECT  '''
    '''         GENERAL FORM         '''
    # FONT = pygame.font.Font(FF,  SIZE)
            # FF --------> FONT_FILE.ttf
            # SIZE ----------> FONT SIZE
    '''            EXAMPLE           '''
    FONT = pygame.font.Font("freesansbold.ttf", 30)
    
    '''  STEP 2: CREATE TEXT OBJECT  '''
    '''         GENERAL FORM         '''
    # TEXT = FONT.render(STR, True, CLR)
            # FONT --> FONT OBJECT ADDED
            # STR -------> TEXT TO WRITE
            # CLR -----------> RGB COLOR
    '''            EXAMPLE           '''
    TEXT = FONT.render("TESTING", True, BLUE)
    
    '''  STEP 3: CREATE RECT OBJECT  '''
    '''         GENERAL FORM         '''
    # RECT = TEXT.get_rect()
            # TEXT --> TEXT OBJECT ADDED
    '''            EXAMPLE           '''
    RECT = TEXT.get_rect()

    '''   STEP 4:  CENTER  THE TEXT   '''
    RECT.center = (375, 375)
    WINDOW.blit(TEXT, RECT)

    pygame.display.update()

def mainloop():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
    pygame.quit()

mainloop()