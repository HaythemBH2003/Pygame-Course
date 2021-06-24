######## CONTROLLING IN-GAME EVENTS #######
#########  WORKING WITH KEYBOARD  #########

####           INITIALISATION          ####
import pygame
pygame.init()
W, H = 600, 700
WINDOW = pygame.display.set_mode((W, H))  
pygame.display.set_caption("KB EVENTS")
FPS = 10
RED = (255, 0, 0)
WHITE = (255, 255, 255)
WINDOW.fill(WHITE)
pygame.display.update()

def draw(x, y):
    WINDOW.fill(WHITE)
    pygame.draw.circle(WINDOW, RED, (x, y), 50)
    pygame.display.update()

def mainloop():
    run = True
    clock = pygame.time.Clock()
    DELTA = 20
    y = 50
    x = W // 2

    ## DETECT CONTINUOUSLY PRESSED KEY EVERY FRAME ##
    '''   IF THE set_repeat(delay) IS NOT CALLED, THE 
          CONTINUOUSLY PRESSED KEYS ARE ONLY DETECTED
          ONCE WHICH IS IN THE FRAME OF THE PRESS '''
    DELAY = 100
    pygame.key.set_repeat(DELAY)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            ## CHECKING ALL KEYBOARD TAPS ##
            if event.type == pygame.KEYDOWN:
                ## GET STATES OF ALL KEYS ##
                keys = pygame.key.get_pressed()
                       # keys -> (512 * 1|0)
                       # 0 ----> NOT PRESSED
                       # 1 --------> PRESSED
                ##  GET STATE OF ONE KEY  ##
                '''    GENERAL FORM  1   '''
                ''' DETECT MULTIPLE KEYS '''
                # K = pygame.key.get_pressed()
                # if K[pygame.KEY_CONSTANTS]:
                    # (....)
                '''        EXAMPLE       '''
                if keys[pygame.K_RIGHT]:
                    if x < W - 50:
                        x += DELTA
                if keys[pygame.K_LEFT]:
                    if x > 50:
                        x -= DELTA
                '''    GENERAL FORM  2   '''
                '''  DETECTS SINGLE KEY  '''
                # BY GETTING KEYDOWN EVENT'S 
                                       # KEY
                # if event.key == pygame.KC:
                       # KC --> KEY CONSTANT
                '''        EXAMPLE       '''           
                if event.key == pygame.K_DOWN:
                    if y < H - 50:
                        y += DELTA
                if event.key == pygame.K_UP:
                    if y > 50:
                        y -= DELTA
        draw(x, y)
    pygame.quit()

mainloop()