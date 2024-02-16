import pygame
import random

pygame.init()
clock = pygame.time.Clock()
playerAScore = 0
playerBScore = 0

def ballMovement():
    global ballSpeedX, ballSpeedY, playerAScore, playerBScore
#--------------------------------Moving the ball---------------------------------------    
    ball.x += ballSpeedX
    ball.y += ballSpeedY
#-------------------------------Ball collisions---------------------------------------
    if ball.top <= 0 or ball.bottom >= screenHeight:
        ballSpeedY *= -1
    if ball.left <= 0: 
        ballReset()
        playerBScore += 1
    if ball.right >= screenWidth:
        ballReset()
        playerAScore += 1
    if ball.colliderect(playerA) or ball.colliderect(playerB):
        ballSpeedX *= -1

#---------------------------Defining player rectangle restrictions----------------- 
def playerMovement():
    if playerA.top <= 0:
        playerA.top = 0
    if playerA.bottom >= screenHeight:
        playerA.bottom = screenHeight
    if playerB.top <= 0:
        playerB.top = 0
    if playerB.bottom >= screenHeight:
        playerB.bottom = screenHeight

#----------------------Resetting the ball after a point is scored---------------------        
def ballReset():
    global ballSpeedX, ballSpeedY
    ball.center = (screenWidth/2, screenHeight/2)
    ballSpeedY *= random.choice((1,-1))
    ballSpeedX *= random.choice((1,-1))
    

#----------------------------------Colours-------------------------------------------
green = (0, 255, 0)
blue = (0, 0, 128)
red = (255, 0, 0)
black = (0, 0, 0)
grey = (200,200,200)

#-----------------------------------Setting the screen---------------------------------------
screenHeight = 600
screenWidth = 800
screen = pygame.display.set_mode((screenWidth ,screenHeight))
pygame.display.set_caption('Pong')

#---------------------------------------Scoreboard--------------------------------------------
font = pygame.font.SysFont("Cascadia Mono", 100)

#--------------------------------------Game rectangles------------------------------------------
playerA = pygame.Rect((screenWidth-20,screenHeight/2-70,10,140))
playerB = pygame.Rect((10,screenHeight/2-70,10,140))
ball = pygame.Rect(screenWidth/2-15, screenHeight/2-15,30,30)

running = True
ballSpeedX = 5
ballSpeedY = 5

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        playerA.move_ip(0,-5)
    if keys[pygame.K_s]:
        playerA.move_ip(0,5)
    if keys[pygame.K_UP]:
        playerB.move_ip(0,-5)
    if keys[pygame.K_DOWN]:
        playerB.move_ip(0,5)
    
    ballMovement()
    playerMovement()
    
#-----------------------------------Visuals-------------------------------------------
    screen.fill(black)
    textA = font.render(str(playerAScore), True, red)
    screen.blit(textA, (300,270))
    textB = font.render(str(playerBScore), True, red)
    screen.blit(textB, (460,270))
    pygame.draw.rect(screen,red,playerA)
    pygame.draw.rect(screen,red,playerB)
    pygame.draw.aaline(screen, grey, (screenWidth/2,0), (screenWidth/2,screenHeight))
    pygame.draw.ellipse(screen, green, ball)
    
#------------------------------------Updating the window-----------------------------
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()

