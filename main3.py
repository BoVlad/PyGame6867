from operator import truediv
import random
import pygame

pygame.init()

# Зберігаємо у змінних розміри вікна (ширина, висота)
# WINDOW_WIDTH = 800
# WINDOW_HEIGHT = 600
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 400

# Зберігаємо у змінній основний колір фону (RGB)
# background_color = (135, 206, 250) # Небесно-блакитний

# Створюємо вікно
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Встановлюємо назву вікна
pygame.display.set_caption("Vlad")
pygame.display.flip()
# Заповнюємо фон кольором

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Перевірка на натискання закриття вікна
            pygame.quit()
    if event.type == pygame.KEYDOWN:  # Перевірка на натискання клавіші
        if event.key == pygame.K_RETURN:  # Якщо натиснута клавіша Enter
            random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            screen.fill(random_color)
            pygame.display.flip()
