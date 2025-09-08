import pygame
import random
pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

x, y = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
RADIUS = 30

last_move_time = 0
MOVE_INTERVAL = 1000  # мс

font = pygame.font.SysFont("Arial", 30)

score = 0
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            distance = (((mouse_x - x) ** 2) + ((mouse_y - y) ** 2)) ** 0.5
            if distance <= RADIUS:
                score += 1
                last_move_time = 0
    current_time = pygame.time.get_ticks()
    if current_time - last_move_time >= MOVE_INTERVAL:
        x, y = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
        last_move_time = current_time

    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), RADIUS)
    score_text = font.render(f"Влучань: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
pygame.quit()