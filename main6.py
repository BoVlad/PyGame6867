import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

# Кольори
YELLOW = (253, 253, 150)
GREEN = (5, 244, 120)

# Початкові координати квадратика
x, y = 300, 200
width, height = 50, 50
speed = 5 # Швидкість руху квадратика

# Основний цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]: # Ліворуч
        x -= speed
    if keys[pygame.K_UP] or keys[pygame.K_w]: # Ліворуч
        y -= speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]: # Ліворуч
        y += speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]: # Ліворуч
        x += speed
    screen.fill(YELLOW)
    pygame.draw.rect(screen, GREEN, (x, y, width, height))
    pygame.display.update()
    clock.tick(60)
