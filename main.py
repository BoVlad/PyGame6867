import pygame
print(pygame.ver)

# Ініціалізуємо Pygame
pygame.init()

# Зберігаємо у змінних розміри вікна (ширина, висота)
# WINDOW_WIDTH = 800
# WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

# Зберігаємо у змінній основний колір фону (RGB)
# background_color = (135, 206, 250) # Небесно-блакитний
background_color = (135, 178, 135)

# Створюємо вікно
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Встановлюємо назву вікна
pygame.display.set_caption("Моя перша гра")

# Заповнюємо фон кольором
screen.fill(background_color)

# Оновлюємо дисплей
pygame.display.flip()

# Затримка перед виходом
pygame.time.delay(5000)