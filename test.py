import pygame

height = 640
width = 240

screen = pygame.display.set_mode((height, width))
running = True

while running:

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # print(event)
        if event.type == pygame.KEYDOWN:
            screen.fill("red")
        if event.type ==pygame.KEYUP:
            screen.fill("yellow")
        pygame.display.flip()

    

pygame.quit()

    