import pygame
import random
pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

color = RED
color_time = 0

x, y = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
RADIUS = 30

last_move_time = 0
MOVE_INTERVAL = 1000  # мс

font = pygame.font.SysFont("Arial", 30)

score = 0
clock = pygame.time.Clock()
running = True
time_score = 0
start_time = pygame.time.get_ticks()



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
                color = GREEN
                color_time = pygame.time.get_ticks()
    current_time = pygame.time.get_ticks()
    if current_time - last_move_time >= MOVE_INTERVAL:
        x, y = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
        last_move_time = current_time
    time_score = (pygame.time.get_ticks() - start_time) // 1000
    screen.fill(WHITE)
    if color == GREEN:
        if (pygame.time.get_ticks() - color_time) > 200:
            color = RED

    pygame.draw.circle(screen, color, (x, y), RADIUS)

    pygame.draw.rect(screen, (20, 200, 222), (5, 10, 150, 35), 3)
    pygame.draw.rect(screen, (20, 200, 222), (5, 10, 150, 65), 3)
    pygame.draw.rect(screen, (20, 200, 222), (5, 10, 490, 485), 3)

    score_text = font.render(f"Влучань: {score}", True, (0, 0, 0))
    time_text = font.render(f"Час: {time_score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(time_text, (10, 40))
    pygame.display.flip()
pygame.quit()


# ...
#     score_text = font.render(f"{points} баллiв", True, (30, 30, 230))
#     screen.blit(score_text, (5, 35))
#     time_text = font.render(f"{MOVE_INTERVAL}ms", True, (230, 30, 30))
#     screen.blit(time_text, (5, 5))
#
#     pygame.display.flip()
# pygame.quit() 