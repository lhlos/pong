import pygame

pygame.init()

pygame.display.set_caption('Pong')

green = (0, 255, 0)
blue = (0, 0, 128)
red = (255, 0, 0)
black = (0, 0, 0)
clock = pygame.time.Clock()

screenHeight = 600
screenWidth = 800
screen = pygame.display.set_mode((screenWidth ,screenHeight))

running = True

font = pygame.font.SysFont("Cascadia Mono", 100)

textA = font.render('1', True, green)
textRectangleA = textA.get_rect()
textRectangleA.center = (screenWidth/3, 45)

textB = font.render('1', True, green)
textRectangleB = textB.get_rect()
textRectangleB.center = (533, 45)

playerA = pygame.Rect((10,screenHeight/2-125,15,170))
playerB = pygame.Rect((screenWidth-30,screenHeight/2-125,15,170))

ball = pygame.draw.circle(screen, green, [300,400], 30)
ballSpeed = [1,1]

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        playerA.move_ip(0,-3)
    if keys[pygame.K_s]:
        playerA.move_ip(0,3)
    if keys[pygame.K_UP]:
        playerB.move_ip(0,-3)
    if keys[pygame.K_DOWN]:
        playerB.move_ip(0,3)
    
    screen.fill(black)
    
    screen.blit(textA, textRectangleA)
    screen.blit(textB, textRectangleB)
    pygame.draw.rect(screen,(255,0,0),playerA)
    pygame.draw.rect(screen,(255,0,0),playerB)
    ball = ball.move(ballSpeed)
    
    ballSpeed[1] = -ballSpeed[1]
    
    pygame.draw.circle(screen, green, ball.center, 15)
    
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()

