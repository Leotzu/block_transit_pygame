import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Super Fun Block Challenge 3000")
clock = pygame.time.Clock()

x = 50
y = 50
width = 40
height = 60
vel = 5

run = True
while run:
    clock.tick(60)
    
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
	    x -= vel
    if keys[pygame.K_RIGHT]:
	    x += vel
    if keys[pygame.K_UP]:
	    y -= vel
    if keys[pygame.K_DOWN]:
	    y += vel
	
	# clear display
    win.fill((0, 0, 0))
    # draw new box
	pygame.draw.rect(win, (255,0,0), (x,y,width,height))
    # update display
    pygame.display.flip()
    #pygame.display.update() # this cause the freeze error...why?

pygame.quit()
