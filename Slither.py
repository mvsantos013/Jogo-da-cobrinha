import pygame
import random
import time

pygame.init()

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Slither')
clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
blue = (0,0,255)

smallFont = pygame.font.SysFont("comicsansms", 25)
medFont = pygame.font.SysFont("comicsansms", 50)
largeFont = pygame.font.SysFont("comicsansms", 80)
#------------------------------------------------------------------------------ 
def text_objects(text, color, size):
    if size == "small":
        textSurface = smallFont.render(text, True, color)
    elif size == "med":
        textSurface = medFont.render(text, True, color)
    elif size == "large":
        textSurface = largeFont.render(text, True, color)
    return textSurface, textSurface.get_rect()
#------------------------------------------------------------------------------ 
def message(msg, color, y_display = 0, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width)/2, (y_display)
    gameDisplay.blit(textSurf, textRect)
#------------------------------------------------------------------------------ 
def dot(x0,y0, block_size):
    gameDisplay.fill(red, rect = [x0,y0, block_size, block_size])
#------------------------------------------------------------------------------ 
def snake(snakeList, block_size):
    for XnY in snakeList:
        gameDisplay.fill(black, rect = [XnY[0] , XnY[1], block_size, block_size])
#------------------------------------------------------------------------------ 
def gameIntro():
    gameDisplay.fill(white)
    gameIntro = True
    while gameIntro:
        message("Welcome to the Slither!", green, 0.3*display_height, "med")
        message("- Get 50 apples (if you can)", blue, 0.42*display_height, "small")
        message("Press Enter to start", black, display_height/2, "small")
        message("Made by Kaleo", green, display_height - 0.05*display_height, "small")
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit() 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_RETURN:
                    gameIntro = False                   
#------------------------------------------------------------------------------ 
def gameLoop():
    #------------------------------------------------------------------------------ 
    a,b,c,d = 0,0,0,0
    FPS = 6
    gameExit = False
    gameOver = False
    block_size = 20
    x0 = block_size*random.randint(0,(display_width/block_size) - 1)
    y0 = block_size*random.randint(0,(display_height/block_size) - 1)
    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = random.choice([-block_size,0,block_size])
    lead_y_change = 0
    if lead_x_change == 0:    
        lead_y_change = random.choice([-block_size,block_size])
    snakeList = []
    bodyCount = 1
    #------------------------------------------------------------------------------ 
     
    while not gameExit:
    #------------------------------------------------------------------------------ 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
    #------------------------------------------------------------------------------ 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if a == 1:
                        pass
                    else:    
                        lead_x_change = -block_size
                        lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    if b == 1:
                        pass
                    else:    
                        lead_x_change = block_size
                        lead_y_change = 0
                elif event.key == pygame.K_UP:
                    if c == 1:
                        pass
                    else:
                        lead_y_change = -block_size
                        lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    if d == 1:
                        pass
                    else:
                        lead_y_change = block_size
                        lead_x_change = 0
    #------------------------------------------------------------------------------ 
        lead_x += lead_x_change
        lead_y += lead_y_change
        if lead_x_change == block_size:
            a,b,c,d = 1,0,0,0
        elif lead_x_change == -block_size:
            a,b,c,d = 0,1,0,0
        elif lead_y_change == block_size:
            a,b,c,d = 0,0,1,0
        elif lead_y_change == -block_size:
            a,b,c,d = 0,0,0,1
        
        if lead_x == x0 and lead_y == y0:
            x0 = block_size*random.randint(0,(display_width/block_size) - 1)
            y0 = block_size*random.randint(0,(display_height/block_size) - 1)
            bodyCount += 1
            FPS += 1
    #------------------------------------------------------------------------------ 
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        if len(snakeList) > bodyCount:
            del snakeList[0]
    #------------------------------------------------------------------------------ 
        if lead_x == -block_size or lead_x == display_width or lead_y == -block_size or lead_y == display_height:
            gameOver = True
            time.sleep(1)
        for i in snakeList[:-1]:
            if i == snakeHead:
                gameOver = True
                time.sleep(1)
    #------------------------------------------------------------------------------ 
        gameDisplay.fill(white)
        message("Apples: %i" %(bodyCount - 1), black, display_height - 0.98*display_height, "small")
        if gameOver == False:          
            dot(x0,y0, block_size)
            snake(snakeList, block_size)
            pygame.display.update()
        clock.tick(FPS)
    #    print (event)        
    #------------------------------------------------------------------------------ 
        while gameOver == True:
            message("Game Over", red, 0.3*display_height, "large")
            message("Press Esc to quit or Enter to continue", black, display_height/2, "small")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        gameExit = True
                        gameOver = False
                    elif event.key == pygame.K_RETURN:
                        gameLoop()
    pygame.quit()
    quit()
    #------------------------------------------------------------------------------ 
gameIntro()
gameLoop()
pygame.quit()
quit()
