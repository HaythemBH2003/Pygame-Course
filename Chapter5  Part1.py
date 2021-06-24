####### CONTROLLING IN-GAME EVENTS #######
##########  WORKING WITH MOUSE  ##########

####          INITIALISATION          ####
import pygame
pygame.init()
W, H = 600, 700
WINDOW = pygame.display.set_mode((W, H))
pygame.display.set_caption("MOUSE EVENTS")
FPS = 20
N = 3
FONT_FILE = "freesansbold.ttf"
RED = (255, 0, 0)
WHITE = (255, 255, 255)
WINDOW.fill(WHITE)
pygame.display.update()
FONT = pygame.font.Font(FONT_FILE, 20)

def draw(x, y, button):
    WINDOW.fill(WHITE)
    TEXT = FONT.render(f"Clicked: {button}", True, RED)
    RECT = TEXT.get_rect()
    RECT.center = (x, y)
    WINDOW.blit(TEXT, RECT)
    pygame.display.update()

def mainloop():
    run = True
    clock = pygame.time.Clock()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            ####    CHECKING FOR  MOUSE CLICKS    ####
            ''' THE TYPE  OF  MOUSE  CLICKING EVENT IS 
                pygame.MOUSEBUTTONDOW              '''    
            if event.type  ==  pygame.MOUSEBUTTONDOWN:
                button = ""
                
                ####    GETTING MOUSE POSITION    ####
                coordinates =   pygame.mouse.get_pos()
                        # coordinates ----> [int, int]
                        # coordinates[0] ----> MOUSE_X
                        # coordinates[1] ----> MOUSE_Y 
                x, y =  coordinates[0], coordinates[1]
                
                ####    SETTING MOUSE POSITION    ####
                '''          GENERAL FORM          '''
                pygame.mouse.set_pos((10, 10))

                ####    GETTING CLICKED BUTTON    ####
                B1,B2,B3 = pygame.mouse.get_pressed(N)
                        # N -------> NUMBER OF BUTTONS
                        # clicked ------> (B1, B2, B3)
                        # B1, B2, B3 -------> BOOLEANS
                        # B1 ------> LEFT BUTTON STATE
                        # B2 -----------> ROLLER STATE
                        # B3 -----> RIGHT BUTTON STATE
                if B1 == True:
                    button += "LEFT BUTTON "
                if B2 == True:
                    button += "ROLLER "
                if B3 == True:
                    button += "RIGHT BUTTON "
                
                ####        SETTING CURSOR        ####
                CURSOR = pygame.cursors.broken_x
                pygame.mouse.set_cursor(CURSOR)
                        # CURSOR ---> NEW MOUSE CURSOR
                draw(x, y, button)      

    pygame.quit()

mainloop()
