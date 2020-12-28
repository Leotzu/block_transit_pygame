import pygame
pygame.init()

x_bounds = 500
y_bounds = 500

win = pygame.display.set_mode((x_bounds, y_bounds))
pygame.display.set_caption("Super Fun Block Challenge 3000")
clock = pygame.time.Clock()

x = 0
y = 0
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
	# keeping the block in-bounds:
    if x>x_bounds-width:
        x=x_bounds-width
    if x<0:
	    x=0
    if y>y_bounds-height:
	    y=y_bounds-height
    if y<0:
	    y=0
	
	# clear display
    win.fill((0, 0, 0))
    # draw new box with position-based colouring
    pygame.draw.rect(win, (abs(x)%255,abs(y)%255,abs(x+y+20)%255), (x,y,width,height))
    # update display
    pygame.display.flip()
    #pygame.display.update() # this cause the freeze error...why?

pygame.quit()
