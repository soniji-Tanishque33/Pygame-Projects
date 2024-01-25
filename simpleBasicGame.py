import pygame


pygame.init()
width = 500
height = 500
screen = pygame.display.set_mode((height, width))
clock = pygame.time.Clock()
fps = 60
running = True
dt = 0
player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)

while running:
  # poll for events
  # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
    screen.fill("purple")
    pygame.draw.circle(screen, "red", player_pos, 40)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
       player_pos.y -= 300*dt
    if keys[pygame.K_DOWN]:
       player_pos.y += 300*dt
    if keys[pygame.K_LEFT]:
       player_pos.x -= 300*dt
    if keys[pygame.K_RIGHT]:
       player_pos.x += 300*dt
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()