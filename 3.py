import pygame


pygame.init()
screen = pygame.display.set_mode((800, 600))
rect_position = pygame.math.Vector2(100, 100)
pygame.display.flip()
screen.fill((255, 255, 255))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if rect_position.x >= 720:
                    continue
                else:
                    rect_position.x = rect_position.x + 30
            if event.key == pygame.K_LEFT:
                if rect_position.x <= 30:
                    continue
                else:
                    rect_position.x = rect_position.x - 30
            if event.key == pygame.K_UP:
                if rect_position.y <= 30:
                    continue
                else:
                    rect_position.y = rect_position.y - 30
            if event.key == pygame.K_DOWN:
                if rect_position.y >= 520:
                    continue
                else:
                    rect_position.y = rect_position.y + 30
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 255), (rect_position.x, rect_position.y, 50, 50))
    pygame.display.flip()
pygame.quit()