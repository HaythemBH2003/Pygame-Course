########### SOUND IN PYGAME ###########

##           INITIALISATION          ##
import os
import pygame
pygame.init()
FPS = 30
W, H = 400, 400
WINDOW = pygame.display.set_mode((W, H))
pygame.display.set_caption("PLAY SOUND")
FONT = pygame.font.SysFont(
    "comicsans", 50)
WHITE = (255, 255, 255)
BLUE = (35, 156, 245)

'''             STEP   1             '''
##        CREATING MIXER OBJECT       ##
MIXER = pygame.mixer
'''             STEP   2             '''
##         INITIALISING MIXER         ##
MIXER.init()
'''             STEP   3             '''
##         LOADING AUDIO FILE         ##
'''           GENERAL FORM           '''
#   FILE = os.path.join(PATH, FILE_NAME)
#   AUDIO_FILE =  MIXER.music.load(FILE)
'''              EXAMPLE             '''
PATH = "Assets"
FILENAME = "sound.mp3"
FILE = os.path.join(PATH, FILENAME)
AUDIO_FILE = MIXER.music.load(FILE)

##        DRAW WINDOW FUNCTION        ##
def draw():
    WINDOW.fill(BLUE)
    TEXT = FONT.render(
        "TAP TO PLAY SOUND", True,WHITE)
    RECT = TEXT.get_rect()
    RECT.centerx, RECT.centery = W // 2, H // 2 - 50
    WINDOW.blit(TEXT, RECT)
    TEXT2 = FONT.render(
        "PRESS r TO PAUSE", True, WHITE)
    RECT2 = TEXT2.get_rect()
    RECT2.centerx, RECT2.centery = W // 2, H // 2 + 50
    WINDOW.blit(TEXT2, RECT2)
    pygame.display.update() 

##              MAINLOOP              ##
def mainloop():    
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                '''      STEP 4      '''
                ##   PLAYING  SOUND   ##
                MIXER.music.play()
                # PLAY LOADED AUDIO FILE
                # MIXER --> MIXER OBJECT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    '''    STEP 5    '''    
                    ##  PAUSE  SOUND  ##
                    MIXER.music.stop()
                    # STOP PLAYING AUDIO
                    # MIXER -> MIXER OBJ 
        draw()
    pygame.quit()

mainloop()
