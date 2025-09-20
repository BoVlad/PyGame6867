import pygame
import random


pygame.init()


font = pygame.font.SysFont("Arial", 30)
score = 0

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Кольори
GREY = (125, 125, 125)
GREEN = (0, 163, 108)
VIOLET = (138, 43, 226)

# Завантаження зображення кота та фону
cat_img = pygame.image.load("1.png") # Завантажуємо зображення кота
cat_img = pygame.transform.smoothscale(cat_img, (50, 50)) # Використовуємо smoothscale для кращої якості
cat = cat_img.get_rect() # Отримуємо розміри зображення кота
cat.topleft = (100, 100) # Встановлюємо початкову позицію кота

# Завантаження фону
background_img = pygame.image.load("landscape-1844229_1280.png") # Завантажуємо фонове зображення
background_img = pygame.transform.scale(background_img, (800, 600)) # Масштабуємо його під розмір екрану

# Параметри швидкості, вони знадобляться пізніше
speed = 0 # Початкова вертикальна швидкість (кіт стоїть на місці)
gravity = 0.3 # Значення нашої сили тяжіння
jump_speed = -7 # Швидкість стрибка (зверни увагу, що вона від'ємна, бо напрямлена вгору)


obstacle_timer = 0 # Таймер для контролю інтервалу часу між перешкодами

obstacles = [] # Список перешкод
obstacle_width = 50 # Ширина перешкоди
gap_height = 150 # Відстань між верхньою та нижньою перешкодами
min_distance = 250 # Мінімальна горизонтальна відстань між перешкодами






# Основний цикл
while True:
    screen.blit(background_img, (0, 0))  # Малюємо фонове зображення на екрані
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            speed = jump_speed  # Встановлюємо швидкість стрибка

    speed += gravity


    cat.y += speed

    if cat.y > 550:
        cat.y = 0
        speed = 0
    if cat.y < 0:
        cat.y = 0
        speed = 0

    obstacle_timer += 1

    # Додамо нову перешкоду тільки коли пройде достатньо часу:

    if obstacle_timer > min_distance:
        top_obstacle_height = random.randint(100, 400)  # Випадкова висота верхньої перешкоди
        bottom_obstacle_height = screen.get_height() - top_obstacle_height - gap_height  # Рахуємо висоту нижньої перешкоди
        top_obstacle = pygame.Rect(800, 0, obstacle_width, top_obstacle_height)
        bottom_obstacle = pygame.Rect(800, screen.get_height() - bottom_obstacle_height, obstacle_width,
                                      bottom_obstacle_height)
        obstacles.append((top_obstacle, bottom_obstacle))
        obstacle_timer = 0

    # Далі переміщаємо перешкоди та перевіряємо на зіткнення:
    for top_obstacle, bottom_obstacle in obstacles:
        top_obstacle.x -= 5  # Переміщаємо перешкоду трохи вліво
        bottom_obstacle.x -= 5  # Переміщаємо нижню перешкоду трохи вліво
        # Перевірка на зіткнення з перешкодою
        if cat.colliderect(top_obstacle) or cat.colliderect(bottom_obstacle):
            print("Game Over!")
            pygame.quit()
            exit()
        if top_obstacle.x < -obstacle_width:  # Видаляємо перешкоду, якщо вона вийшла за межі екрану
            obstacles.remove((top_obstacle, bottom_obstacle))

        if top_obstacle.x + 60 == 100:  # Видаляємо перешкоду, якщо вона вийшла за межі екрану
            score = score + 1


    # Лишилося відмалювати самі перешкоди:
    for top_obstacle, bottom_obstacle in obstacles:
        pygame.draw.rect(screen, GREEN, top_obstacle)  # Верхня перешкода
        pygame.draw.rect(screen, GREEN, bottom_obstacle)
    screen.blit(cat_img, cat.topleft)

    score_text = font.render(f"Рахунок: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))



    pygame.display.update()

    clock.tick(60)