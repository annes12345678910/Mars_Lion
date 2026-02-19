# Mars_Lion
#It is stuff for mars

import pygam
Pygame.inut()

fps = 45
timer = pygame.time.Clock()
Whith = 1200
Height = 1000

screen = pygame.display.set_mode([WIDTH, Height])
pygame.display.set_caption('Paint!')


run = True 
while run:  
  timer.tick(fps)
  screen.fill(255, 127, 127)

  for event in pygame.event.get():
     if event.type == pygame.QUIT:
        run = False
  Pygame.display.flip()
Pygame.quit()
