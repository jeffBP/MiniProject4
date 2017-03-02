import sys, pygame

pygame.init()

size = width, height = 600, 400
speed = [0,0]
black = 0,0,0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.jpeg")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    ballrect = ballrect.move(speed)
    if( pygame.key.get_pressed()[pygame.K_UP] != 0 ):
        speed[0]= .2
    if( pygame.key.get_pressed()[pygame.K_DOWN] != 0 ):
        speed[0]= -.2
    if( pygame.key.get_pressed()[pygame.K_LEFT] != 0 ):
        speed[1]= -.2
    if( pygame.key.get_pressed()[pygame.K_RIGHT] != 0 ):
        speed[1]= .2
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
