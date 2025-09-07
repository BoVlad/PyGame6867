import sys
import pygame

pygame.init()
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пример меню на pygame")
clock = pygame.time.Clock()

# ---------- Утилиты ----------
def draw_text(surf, text, size, color, center):
    font = pygame.font.SysFont(None, size)  # системный шрифт
    txt = font.render(text, True, color)
    rect = txt.get_rect(center=center)
    surf.blit(txt, rect)
    return rect

class Button:
    def __init__(self, text, center, w=260, h=56):
        self.text = text
        self.rect = pygame.Rect(0, 0, w, h)
        self.rect.center = center
        self.focus = False

    def draw(self, surf):
        bg = (30, 144, 255) if self.focus else (230, 230, 230)
        fg = (255, 255, 255) if self.focus else (30, 30, 30)
        pygame.draw.rect(surf, bg, self.rect, border_radius=12)
        pygame.draw.rect(surf, (180, 180, 180), self.rect, 2, border_radius=12)
        draw_text(surf, self.text, 32, fg, self.rect.center)

    def update_focus_by_mouse(self, mouse_pos):
        self.focus = self.rect.collidepoint(mouse_pos)

    def click(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

# ---------- Сцены ----------
class MenuScene:
    def __init__(self):
        cx, cy = WIDTH // 2, HEIGHT // 2
        gap = 72
        self.buttons = [
            Button("Начать игру", (cx, cy - gap)),
            Button("Настройки",  (cx, cy)),
            Button("Выход",     (cx, cy + gap)),
        ]
        self.idx = 0
        self.buttons[self.idx].focus = True

    def draw(self, surf):
        surf.fill((245, 248, 252))
        draw_text(surf, "Главное меню", 48, (40, 40, 40), (WIDTH//2, 120))
        for b in self.buttons:
            b.draw(surf)

        draw_text(surf, "↑/↓ — выбор, Enter — подтвердить, Esc — выход",
                  22, (100, 100, 100), (WIDTH//2, HEIGHT - 30))

    def update(self, events):
        mouse_pos = pygame.mouse.get_pos()

        # Ховер мышью
        for i, b in enumerate(self.buttons):
            b.update_focus_by_mouse(mouse_pos)
            if b.focus:
                self.idx = i

        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key in (pygame.K_UP, pygame.K_w):
                    self.idx = (self.idx - 1) % len(self.buttons)
                elif e.key in (pygame.K_DOWN, pygame.K_s):
                    self.idx = (self.idx + 1) % len(self.buttons)
                elif e.key == pygame.K_ESCAPE:
                    return "quit"
                elif e.key in (pygame.K_RETURN, pygame.K_SPACE):
                    return self.activate(self.idx)

            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                # клик по кнопке
                for i, b in enumerate(self.buttons):
                    if b.click(e.pos):
                        return self.activate(i)

        # синхронизируем фокус
        for i, b in enumerate(self.buttons):
            b.focus = (i == self.idx)
        return None

    def activate(self, i):
        if i == 0:
            return "game"
        elif i == 1:
            return "settings"
        elif i == 2:
            return "quit"

class GameScene:
    def __init__(self):
        self.t = 0

    def draw(self, surf):
        surf.fill((20, 20, 30))
        draw_text(surf, "Игра идёт (демо)", 42, (255, 255, 255), (WIDTH//2, HEIGHT//2 - 20))
        draw_text(surf, "Esc — вернуться в меню", 24, (200, 200, 200), (WIDTH//2, HEIGHT//2 + 25))

    def update(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                return "menu"
        return None

class SettingsScene:
    def draw(self, surf):
        surf.fill((250, 245, 235))
        draw_text(surf, "Настройки (демо)", 42, (40, 40, 40), (WIDTH//2, HEIGHT//2 - 20))
        draw_text(surf, "Esc — назад", 24, (80, 80, 80), (WIDTH//2, HEIGHT//2 + 25))

    def update(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                return "menu"
        return None

# ---------- Менеджер сцен ----------
def main():
    scene = "menu"
    menu = MenuScene()
    game = GameScene()
    settings = SettingsScene()

    while True:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()

        if scene == "menu":
            action = menu.update(events)
            menu.draw(screen)
            if action == "game":
                scene = "game"
            elif action == "settings":
                scene = "settings"
            elif action == "quit":
                pygame.quit(); sys.exit()

        elif scene == "game":
            action = game.update(events)
            game.draw(screen)
            if action == "menu":
                scene = "menu"

        elif scene == "settings":
            action = settings.update(events)
            settings.draw(screen)
            if action == "menu":
                scene = "menu"

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
