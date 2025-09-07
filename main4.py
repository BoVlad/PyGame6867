import pygame

# Ініціалізація pygame
pygame.init()
# Встановлення розміру вікна
screen = pygame.display.set_mode((800, 600))
# Створення об'єкта: прямокутник
rect_position = pygame.math.Vector2(100, 100)  # Початкова позиція
# Основний цикл
pygame.display.flip()
screen.fill((255, 255, 255))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:  # Перевірка на натискання клавіші
            if event.key == pygame.K_d:  # Якщо натиснута клавіша Enter
                if rect_position.x >= 720:
                    continue
                else:
                    rect_position.x = rect_position.x + 30
            if event.key == pygame.K_a:  # Якщо натиснута клавіша Enter
                if rect_position.x <= 30:
                    continue
                else:
                    rect_position.x = rect_position.x - 30
            if event.key == pygame.K_w:  # Якщо натиснута клавіша Enter
                if rect_position.y <= 30:
                    continue
                else:
                    rect_position.y = rect_position.y - 30
            if event.key == pygame.K_s:  # Якщо натиснута клавіша Enter
                if rect_position.y >= 520:
                    continue
                else:
                    rect_position.y = rect_position.y + 30
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 255), (rect_position.x, rect_position.y, 50, 50))
    # Очищуємо екран
    # Малюємо прямокутник
    # Оновлення екрана
    pygame.display.flip()
# rect_position = pygame.math.Vector2(0, 550)
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     # Очищуємо екран
#     # screen.fill((255, 255, 255))
#     # Малюємо прямокутник
#     pygame.draw.rect(screen, (0, 0, 255), (rect_position.x, rect_position.y, 50, 50))
#     rect_position.x = rect_position.x + 1
#     rect_position.y = rect_position.y - 0.7
#
#     # Оновлення екрана
#     pygame.display.flip()
pygame.quit()
