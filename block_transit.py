import pygame
import random
pygame.init()

x_bounds = 500
y_bounds = 500

win = pygame.display.set_mode((x_bounds, y_bounds))
pygame.display.set_caption("Super Fun Block Challenge 3000")
clock = pygame.time.Clock()

x = 0
y = 0
width = 5
height = 5
vel = 20
rand_max = 30

run = True
while run:
    clock.tick(60)
    
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()
    i=0
    while (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]) and run:
        clock.tick(60)
        
        # this was previously used to decrease colour brightness 
        # the further the particles diffused, but now it's just
        # defining how long between main particle movements
        r = 255-20*i
        i += 1
        if r<0:
            r=0
            break
       
        # create multiple diffusing particles at once:
        for k in range(0,4):
            pygame.draw.rect(win, (abs(x)%255,abs(y)%255,abs(x+y+20)%255), (x+random.randint(-rand_max,rand_max), y+random.randint(-rand_max,rand_max), width, height))
        '''
        pygame.draw.rect(win, (r,0,0), (x+i+random.randint(-rand_max,rand_max), y+i+random.randint(-rand_max,rand_max), width, height))
        pygame.draw.rect(win, (r,0,0), (x+random.randint(-rand_max,rand_max), y+i+random.randint(-rand_max,rand_max), width, height))
        pygame.draw.rect(win, (r,0,0), (x-i+random.randint(-rand_max,rand_max), y+i+random.randint(-rand_max,rand_max), width, height))
        pygame.draw.rect(win, (r,0,0), (x-i+random.randint(-rand_max,rand_max), y+random.randint(-rand_max,rand_max), width, height))
        pygame.draw.rect(win, (r,0,0), (x-i+random.randint(-rand_max,rand_max), y-i+random.randint(-rand_max,rand_max), width, height))
        pygame.draw.rect(win, (r,0,0), (x+random.randint(-rand_max,rand_max), y-i+random.randint(-rand_max,rand_max), width, height))
        pygame.draw.rect(win, (r,0,0), (x+i+random.randint(-rand_max,rand_max), y-i+random.randint(-rand_max,rand_max), width, height))
        pygame.draw.rect(win, (r,0,0), (x+i+random.randint(-rand_max,rand_max), y+random.randint(-rand_max,rand_max), width, height))
        
        for j in range(0,5):
            pygame.draw.rect(win, (r,0,0), (x+random.randint(-rand_max,rand_max), y+random.randint(-rand_max,rand_max), width, height))
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.flip()
        win.fill((0, 0, 0))
        # refreshes the get_pressed()
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
    #win.fill((0, 0, 0))
    # draw new box with position-based colouring
    pygame.draw.rect(win, (abs(x)%255,abs(y)%255,abs(x+y+20)%255), (x,y,width,height))
    # update display
    pygame.display.flip()
    #pygame.display.update() # this cause the freeze error...why?

pygame.quit()
